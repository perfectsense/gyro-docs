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

    @plugin: 'gyro:gyro-aws-provider:0.99.0-SNAPSHOT'

@repository
-----------

This directive adds a Maven repository that Gyro will use to load plugins. It takes a single argument that
is the URL to the repository to search.

By default only the Maven central repository is searched for plugins.

.. note:: This directive can only be used in ``.gyro/init.gyro``.

**Example**

.. code::

    @repository: 'https://artifactory.psdops.com/public'
    @repository: 'https://artifactory.psdops.com/gyro-snapshots'

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


@virtual
--------

See :ref:`virtual-resource`.

@for
----

See :ref:`for-loop`.

@if
---

See :ref:`if-expression`.
