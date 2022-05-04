Installing Gyro
+++++++++++++++

Official distributions of Gyro are available for macOS, Linux, and Windows operating systems. These distributions
include a minimal OpenJDK 11 so it is not necessary to download and install Java.

Official distributions are:

================== =================
OS                  Archive
================== =================
**macOS**          `gyro-cli-macos-1.1.3rc2.zip <https://artifactory.psdops.com/gyro-releases/gyro/gyro-cli-macos/1.1.3rc2/gyro-cli-macos-1.1.3rc2.zip>`_
**Linux**          `gyro-cli-linux-1.1.3rc2.zip <https://artifactory.psdops.com/gyro-releases/gyro/gyro-cli-linux/1.1.3rc2/gyro-cli-linux-1.1.3rc2.zip>`_
**Windows**        `gyro-cli-windows-1.1.3rc2.zip <https://artifactory.psdops.com/gyro-releases/gyro/gyro-cli-windows/1.1.3rc2/gyro-cli-windows-1.1.3rc2.zip>`_
================== =================

The easiest installation method is to download the distribution and extract it.

For Linux, and macOS extracting directly to ``/usr/local/bin`` will ensure the ``gyro`` binary is in
your path. Alternatively you can unzip Gyro to your preferred location and then ensure the ``gyro``
binary is in your ``PATH``. These distributions contain two artifacts, the ``gyro`` binary, and the
``gyro-rt/`` directory containing a minimal JDK runtime.

For example:

.. code:: shell

    $ unzip -d /usr/local/bin gyro-cli-linux-1.1.2.zip

     Archive:  gyro-cli-linux-1.1.0.zip
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

For Windows, extract the distribution to your preferred location and ensure the ``gyro`` executable is in your path. We
recommend adding the following to your Powershell profile to ensure Unicode characters output properly:

.. code:: powershell

    $OutputEncoding = [console]::InputEncoding = [console]::OutputEncoding = New-Object System.Text.UTF8Encoding

Verify Installation
-------------------

Check that Gyro is installed and working by creating a small test configuration and running Gyro in test mode.

Start by creating a directory for your project and then initial Gyro inside the project directory. This will
become the root of your Gyro project.

.. code:: shell

    $ mkdir myproject
    $ cd myproject
    $ gyro init gyro:gyro-aws-provider:1.4.0
    + Creating a new .gyro directory
    + Writing to the .gyro/init.gyro file

This will create a .gyro directory with an ``init.gyro`` file and will install all the plugins that
are required to spin up a resource.

.. code::

    @repository: 'https://artifactory.psdops.com/public'
    @repository: 'https://artifactory.psdops.com/gyro-releases'
    @plugin: 'gyro:gyro-aws-provider:1.4.0'

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
    ↓ Loading plugin: gyro:gyro-aws-provider:1.4.0

     Looking for changes...

     + Create aws::vpc vpc

     Are you sure you want to change resources? (y/N) y

     + Creating aws::vpc vpc OK
    $
