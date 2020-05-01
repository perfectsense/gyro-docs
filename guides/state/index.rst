State
=====

For each configuration file you use to manage resources, Gyro automatically creates a corresponding
state file. These state files are used by Gyro to determine which resources have already been created and to keep
track of metadata. By default, these state files are stored in your local ``.gyro/state`` directory. It is possible
to store these state files in a remote storage location, as described by :ref:`remote-storage`. In addition, if
multiple users are using Gyro at the same time, we recommend configuring :ref:`locking` to prevent users modifying the
same resources at the same time.

.. toctree::
    :maxdepth: 1

    locking
    remote-storage
