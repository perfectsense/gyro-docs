Implementing a Directive
========================

To create your own directive subclass `DirectiveProcessor <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java>`_ and implement the method **process**.

Name your directive by annotating your class with the ``@Type(string)``. The name provided by this
annotation will expose your directive to the Gyro language as ``@<typename>``. Directives can be namespaced, similar
to how resources are namespaced by provider, by adding ``package-info.java`` to the package with your
directive. Annotate the ``package`` declaration in ``package-info.java`` with the ``@Namespace(<name>)`` annotation. With
a namespace defined your directive will be available as ``@<namespace>::<type>``.

The ``process`` method is called when Gyro encounters your directive in a Gyro configuration file.
It will be passed in a `Scope
<https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_
object that gives you access to Gyro's internal scope (map of values), and a `DirectiveNode
<https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_
object that gives you access to the directive node in Gyro's AST.

Subclasses of ``DirectiveProcessor`` must supply a scope class. The scope class that is chosen has the effect
of limiting where the directive can be used. The following are the ``Scope`` classes and their limitions:

.. list-table::
    :widths: 10 90
    :header-rows: 1

    * - Scope
      - Usage

    * - `DiffableScope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/DiffableScope.java>`_
      - Directive can ony be used inside a ``Resource`` definition.

    * - `RootScope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/RootScope.java>`_
      - Directive can only be used inside ``.gyro/init.gyro``.

    * - `FileScope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/FileScope.java>`_
      - Directive can be used will all ``.gyro`` files except ``.gyro/init.gyro`` and cannot be used inside a ``Resource`` definition.

Handling Arguments
++++++++++++++++++

`DirectiveProcessor
- `validateArguments <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java#L71>`_
	This method accepts a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_ object, min and max value. This validates if the number of arguments being passed is between the min and max range set, throws a error other wise.

- `validateOptionArguments <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java#L83>`_
	This method accepts a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_ object, option name, min and max value. Similar to *validateArguments* this validates the right amount of arguments for the option specified by the name.

- `getArguments <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java#L120>`_
	This method accepts a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_ object, a `Scope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_ object, and a <classType> (return type). This method returns all the argument values passed in the the directive as a list of the the type sepcified.

- `getArgument <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java#L116>`_
	This method accepts a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_ object, a `Scope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_ object, a <classType> (return type), and an index. Similar to *getArguemnts* this method gets the argument value of the passed argument based on index provided and returned in the type specified.

- `getOptionArgument <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java#L126>`_
	This method accepts a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_ object, a `Scope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_ object, option name, a <classType> (return type), and an index. Similar to *getArgument* this method gets the arguments for the option specified by the name and based on the index provided and returned in the type specified.

- `evaluateBody <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java#L131>`_
	This method accepts a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_ object and a `Scope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_ object.

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
