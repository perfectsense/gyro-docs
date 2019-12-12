Modeling
========

Each resource must extend the `Resource <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/resource/Resource.java>`_
class.

Naming a Resource
-----------------

Each resource gets its name from a combination of the ``@Namespace`` and ``@Type`` annotations. The root package in
each provider should have ``package-info.java`` that is annotated with the ``@Namespace`` annotation. For example:

.. code-block:: java

    @Namespace("aws")
    package gyro.provider.aws;

    import gyro.core.Namespace;
    import gyro.core.resource.DocNamespace;

Use the ``@Type(<string>)`` annotation on the resource implementation class to specify the resource name, for
example:

.. code-block:: java

    @Type("vpc")
    public class VpcResource extends Resource {
      ...
    }

When combined these annotations provide the name exposed to Gyro, ``aws::vpc``, in this example.

Properties
----------

Model a resource by looking at both the cloud providers web console and their API to see what properties a
resource uses.

A general rule of thumb is to model a resource similar to the cloud provider's API model and adjust based on how the
API is exposed on the provider's web console. In some instances the cloud provider's web console will hide some of the
complexity of the API and part of the modeling process is to determine if that abstraction should be kept.

As an example, a basic ``aws::vpc`` resource has a cidr block, dns settings, and tags. The model might look like
the following:

.. code-block:: java

    @Type("vpc")
    public class VpcResource extends Resource {

        private String cidrBlock;
        private Boolean enableDnsHostnames;
        private Boolean enableDnsSupport;
        private Map<String, String> tags;

        public String getCidrBlock() {...}
        public void setCidrBlock(String cidrBlock) {...}

        ...
    }

Each property will be exposed in the Gyro configuration language by converting the getter method from camel case to
lowercase with dashes -- ``getCidrBlock`` becomes ``cidr-block``. Using the ``VpcResource`` resource above, in Gyro
it would be configured as:

.. code-block:: java

    aws::vpc vpc
        cidr-block: "10.0.0.0/16"
        enable-dns-hostnames: true

        tags: {
            Name: "Gyro VPC"
        }
    end

Annotations
-----------

There are several annotations that should be used when modeling a resource. These annotations give Gyro extra
information necessary when running the diff engine.

@Id
~~~

The property that is the unique identifier of the resource in the cloud should be annotated with ``@Id``. This is
used by Gyro to create placeholder objects when a user provides the id as a string value rather than as a
reference to an existing resource.

@Output
~~~~~~~

Any property that is output only (i.e cannot be set by the user) should be annotated with ``@Output``. This is currently
only used by the documentation system.

@Updatable
~~~~~~~~~~

By default properties are not considered updatable in Gyro. This means Gyro will attempt to replace a resource
if a property changed. However, if the cloud provider API supports changing the property, add the ``@Updatable``
annotation to the getter method and Gyro will call the ``update(GyroUI ui, State state, Resource config, Set<String> changedProperties)``
method of the resource with the names of the properties that changed passed into ``changedProperties``.
