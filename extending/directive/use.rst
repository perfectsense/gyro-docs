Using a Directive
-----------------

A directive uses the ``@<directive-name>: <arg1> <arg2>`` notation. The Directive can take as many arguments as defined by the implementation.

Directives can also be multiline which accepts a map of directive settings along with the arguments.

.. code-block:: shell

	@<directive-name> <arg1> <arg2>
		<directive-setting-param-1>: <value>
		<directive-setting-param-2>: <value>
	@end

For example:

.. code-block:: java

	@wait: $(aws::load-balancer production).instance-health.InService >= 5 -check-every 60 -at-most 600

This directive allows gyro to wait depending on the condition provided by the first argument (**$(aws::load-balancer production).instance-health.InService >= 5**) the second argument (**-check-every 60**) specifies the check interval and the third argument (**-at-most 600**) specifies the upper bound for the waiting time.