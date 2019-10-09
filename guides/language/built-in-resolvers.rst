Built-in Resolvers
+++++++++++++++++++

Gyro comes with the following built-in resolvers.

external-query
--------------

This resolver loads resources from the cloud providers that Gyro may or may not directly control. It takes two arguments, first specifying what resource to load for which provider in the format ``<provider>::<resource-name>``. The second is a map which will filter the resources to be loaded.

Most resource will have a finder implementation associated with it.

.. note:: The external query will not work for a resource that has no finder implementation.

**Example**

.. code::

    $(external-query aws::ami {name = 'amzn-ami-hvm-2018.03.0.20181129-x86_64-gp2'})