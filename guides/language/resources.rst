Resources
+++++++++

Resources are the primary type in Gyro. Gyro is built around defining resources. A resource is the
definition of your cloud resource. Gyro will create, update, or delete your cloud resources to keep
them consistent with the definition of resources in a Gyro file.

A resource is a group of key/value pairs and subresources. Resources can have one or more key/value
pairs and zero or more subresources.

Here is an example of a AWS instance resource defined using the Gyro language:

.. code::

    aws::instance web-server
        ami: $(external-query aws::ami { name: "amzn-ami-hvm-2018.03.0.20181129-x86_64-gp2" }).0.id
        instance-type: "t2.micro"
        key: $(aws::key-pair key-pair-example)
        subnet: $(aws::subnet subnet)
        security-groups: [
            $(aws::security-group webserver)
        ]

        tags: {
            Name: "web-server"
        }
    end

The syntax of this resource is:

.. code::

    <RESOURCE TYPE> <RESOURCE NAME>
        <KEY>: <VALUE>

        <SUBRESOURCE>
            <KEY>: <VALUE>
        end
    end

- **RESOURCE TYPE** is the name of the resource as provided by a provider plugin (e.g. ``aws::instance``).
- **RESOURCE NAME** is a name you give this instance of the resource. This name is used by Gyro to
  track state of the resource. It's also used when referencing a resource in your own Gyro code.
- **KEY/VALUES** map the settings for a particular resource. For more information on what valid keys
  and values are see the "Key/Values" section below.
- **SUBRESOURCE** are resources tied directly to their parent resource.

References
----------

Resources can be referenced by the resource name. Using the example above we can reference the ``aws::instance``
using the following syntax:

.. code::

    $(aws::instance web-server)

Use dot notation to references key/value pairs within a resource:

.. code::

    $(aws::instance web-server).instance-type

Use index notation to reference a list value:

.. code::

    $(aws::instance web-server).security-groups.0.group-id

Use wildcard notation to reference multiple instances:

.. code::

    $(aws::instance web*).public-ip-address
