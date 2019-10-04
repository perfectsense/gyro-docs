Resolver
========

Resolvers are one of several options that Gyro provides to extend itself.
A resolver can accept one or more arguments that is processed and a value is returned based off of that. A resolver can be as simple as somthing returning a transformation of the arguments passed in or more complex like querying an external source to resolve the arguments into a usefuls value.

**Why Resolvers?**

Resolvers allow you to be more flexible with the values you use in the gyro configuration files.
Typically when you use values in the configuration files, not all of them are static in nature, some could be references from other configurations, some may need transformations like getting a site name from a field which has a full url, some might need querying from an external source like looking up an id from an external query based on some criteria. All these can be done using resolvers giving you a finer control over the configurations.

.. toctree::
    :maxdepth: 1

    define
    implementation
