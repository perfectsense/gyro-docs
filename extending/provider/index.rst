Adding a Provider
=================

Provider plugins extend Gyro by making new cloud resource types available to the Gyro language. Each resource
implementation is responsible for refreshing, creating, updating, and deleting a cloud resource.

Provider plugins are written in Java and distributed using the Maven repository system.

.. toctree::
    :maxdepth: 1

    credentials
    implementation
    code-organization
    documentation