Built-in Resolvers
+++++++++++++++++++

Gyro comes with the following built-in resolvers.

external-query
--------------

This resolver loads resources from the cloud providers that Gyro may or may not directly control. It takes two arguments, first specifying what resource to load for which provider in the format ``<provider>::<resource-name>``. The second is a map which will filter the resources to be loaded.

To query for resources using non-default credentials, use the ``-credentials <name>`` option. This can be used to
query for resources in a different account or region. 

.. note:: The result of queries will be cached and reused for identical queries in order to reduce external calls. Caching for a specific query may be disabled by using the ``-cache false`` option.

In order to load a resource using ``external-query`` the resource must implement the ``Finder`` API. While most resources will implement this API consult the provider's resource documentation for information on whether finder is supported or not.

.. note:: The external query will not work for a resource that has no finder implementation.

**Example**

.. code::

    $(external-query aws::ami {name = 'amzn-ami-hvm-2018.03.0.20181129-x86_64-gp2'})

.. code::

    $(external-query aws::ami {name = 'amzn-ami-hvm-2018.03.0.20181129-x86_64-gp2'} -credentials 'sandbox')
