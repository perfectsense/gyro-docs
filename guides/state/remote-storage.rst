.. _remote-storage:

Remote Storage
--------------

It is possible to store all state files in a remote storage location. Storing state files in a remote backend
provides many benefits, such as ensuring all team members are using the most up to date state files and
keeping potentially sensitive information off of members' local disks. Setting up a remote state backend is a
simple process, and Gyro makes migrating between various backends easy as well.

.. note:: We **strongly encourage** using :ref:`state locking <locking>` whenever using remote storage.

Configuring Remote Backends
+++++++++++++++++++++++++++

A remote state backend is configured in your ``init.gyro`` using the ``@state-backend`` directive. **Gyro cannot
use more than one state backend to store state files**.

In order to configure a remote state backend, first read the documentation for the state backend in your corresponding
provider. Next, to use that state backend, add the ``@state-backend`` directive to your ``init.gyro`` with
its necessary fields. For example, the following would store all state files in an S3 bucket named ``my-gyro-state``,
under the ``.gyro/state`` prefix:

.. code:: shell

    @state-backend 'aws::s3'
        bucket: "my-gyro-state"
        prefix: ".gyro/state"
    @end

If you previously have been storing state files on your local disk, you should use the
:ref:`state copy command <migrating-backends>` to push all your local state files up to your new remote state backend.

After configuring your state backend, running Gyro should function the same as before, requiring no additional prompts
or configurations. However, now state files will no longer be stored locally in your ``.gyro/state`` directory.
Also, when running Gyro, you will notice a message indicating that all state files were successfully pushed up to
the remote backend:

.. code:: shell

    $ gyro up
    ↓ Loading plugin: gyro:gyro-aws-provider:1.4.11

    Looking for changes...

    + Create aws::vpc vpc

    Are you sure you want to change resources? (y/N) y

    + Creating aws::vpc vpc OK

    Pushing state files to remote backend... OK

.. _migrating-backends:

Migrating Backends
++++++++++++++++++

There may come a time when you wish to stop using one provider's state backend and switch to another. Or you may
have been using your local machine for state storage, but would now like to migrate all state files to a remote backend.
The ``gyro state copy command`` can be used for this purpose, as it copies all state files between remote state
backends as well as your local state backend.

.. code:: shell

    gyro state copy --from <backend-name> --to <backend-name>

In the above command, ``<backend-name>`` is the name of the ``@state-backend`` from your ``init.gyro``. If your state
backend has no name, eg. ``@state-backend 'aws::s3'``, use ``default`` for your ``<backend-name>``. If you want to copy
to/from your local directory, use ``local`` for your ``<backend-name>``.

For example, if you'd like to copy all state files from your local backend to your default state backend, run:

.. code:: shell

    gyro state copy --from local --to default

Now let's say you have been using your default S3 state backend, but would like to migrate now to using GCP storage.
First, add the new state backend to your init and give it a name:

.. code:: shell

    @state-backend 'gcp::storage', 'new-backend'
        bucket: "my-gcp-gyro-state"
        prefix: ".gyro/state"
    @end

Next, to copy all state files from your default S3 backend to the new GCP backend, run:

.. code:: shell

    gyro state copy --from default --to new-backend

This will copy all files from ``default`` to ``new-backend``. You may now delete all the state files from your
S3 bucket if desired. In order to start using the GCP backend as your new state backend, remove the
S3 state backend from your ``init.gyro``, and remove the ``new-backend`` name from your GCP state backend.

.. note:: This command doesn't delete the copied files. All files that will be copied are listed and given a confirmation prompt before copying. **All duplicate existing files in the** ``--to`` **backend will be overwritten.**

Recovering from Errors
++++++++++++++++++++++

As state files are modified during resource updating/creating, they are written to a local temporary directory.
Writing to a temporary local directory minimizes the number of remote writes and also gives Gyro a way to recover
in case writing to remote fails. If the write to remote fails, you will see an error message directing you to run
``gyro up`` again:

.. code:: shell

    $ gyro up
    ↓ Loading plugin: gyro:gyro-aws-provider:1.4.11

    Looking for changes...

    + Create aws::vpc vpc

    Are you sure you want to change resources? (y/N) y

    + Creating aws::vpc vpc OK

    Pushing state files to remote backend...

    Error pushing state files to remote: Can't open ec2/ami.gyro in gyro.aws.S3FileBackend for writing!

    Run 'gyro up' again to retry.

The resources themselves have been successfully created/updated, however the state files in your remote backend are now
out of sync. When running Gyro again, Gyro will automatically detect the state files that failed, and direct you to
try to push them up again:

.. code:: shell

    $ gyro up
    ↓ Loading plugin: gyro:gyro-aws-provider:1.4.11

    Temporary state files were detected, indicating a past failure pushing to a remote backend.
    Would you like to attempt to push the files to your remote backend? (y/N) y
    + Copy file: ec2/ami.gyro

    Are you sure you want to copy all files? This will overwrite existing files! (y/N) y
    + Copying file: ec2/ami.gyro

    Looking for changes...

    No changes.

.. note:: If using :ref:`state locking <locking>`, the lock will remain locked if the push to remote fails. Therefore, it is important to run ``gyro up`` again to let Gyro recover the state as well as unlock the lock.
