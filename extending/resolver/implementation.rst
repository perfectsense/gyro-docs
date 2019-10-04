Implementing a Resolver
-----------------------

A resolver needs to extend ``ReferenceResolver`` part of **gyro.core.reference** and there by implement the method **resolve**.

The class should also be annotated with the ``@Type(string)`` annotation. The name provided by this annotation is the name you use when using this resolver. This lets Gyro lookup the resolver implementation. 

The following example shows the implementation of a simple resolver called the ``string-concat`` that concatenates two or more stings.

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