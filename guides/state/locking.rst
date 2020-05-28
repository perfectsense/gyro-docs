.. _locking:

Locking
-------

Locking is used to prevent multiple users from reading and writing state files at the same time. Once properly
configured, a user running a command that reads or writes state files will obtain and hold the lock until the command
finishes running. If another user attempts to run a command during that time, they will be given an error message,
and must wait until the lock owner has finished.

Configuring Locking
+++++++++++++++++++

In order to configure a locking backend, simply add a ``@lock-backend`` to your ``init.gyro``. Read the documentation
for the provider of your choosing in order to find out what types of backends are available, as well as the necessary
fields. It is important to read the provider's documentation as some lock backends may require specific configurations
when creating the tables. The following example would create a DynamoDb lock backend using a table named
``gyro-lock-table``:

.. code:: shell

    @lock-backend 'aws::dynamo-db'
        table-name: "gyro-lock-table"
    @end

After configuring locking, running Gyro will appear exactly the same. Gyro will automatically lock when running a
command that modifies state, and will unlock automatically when that command finishes.

If a user attempts to run a command while the state is locked, their execution will terminate, and they will be given
an error message detailing information about the lock similar to below:

.. code:: shell

    $ gyro up
    ↓ Loading plugin: gyro:gyro-aws-provider:0.99.1

    Error: State is currently locked!
    Current lock ID: 'adf4feb3-3333-447e-89d9-819da078618d'.
    Locked by 'gyro-user' running 'up ec2/ami.gyro' at '16:38:29 EDT, Apr-27'.

Force Unlocking
+++++++++++++++

Locking is meant to prevent users from running commands at the same time and potentially corrupting the state. There
should be very few scenarios when using locking where a lock becomes stuck. As such, if a user sees an error message
saying the state is locked, they should simply wait until the state is unlocked. However, in the rare scenarios where
you believe the lock is stuck and should be unlocked, you may use the ``force-unlock`` command:

.. code:: shell

    gyro state force-unlock --lock-id <lock-id>

In the above command, the ``<lock-id>`` is a required field that ensures when force unlocking, we are always unlocking
the correct lock. This lock ID can be retrieved simply by running ``gyro up`` and copying the ID from the outputted
error message.

.. note:: If using :ref:`remote state storage <remote-storage>` and an exception occurs during the push to remote, the lock will **not unlock**. In this scenario, running ``gyro up`` again will allow Gyro to automatically recover the state as well as unlock the lock.