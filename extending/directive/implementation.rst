Implementing a Directive
========================

To create your own a directive subclass `gyro.core.directive.DirectiveProcessor <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java>`_ and implement the method **process**.

Annotate this class with the ``@Type(string)`` annotation to give this directive a name. The name provided by this
annotation is the name that will be exposed to the Gyro language, (i.e. ``@<typename>:``). Note that if the Java
package that contains your directive provides a ``package-info.java`` file annotated with ``@Namespace``, your directive
will be available as ``@<namespace>::<type>:``.

Your directive's ``process`` method will be called whenever Gyro encounters a reference with the name of your directive
in it. Your directive will be passed in a `Scope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_ object, this gives you access to Gyro's internal scope (map of
values), and a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_ object, this gives you direct access to Gyro's AST for you to manipulate it as you please.

The ``DirectiveProcessor<s extend scope>`` acceps a ``scope`` as a genric. This allows differrent behavior based on differnt scopes passed and restrictons on where a directive can work.
Following are some of the out of the box scope flavors and corresponding restrictions:

=============================================================================================================================  ============
Scope 		   																													Usage
=============================================================================================================================  ============
`DiffableScope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/DiffableScope.java>`_		Directive can ony be used inside a ``Resource`` definition.
`RootScope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/RootScope.java>`_				Directive can only be used inside ``.gyro/init.gyro``.
`FileScope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/FileScope.java>`_				Directive can be used will all ``.gyro`` files except ``.gyro/init.gyro`` and cannot be used inside a ``Resource`` definition.
=============================================================================================================================  ============ 

You are free to extend `Scope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_ and create your own sub type to use in a custom directive, whose behavior and restrictions would be based on how you implement your version of the scope.

Example
+++++++

.. code-block:: java
	
	@Type("production")
	public class ProductionProtectionDirectiveProcessor extends DirectiveProcessor<FileScope> {

	    @Override
	    public void process(FileScope fileScope, DirectiveNode directiveNode) throws Exception {
	        GyroUI ui = GyroCore.popUi();
	        if (!(ui instanceof ProductionGyroUi)) {
	            ui = new ProductionGyroUi(ui);
	        }

	        GyroCore.pushUi(ui);
	    }
	}

	public class ProductionGyroUi implements GyroUI {

		.. code for appending **[PRODUCTION]** to all outputs
	}

The following is how this can be used:

.. code-block:: java
	
	@production: true

	aws::instance frontend
		name: webserver
		.
		.
	end

In your gyro configuration file which reflects production assets if ``@production: true`` is used on top, then all the display outputs will be appended with **[PRODUCTION]** text to notify that changes will be done to the production environment.
