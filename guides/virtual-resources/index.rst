.. _virtual-resource:

Virtual Resource
================

The ``@virtual`` directive defines a virtual resource. A virtual resource groups resource definitions together into a single
virtual resource much like a function in a full programming language.

A virtual resource can define arguments that must be passed in using the ``@param`` directive.

**Example**

.. code::

    @virtual myproject::network
        @param name

        aws::vpc vpc
            cidr-block: '10.0.0.0/16'

            tags: {
                Name: "$name project"
            }
        end
    @end

To use this virtual resource define a resource using the name you gave the virtual resource:

.. code::

    myproject::network dev-network
        name: "development"
    end

To reference resources created by the virtual resource prepend the resource name you provided when
using the virtual resource followed by the name of the resource inside the virtual resource definition:

.. code::

    aws::subnet mysubnet
        vpc: $(aws::vpc dev-network/vpc)
    end
