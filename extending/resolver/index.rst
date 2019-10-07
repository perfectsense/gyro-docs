Adding a Resolver
=================

Resolvers are how Gyro looks up all variable references (i.e. ``$(variable)`` or ``$(aws::instance frontend)``). The
default resolver will look up variable and resource references using Gyro's internal scoping rules. Gyro also provides
the ``external-query`` resolver for querying for resources in the cloud that Gyro doesn't directly control.

.. toctree::
    :maxdepth: 1

    implementation
    use
