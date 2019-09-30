Documentation
-------------

Documentation for providers is auto-generated using a special Java Doclet. This doclet reads specially formatted comments
on the class and method implementations for each resource.

Each resource should have a class level comment describing what the resource is followed by at least one simple example
showcasing using the resource, such as:

.. code-block:: shell

    /**
     * Creates an Instance with the specified AMI, Subnet and Security group.
     *
     * Example
     * -------
     *
     * .. code-block:: gyro
     *
     *     aws::instance instance
     *         ami-name: "amzn-ami-hvm-2018.03.0.20181129-x86_64-gp2"
     *         shutdown-behavior: "stop"
     *         instance-type: "t2.micro"
     *         key-name: "instance-static"
     *     end
     */

Each resource field getter should have a single line comment with a description of the field, possible values, side
effect of the field, and whether the field is required or optional.

.. code-block:: shell

    /**
     * The ID of an AMI that would be used to launch the instance. (Required)
     */
    public String getAmiId() {
        return amiId;
    }

Generating Documentation
++++++++++++++++++++++++

Documentation is generated using the Gyro Doclet. To generate documentation using the Doclet add the following to
the providers ``build.gradle`` file, then run ``gradle referenceDocs``:

.. code-block:: shell

    task referenceDocs(type: Javadoc) {
        title = null // Prevents -doctitle and -windowtitle from being passed to GyroDoclet
        source = sourceSets.main.allJava
        classpath = configurations.runtimeClasspath
        options.doclet = "gyro.doclet.GyroDoclet"
        options.docletpath = configurations.gyroDoclet.files.asType(List)
    }
