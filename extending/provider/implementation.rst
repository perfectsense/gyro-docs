Implementation
--------------

Annotations
+++++++++++

**@Type(string)**
    The class should be annotated with the ``@Type(string)`` annotation. The name provided by this annotation is
    used by the Gyro language to lookup the resource implementation. For example, ``@Type("instance")`` in the AWS
    provider will make ``aws::instance`` available to the Gyro language.

    The Java package(s) that make up a provider should be annotated with one or more of the following:

**@Namespace(string)**
    This is name the primary namespace of the provider that will be exposed to the Gyro language. For example, for
    the resource ``aws::instance`` this annotation defines the ``aws`` portion of the resource name. The namespace
    should be short, all-lower case, unique, and concisely describe the provider.

    This is a ``package`` annotation intended to be used in a ``package-info.java`` file at the root of the provider
    projects main package.

**@DocNamespace(string)**
    Same as above but used for auto-generated documentation.

**@DocGroup(string)**
    As explained above each provider should be logically separated into packages based on the provider's API and
    service groupings. Each of these service group packages should define this annotation.

    This is a ``package`` annotation intended to be used in a ``package-info.java`` file.

Fields should be annotated with one of the following annotations, if applicable:

**@Id**
    This annotation marks the field that is the unique identifier for the resource.

**@Output**
    This annotation marks fields that are read-only and that will be updated after the initial creation of a resource. This
    annotation's primary purpose is for auto-generated documentation.

**@Updatable**
    This annotation marks fields which can be updated independently using the provider's API.

Methods
+++++++

Each resource must extend the abstract ``Resource`` class and implement the interface ``Copyable`` class. The below given method must be implemented by each of the Resource Type class.

.. code-block:: java

    Resource.java

    public abstract class Resource extends Diffable {
        public abstract boolean refresh();
        public abstract void create(GyroUI ui, State state);
        public abstract void update(GyroUI ui, State state, Resource current, Set<String> changedFieldNames);
        public abstract void delete(GyroUI ui, State state);
    }

 -------------------------------------------------------------------------------------------------------------------------------------------

    Copyable.java

    public interface Copyable<M> {

        void copyFrom(M model);

    }


The ``GyroUI`` parameter in create, update and delete method is responsible for displaying the output on the console UI and the ``State`` parameter is responsible to generate and update state files for the resources.

**refresh()**

The ``refresh()`` method is called by Gyro to refresh the state of a resource. Implementations should query the
provider API and return the response resource data.

If the object no longer exists in the cloud provider this method should return ``false``, otherwise it passes the call to the ``copyFrom`` method which sets the resource data and returns ``true`` to
indicate the data has been updated.

The copyFrom implementation update the current object instance with the cloud instance data.

The following example implementation of ``refresh()`` updates an EBS volume in AWS.

.. code-block:: java

     @Override
     protected boolean refresh() {
         Ec2Client client = createClient(Ec2Client.class);

         Volume volume = getVolume(client);

         if (volume == null) {
             return false;
         }

         copyFrom(volume);

         return true;
     }

     @Override
     public void copyFrom(Volume volume) {
         setId(volume.volumeId());
         setAvailabilityZone(volume.availabilityZone());
         setCreateTime(Date.from(volume.createTime()));
         setEncrypted(volume.encrypted());
         setIops(volume.iops());
         setKms(!ObjectUtils.isBlank(volume.kmsKeyId()) ? findById(KmsKeyResource.class, volume.kmsKeyId()) : null);
         setSize(volume.size());
         setSnapshot(!ObjectUtils.isBlank(volume.snapshotId()) ? findById(EbsSnapshotResource.class, volume.snapshotId()) : null);
         setState(volume.stateAsString());
         setVolumeType(volume.volumeTypeAsString());

         Ec2Client client = createClient(Ec2Client.class);

         DescribeVolumeAttributeResponse responseAutoEnableIo = client.describeVolumeAttribute(
             r -> r.volumeId(getId())
                 .attribute(VolumeAttributeName.AUTO_ENABLE_IO)
         );

         setAutoEnableIo(responseAutoEnableIo.autoEnableIO().value());
     }

**create(GyroUI ui, State state)**

The ``create(..)`` method is called by Gyro when it determines that it should create a resource. Implementations should
create the resource and update any unique ID fields on the current object instance that will be necessary to query for
the resource ``refresh()`` method.

Gyro will call ``create(..)`` if the resource does not exist in state or if a non-updatable field has been modified. In
the later case Gyro will first call ``delete(..)``.

The following example implementation of ``create(GyroUI ui, State state)`` creates an EBS volume in AWS:

.. code-block:: java

    @Override
    protected void create(GyroUI ui, State state) {
        Ec2Client client = createClient(Ec2Client.class);

        validate(true);

        CreateVolumeResponse response = client.createVolume(
            r -> r.availabilityZone(getAvailabilityZone())
                .encrypted(getEncrypted())
                .iops(getVolumeType().equals("io1") ? getIops() : null)
                .kmsKeyId(getKms() != null ? getKms().getId() : null)
                .size(getSize())
                .snapshotId(getSnapshot() != null ? getSnapshot().getId() : null)
                .volumeType(getVolumeType())
        );

        setId(response.volumeId());
        setCreateTime(Date.from(response.createTime()));
        setState(response.stateAsString());
    }

**update(GyroUI ui, State state, AwsResource config, Set<String> changedProperties)**

The ``update(..)`` method is called by Gyro when it determines that a resource attribute can be updated. This method
will only be called if the fields that changed are marked with the ``@Updatable`` annotation. In cases where
both updatable and non-updatable fields are changed Gyro will not call this method, instead it will call ``delete()``
followed by ``create()``.

The ``changedProperties`` set contains the names of fields that changed. This allows implementations to minimum the
of API calls necessary to effect an update.

The following example implementation of ``update(..)`` updates an EBS volume in AWS:

.. code-block:: java

    @Override
    protected void update(GyroUI ui, State state, AwsResource config, Set<String> changedProperties) {
        Ec2Client client = createClient(Ec2Client.class);

        if (changedProperties.contains("iops") || changedProperties.contains("size") || changedProperties.contains("volume-type")) {

            client.modifyVolume(
                r -> r.volumeId(getId())
                    .iops(getVolumeType().equals("io1") ? getIops() : null)
                    .size(getSize())
                    .volumeType(getVolumeType())
            );
        }

        if (changedProperties.contains("auto-enable-io")) {
            client.modifyVolumeAttribute(
                r -> r.volumeId(getId())
                    .autoEnableIO(a -> a.value(getAutoEnableIo()))
            );
        }
    }

**delete(GyroUI ui, State state)**

The ``delete(GyroUI ui, State state)`` method is called by Gyro when it determines that a resource should be deleted from the provider. The
resource implementation should delete the resource from the provider.