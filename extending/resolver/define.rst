Defining a Resolver
-------------------

A resolver is defined using the ``$(<resolver-name> <arg1> <arg2>)`` notation. The resolver can take as many arguments as defined by the implementation.

For example:

.. code-block:: java

	$(external-query aws::ami { name: "amzn-ami-hvm-2018.03.0.20181129-x86_64-gp2" })

This resolver searches AWS for an AMI having a certain name. The resolver is called **external-query** which takes two arguments, the first one **aws::ami** tells the resolver what provider resource to process and resolve to, and the second one is a map of values to filter on.