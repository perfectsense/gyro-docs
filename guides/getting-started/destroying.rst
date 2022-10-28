Destroying Infrastructure
-------------------------

Just as Gyro will detect new or changed resources, it will also detect that a resource has been
removed from the configuration and will delete the resource from the cloud.

Using our previous examples, delete the ``instance.gyro`` file and run ``gyro up`` to see
how Gyro handles the deletion of resources.

.. code::

    $ rm instance.gyro
    $ gyro up --no-verbose
    ↓ Loading plugin: gyro:gyro-aws-provider:1.5.0
    ⟳ Refreshed resources: 1

    Looking for changes...

    - Delete aws::instance webserver (i-00b86f46e69e6d5bb)

    Are you sure you want to change resources? (y/N) y

    - Deleting aws::instance webserver (i-00b86f46e69e6d5bb)

That's the basics of Gyro.
