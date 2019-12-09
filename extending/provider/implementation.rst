Implementation
--------------

Every cloud provider is made up of one or more resources. Each resource implementation will manage the lifecycle
of a resource in the cloud: create, read, update, and delete.

A resource is any entity in a cloud provider that has state. For example, ``aws::load-balancer`` or
``aws::instance`` are resources with state where-as a service like AWS Rekognition has no persistent state so
it would not need to be implemented as a resource in Gyro.

With the exception of ``refresh()`` all CRUD methods provide a ``GyroUI`` and ``State`` objects.

The ``GyroUI`` objects can be used to output additional information to the user's console.

The ``State`` object can be used to periodically save state between operations within one of the CRUD methods. For
example, if creation of an object requires multiple API calls then state should be saved (i.e. ``state.save()``) between
each API call to ensure state has a view consistent with the cloud provider's state.

Implementing refresh
====================

The ``refresh()`` method is called to refresh the state of a resource. Gyro will call this method on every
resource loaded from state. Any properties saved in state will set on the resource prior to calling this method.

Implementations should reload the resource properties using cloud provider APIs. This ensures that Gyro can detect
changes to a resource that were made outside of Gyro, such as the providers web console.

If a resource cannot be found this method should return **false**, otherwise return **true** to indicate the
resource was refreshed.

.. note::

    Lists and sets in a resource should be cleared (i.e. ``myset.clear()``) prior to updating them to ensure
    the any values that may have been removed is reflected in the updated resource.

    .. code-block:: java

        getVolumes().clear();
        getVolumes().add(volume);

The following is an example implementation of ``refresh()`` for an EBS volume in AWS:

.. code-block:: java

     @Override
     protected boolean refresh() {
         Ec2Client client = createClient(Ec2Client.class);

         Volume volume = getVolume(client);

         if (volume == null) {
             return false;
         }

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

         DescribeVolumeAttributeResponse responseAutoEnableIo = client.describeVolumeAttribute(
             r -> r.volumeId(getId()).attribute(VolumeAttributeName.AUTO_ENABLE_IO)
         );

         setAutoEnableIo(responseAutoEnableIo.autoEnableIO().value());

         return true;
     }

Implementing create
===================

The ``create(GyroUI ui, State state)`` method is called to create a resource. Gyro will call this method for every resource
it determines needs to be created.

Implementations should create the resource and update any output properties after creation. At a minimum the id
that uniquely identifies the resource in the cloud provider should be set.

.. note::

    Call ``state.save()`` in the create method after each API call that creates/updates the resource. This is necessary
    when the cloud provider requires an API call to create the resource, then subsequent API calls to update
    specific properties. If there is only one API call to create a resource then calling ``state.save()`` is not
    necessary as Gyro will call it one more after returning from the create method.

The following example implementation creates an EBS volume in AWS:

.. code-block:: java

    @Override
    protected void create(GyroUI ui, State state) {
        Ec2Client client = createClient(Ec2Client.class);

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

Implementing update
===================

The ``update(GyroUI ui, State state, Resource config, Set<String> changedProperties)`` method is called by Gyro when
it determines that one or more resource properties should be updated. This method will only be called if the properties
that changed are marked with the ``@Updatable`` annotation. In cases where both updatable and non-updatable properties are
changed this method will not be called, instead if a workflow exists for this the resource type it will be executed,
otherwise all changes will be skipped.

The ``changedProperties`` set contains the names of fields that changed. This allows implementations to minimum the
of API calls necessary to effect an update.

The following example implementation updates an EBS volume in AWS:

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

Implementing delete
===================

The ``delete(GyroUI ui, State state)`` method is called by Gyro when it determines that a resource should be deleted
from the cloud provider. The resource implementation should delete the resource from the cloud provider.
