Installing Gyro
+++++++++++++++

Official distributions of Gyro are available for macOS, Linux, and Windows operating systems. These distributions
include a minimal OpenJDK 11 so it is not necessary to download and install Java.

Official distributions are:

================== =================
OS                  Archive
================== =================
**macOS**          `gyro-cli-osx-0.15-20190827.211110-49.zip <https://artifactory.psdops.com/gyro-snapshots/gyro/gyro-cli-osx/0.15-SNAPSHOT/gyro-cli-osx-0.15-20190827.211110-49.zip>`_
**Linux**          `gyro-cli-linux-0.15-20190827.211008-49.zip <https://artifactory.psdops.com/gyro-snapshots/gyro/gyro-cli-linux/0.15-SNAPSHOT/gyro-cli-linux-0.15-20190827.211008-49.zip>`_
**Windows**        `gyro-cli-windows-0.99.0-20191002.121244-5.zip <https://artifactory.psdops.com/gyro-snapshots/gyro/gyro-cli-windows/0.99.0-SNAPSHOT/gyro-cli-windows-0.99.0-20191002.121244-5.zip>`_
================== =================

The easiest installation method is to download the distribution and extract it.

For Linux, and macOS extracting directly to ``/usr/local/bin`` will ensure the ``gyro`` binary is in
your path. Alternatively you can unzip Gyro to your preferred location and then ensure the ``gyro``
binary is in your ``PATH``. These distributions contain two artifacts, the ``gyro`` binary, and the
``gyro-rt/`` directory containing a minimal JDK runtime.

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

For Windows, extract the distribution to your preferred location and ensure the ``gyro`` executable is in your path. We
recommend adding the following to your Powershell profile to ensure Unicode characters output properly:

.. code:: powershell

    $OutputEncoding = [console]::InputEncoding = [console]::OutputEncoding = New-Object System.Text.UTF8Encoding


