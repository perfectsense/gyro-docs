Updating Infrastructure
-----------------------

Things never stay the same for long. Cloud infrastructure is no different. In this section we'll show you
how easy it is to update your infrastructure using Gyro.

Let's give our new instance a name so that it's purpose is clear within the AWS web console. To add tags
we just edit our configuration file and field named ``tags`` with a map of key/value pairs.

.. code::

    ami-id: $(external-query aws::ami {
        name: 'ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-20190628',
        architecture: 'x86_64',
        root-device-type: 'ebs',
        virtualization-type: 'hvm',
        owner-id: '099720109477',
        state: 'available'
    }).0.id

    aws::instance webserver
        ami: $(ami-id)
        instance-type: "t3.nano"

        tags: {
            Name: "webserver",
            Project: "gyro"
        }
    end

To effect this change we run the same command we did to create the infrastructure, ``gyro up``. This time
Gyro will show that its going to modify the existing instance to add the tags:

.. code::

    $ gyro up
    ↓ Loading plugin: gyro:gyro-aws-provider:1.4.7
    ⟳ Refreshed resources: 1

    Looking for changes...

    ⟳ Update aws::instance webserver (i-00b86f46e69e6d5bb)
    · tags:  +{ Name: 'webserver', Project: 'gyro' }

    Are you sure you want to change resources? (y/N) y

    ⟳ Updating aws::instance webserver (i-00b86f46e69e6d5bb) OK

In the next section we'll show how what happens if we remove the instance configuration.

