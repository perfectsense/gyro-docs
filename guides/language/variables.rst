Variables
+++++++++

Variables in Gyro defined using the ``key: value`` syntax.

Scoping
-------

There are three levels of scoping: resource, file, and global.

To define a variable that is scoped to all files in a Gyro project, define the variable ``.gyro/init.gyro``. Variables
defined in Gyro files will override variables defined in ``.gyro/init.gyro``.

Variables are referenced using the ``$name`` or ``$(name)`` syntax. Use ``$(name)`` to surround a variable name
when used inside a string.

**Example:**

.. code::

    project: "gyro"
    server-size: "t2.micro"

    aws::instance webserver
        image-id: "ami-0cd3dfa4e37921605"
        instance-type: $server-size

        tags: {
            Name: "$(gyro)-$(server-size)"
        }
    end

Keys must be a valid identifer, or string literal. Identifiers can be made up of letters, digits, ``_``, or ``-``. Spaces
can be included in keys by quoting the key using single quotes (``'``).

Values can by one of the following types:

**Scalar Types**

Gyro has the following scalar types: string, numbers, and booleans.

String literals are defined as is zero or more characters enclosed within single quotes (``'my value'``).

String expressions are defined as zero or more characters enclosed within double quotes. String expressions differ from string
literals in that reference expressions will be interpolated prior to using the value (``"my value with $(key)"``).

Numbers can be integers or floats (``10``, ``10.5``, ``-10``).

Booleans are defined as ``true`` or ``false``.

**Compound Types**

Gyro has two compound types: maps, and lists.

Maps are zero or more comma-separated key/value pairs inside curly brackets (``{ key: 'value' }``).

Lists are zero or more comma-separated values inside square brackets (``['item1', 'item2']``).