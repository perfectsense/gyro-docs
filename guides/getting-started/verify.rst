Verify Installation
+++++++++++++++++++

Check that Gyro is installed and working by creating a small test configuration and running Gyro in test mode.

Start by creating a directory for your project and then initial Gyro inside the project directory. This will
become the root of your Gyro project.

.. code:: shell

    $ mkdir myproject
    $ cd myproject
    $ gyro init gyro:gyro-aws-provider:0.99.0-SNAPSHOT
    + Creating a new .gyro directory
    + Writing to the .gyro/init.gyro file

This will create a .gyro directory with an ``init.gyro`` file and will install all the plugins that
are required to spin up a resource.

.. code::

    @repository: 'https://artifactory.psdops.com/public'
    @repository: 'https://artifactory.psdops.com/gyro-snapshots'
    @plugin: 'gyro:gyro-aws-provider:0.99.0-SNAPSHOT'

We will be creating a VPC resource to test our installation.

Create a file named `test.gyro` in the `gyro` directory, with the following configs

.. code::

    aws::vpc vpc
      cidr-block: "10.0.1.0/16"
    end

To verify the installation run ``gyro up <file>`` in test mode. If ``y`` is given at the prompt,
gyro will generate a state file in the local directory ``.gyro/state/``, you can check your state
file here ``.gyro/state/test.gyro``.

.. code:: shell

    $ /usr/local/bin/gyro up --test test.gyro
    ↓ Loading plugin: gyro:gyro-aws-provider:0.15-SNAPSHOT

     Looking for changes...

     + Create aws::vpc vpc

     Are you sure you want to change resources? (y/N) y

     + Creating aws::vpc vpc OK
    $