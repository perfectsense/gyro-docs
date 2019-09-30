
Official distributions of Gyro are available for macOS, and Linux operating systems. Official distributions
include a stripped-down OpenJDK 11 so it is not necessary to download and install Java.

Official distributions are:

================== =================
OS                  Archive
================== =================
**macOS**          `gyro-cli-osx-0.15-20190827.211110-49.zip <https://artifactory.psdops.com/gyro-snapshots/gyro/gyro-cli-osx/0.15-SNAPSHOT/gyro-cli-osx-0.15-20190827.211110-49.zip>`_
**Linux**          `gyro-cli-linux-0.15-20190827.211008-49.zip <https://artifactory.psdops.com/gyro-snapshots/gyro/gyro-cli-linux/0.15-SNAPSHOT/gyro-cli-linux-0.15-20190827.211008-49.zip>`_
================== =================

macOS and Linux
+++++++++++++++

Download the distribution and extract it into ``/usr/local/bin``. For example:

.. code:: shell

    $ unzip -d /usr/local/bin gyro-cli-osx-0.15-20190827.211110-49.zip

     Archive:  gyro-cli-osx-0.15-20190827.211110-49.zip
      creating: /usr/local/bin/gyro-rt/
      creating: /usr/local/bin/gyro-rt/bin/
      inflating: /usr/local/bin/gyro-rt/bin/java
      inflating: /usr/local/bin/gyro-rt/bin/jrunscript
      inflating: /usr/local/bin/gyro-rt/bin/keytool
      creating: /usr/local/bin/gyro-rt/conf/
      inflating: /usr/local/bin/gyro-rt/conf/logging.properties
      .
      .
      .
      inflating: /usr/local/bin/gyro-rt/release
      inflating: /usr/local/bin/gyro
    $

Test Your Installation
++++++++++++++++++++++

Check that Gyro is installed and working by creating a small test configuration and running Gyro in test mode.

Start by creating a gyro directory in your project folder and an initial configuration file named ``init.gyro``, which gets created by running the following command:

 ``gyro init gyro:gyro-aws-provider:0.15-SNAPSHOT``

This will create a .gyro directory with an ``init.gyro`` file and will install all the plugins that are required to spin up a resource.

.. code::

    @repository: 'https://artifactory.psdops.com/public'
    @repository: 'https://artifactory.psdops.com/gyro-snapshots'
    @plugin: 'gyro:gyro-aws-provider:0.15-SNAPSHOT'

We will be creating a VPC resource to test our installation.

Create a file named `test.gyro` in the `gyro` directory, with the following configs

.. code::

    aws::vpc vpc
      cidr-block: "10.0.1.0/16"
    end

To verify the installation run ``gyro up <file>`` in test mode. If ``y`` is given at the prompt, gyro will generate a state file in the local directory ``.gyro/state/``, you can check your state file here ``.gyro/state/test.gyro``.

.. code:: shell

    $ /usr/local/bin/gyro up --test test.gyro
    ↓ Loading plugin: gyro:gyro-aws-provider:0.15-SNAPSHOT

     Looking for changes...

     + Create aws::vpc vpc

     Are you sure you want to change resources? (y/N) y

     + Creating aws::vpc vpc OK
    $
