Built-in Directives
+++++++++++++++++++

Gyro comes with the following built-in directives.

@plugin
-------

This directive loads a Gyro plugin from a Maven repository. It takes a single argument in the format
``<artifact>:<group>:<version>`` for the plugin to be loaded.

Every Gyro project will have at least one ``@plugin`` directive call to load a cloud provider.

.. note:: This directive can only be used in ``.gyro/init.gyro``.

**Example**

.. code::

    @plugin: 'gyro:gyro-aws-provider:0.99.1'

@repository
-----------

This directive adds a Maven repository that Gyro will use to load plugins. It takes a single argument that
is the URL to the repository to search.

By default only the Maven central repository is searched for plugins.

.. note:: This directive can only be used in ``.gyro/init.gyro``.

**Example**

.. code::

    @repository: 'https://artifactory.psdops.com/public'
    @repository: 'https://artifactory.psdops.com/gyro-releases'

@credentials
------------

This directive defines credentials to be used by Gyro. It takes the name of the credentials provider, and optionally,
a name for these credentials. Any attributes defined in the body of this directive will be passed to the credential
provider implementation.

If a name is not provided, ``default`` will be used.

.. note:: This directive can only be used in ``.gyro/init.gyro``.

**Example**

.. code::

    @credentials 'aws::default'
        profile-name: "my-project"
        region: 'us-east-1'
    @end

@file-backend
-------------

This directive defines a file backend implementation to be used by Gyro. It takes the name of the file backend
provider implementation and a name. Any attributes defined in the body of this directive will be passed to the
file backend provider implementation.

.. note:: This directive can only be used in ``.gyro/init.gyro``.

**Example**

.. code::

    @file-backend 'aws::s3', 'builds'
        bucket: 'builds-bucket'
    @end

@print
------

This directive takes single argument and prints it. This can be used to debug external queries or references. Resources
are output to JSON format.

**Example**

.. code::

    @print: $(external-query aws::ami { name: 'gyro' })

**Outputs**

.. code::

    {
      "name" : "gyro",
      "id" : "ami-091b8328283d287be"
    }

.. _extends:

@extends
--------

This directive copies attributes from an existing resource into a new resource definition. It is intended to be used
when you want to create a new resource that is similar to an existing resource definition.

**Options**

-exclude <attribute>
    Exclude provided attribute from the copy. Use this to prevent ``@extends`` from copying attributes
    to the new resource.

-merge true|false
    When true, merge maps and lists defined in the source definition with those defined in the new definition. This
    defaults to false.

**Example** ::

    aws::instance webserver-1
        ami: "ami-05ecb1463f8f1ee4b"
        instance-type: "t3.nano"
        security-groups: $(aws::security-groups webserver-*)

        tags: {
            Name: "webserver-1"
            Project: "gyro"
        }
    end

    aws::instance webserver-2
        @extends: $(aws::instance webserver-1) -exclude private-ip-address -merge true

        tags: {
            Name: "webserver-2"
        }
    end

This equivalent to defining ``webserver-2`` as::

    aws::instance webserver-2
        ami: "ami-05ecb1463f8f1ee4b"
        instance-type: "t3.nano"
        security-groups: $(aws::security-groups webserver-*)

        tags: {
            Name: "webserver-2"
            Project: "gyro"
        }
    end


@depends-on
-----------

This directive sets up an external dependency between two resource definition. It is intended to be used when two resources are not dependent on on each other via resource reference but one resource needs another resource to exist in order to work.

**Example** ::

    aws::application-load-balancer alb-example
        name: "alb-example"
        ip-address-type: "ipv4"
        scheme: "internal"
        
        security-groups: [
            $(aws::security-group security-group),
            $(aws::security-group other-security-group)
        ]
        
        subnets: [
            $(aws::subnet subnet-us-east-2a),
            $(aws::subnet subnet-us-east-2b)
        ]
        
        tags: {
            Name: "alb-example"
        }

        @depends-on: $(aws::internet-gateway)
    end

    aws::internet-gateway internet-gateway
        vpc: $(aws::vpc vpc)
    end

The ``aws::application-load-balancer`` needs an ``aws::internet-gateway`` to be present for it to be created without any direct dependency. Having the ``@depneds-on`` will make sure the ``internet-gateway`` is created first before the ``application-load-balancer``.

@timeout
--------

This directive allows you to override a resource's default Wait logic if present for create, update and delete actions. It could be used when default wait times are not enough given more network latency, especially if creating resources in a distant region.

**Attributes**

at-most-duaration
    The max wait time before 

check-every-duration
    The interval after which you check for the wait condition to be satisfied. 

prompt
    If set to true, after the max wait time has elapsed, the user would be prompted to start the wait again or abort.

action
    Action determines which wait is overriden, CREATE for creation wait, UPDATE for update wait and DELETE for deletion waits.

**Example** ::

    aws::application-load-balancer alb-example
        name: "alb-example"
        ip-address-type: "ipv4"
        scheme: "internal"
        
        security-groups: [
            $(aws::security-group security-group),
            $(aws::security-group other-security-group)
        ]
        
        subnets: [
            $(aws::subnet subnet-us-east-2a),
            $(aws::subnet subnet-us-east-2b)
        ]
        
        tags: {
            Name: "alb-example"
        }

        @timeout
            action: CREATE
            at-most-duration: PT15M
        @end
    end

The wait time for ``aws::application-load-balancer alb-example`` is overriden for when its being created where the `at-most-duration` of the wait is set to 15 min.

@virtual
--------

See :ref:`virtual-resource`.

@for
----

See :ref:`for-loop`.

@if
---

See :ref:`if-expression`.
