Variables
+++++++++

Variables in Gyro defined using the ``key: value`` syntax.

Scoping
-------

There are three levels of scoping: **resource**, **file**, and **global**.

*Resource* scoped variables are defined inside of a resource definition. In the example below
``image-id`` and ``instance-type`` are resource scoped variables. These variables can only be
referenced from within the resource using the implicit ``$SELF`` variable.

.. code::

    aws::instance webserver
        image-id: "ami-0cd3dfa4e37921605"
        instance-type: $server-size

        tags: {
            Name: "webserver \($SELF.instance-type)"
        }
    end

*File* scoped variables are defined within a Gyro configuration file but not within a resource
definition. In the example below ``project`` and ``server-size`` are file scoped variables.

.. code::

    project: "gyro"
    server-size: "t2.micro"

    aws::instance webserver
        image-id: "ami-0cd3dfa4e37921605"
        instance-type: $server-size

        tags: {
            Name: "webserver \($SELF.instance-type)"
        }
    end

*Global* scoped variables are defined in ``.gyro/init.gyro`` at the root of the Gyro project.

Scalar Types
------------

Gyro has the following scalar types: **string**, **number**, and **boolean**.

String literals are defined as is zero or more characters enclosed within single quotes (``'my value'``).

String expressions are defined as zero or more characters enclosed within double quotes. String expressions differ from string
literals in that reference expressions will be interpolated prior to using the value (``"my value with $(key)"``).

Numbers can be integers or floats (``10``, ``10.5``, ``-10``).

Booleans are defined as ``true`` or ``false``.

References
**********

Variables are referenced using the ``$name`` or ``$(name)`` syntax. Use ``$(name)`` to surround a variable name
when used inside a string.

Keys must be a valid identifer, or string literal. Identifiers can be made up of letters, digits, ``_``, or ``-``. Spaces
can be included in keys by quoting the key using single quotes (``'``).

Compound Types
--------------

Gyro has two compound types: **map**, and **list**.

Maps are zero or more comma-separated key/value pairs inside curly brackets (``{ key: 'value' }``).

Lists are zero or more comma-separated values inside square brackets (``['item1', 'item2']``).

References
**********

Maps can be referenced using dot notation with the key name:

.. code::

    tags: {
        Name: "Name"
        gyro-key: "value"
    }

    Name: $(tags).Name
    Value: $(tags).gyro-key

Lists can be referenced using index notation with the position of the list element you'd like to retrieve:

.. code::

    values: ["value1", "value2", "value3"]

    Value1: $(values).0
    Value2: $(values).1
    Value3: $(values).2
