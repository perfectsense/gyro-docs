Control Structures
++++++++++++++++++

Gyro provides control structures via directives.

.. _if-expression:

@if expression
--------------

The ``@if`` directive allows you to branch your configuration depending on conditions. The condition
is provided as a boolean expression to ``@if``. An ``@if`` directive alway ends with ``@end``.

Multiple conditions can be handled by using the ``-elseif`` option. Use ``-else`` option to
define logic to execute if no other conditions are met.

**Syntax**

.. code::

    @if <expression>
        <configuration>
    -elseif <expression>
        <configuration>
    -else
        <configuration>
    @end

**Example**

.. code::

    @if $(subnet).availability-zone = 'us-east-1a'
        aws::instance us-east-1a-instance
            image-id: "ami-0cd3dfa4e37921605"
            instance-type: "t2.nano"
            subnet: $subnet
        end
    -elseif $(subnet).availability-zone = 'us-east-1b'
        aws::instance us-east-1b-instance
            image-id: "ami-0dd3aea9e319ab101"
            instance-type: "t2.micro"
            subnet: $subnet
        end
    @end

.. _for-loop:

@for loop
---------

The ``@for`` directive allows you to loop over a set of values while repeating a block of configuration.

If multiple variables are provided to ``@for`` it will fill each variable in from the corresponding values
provided by the ``in`` option. For example:

.. code::

    @for zone, cidr -in ['us-east-1a', '10.0.0.0/24', 'us-east-1b', '10.0.1.0/24']
        aws::subnet "public-$zone"
            cidr-block: $cidr
        end
    @end

This will produce the following final configuration:

.. code::

    aws::subnet "public-us-east-1a"
        cidr-block: '10.0.0.0/24'
    end

    aws::subnet "public-us-east-1b"
        cidr-block: '10.0.1.0/24'
    end

**Syntax**

.. code::

    @for <variable> [, <variable, ...] -in <list>
        <configuration>
    @end

**Example**

.. code::

    @for subnet -in $(aws::subnet public-*)
        aws::instance us-east-1b-instance
            image-id: "ami-0dd3aea9e319ab101"
            instance-type: "t2.micro"
            subnet: $subnet
        end
    @end