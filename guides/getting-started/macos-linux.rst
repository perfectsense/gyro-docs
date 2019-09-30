Installing on macOS and Linux
+++++++++++++++++++++++++++++

Official distributions of Gyro are available for macOS, and Linux operating systems. Official distributions
include a stripped-down OpenJDK 11 so it is not necessary to download and install Java.

Official distributions are:

================== =================
OS                  Archive
================== =================
**macOS**          `gyro-cli-osx-0.15-20190827.211110-49.zip <https://artifactory.psdops.com/gyro-snapshots/gyro/gyro-cli-osx/0.15-SNAPSHOT/gyro-cli-osx-0.15-20190827.211110-49.zip>`_
**Linux**          `gyro-cli-linux-0.15-20190827.211008-49.zip <https://artifactory.psdops.com/gyro-snapshots/gyro/gyro-cli-linux/0.15-SNAPSHOT/gyro-cli-linux-0.15-20190827.211008-49.zip>`_
================== =================

The easiest installation method is to download the distribution and extract Gyro into ``/usr/local/bin``.  This will
install the ``gyro`` binary and the ``gyro-rt/`` directory with a small JVM runtime.

Alternatively you can unzip Gyro to your preferred location and then ensure the ``gyro`` binary is in your ``PATH``.

For example:

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


