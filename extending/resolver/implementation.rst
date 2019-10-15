Implementing a Resolver
-----------------------

To create your own a resolver subclass `ReferenceResolver
<https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/reference/ReferenceResolver.java>`_
and implement the method **resolve**.

Name your resolver using by annotating this class with the ``@Type(string)``. The name provided by
this annotation be exposed to the Gyro language ``$(<name>)``. Resolvers can be namespaced, similar
to how resources are namespaced by provider, by adding a ``package-info.java`` to the package with your
resolver. Annotate the ``package`` definition in ``package-info.java`` with the ``@Namespace(<name>)`` annotation. With
a namespace defined your resolver will be available as ``$(<namespace>::<type>)``.

Your resolver's ``resolve`` method will be called whenever Gyro encounters a reference with the name
of your resolver in it. Your resolver will be passed in a `Scope
<https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_
object, this gives you access to Gyro's internal scope (map of values), and a ``List<Object>`` of
arguments that have already been resolved.

Your resolver should return a value that can be used by the Gyro configuration language. Typically this means
returning a basic type (integer, string, list, or map) or a Resource.

Example
+++++++

The following example shows the implementation of a simple resolver called the ``string-concat``
that concatenates two or more stings.

.. code-block:: java

	@Type("string-concat")
	public class StringConcatResolver extends ReferenceResolver {

	    @Override
	    public Object resolve(Scope scope, List<Object> arguments) throws Exception {
	    	if (arguments.size() < 2) {
	    		throw GyroException("The 'String-concat' resolver needs atleast two arguments");
	    	}

	    	return String.join(" ", arguments);
    }
    }