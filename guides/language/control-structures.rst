Control Structures
++++++++++++++++++

Gyro provides control structures via directives.

@if
+++

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

@for
++++

.. code::

    @for subnet -in $(aws::subnet public-*)
        aws::instance us-east-1b-instance
            image-id: "ami-0dd3aea9e319ab101"
            instance-type: "t2.micro"
            subnet: $subnet
        end
    @end