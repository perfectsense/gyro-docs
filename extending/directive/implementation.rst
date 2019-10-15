Implementing a Directive
========================

To create your own directive subclass `gyro.core.directive.DirectiveProcessor <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java>`_ and implement the method **process**.

Annotate this class with the ``@Type(string)`` annotation to give this directive a name. The name provided by this
annotation is the name that will be exposed to the Gyro language, (i.e. ``@<typename>:``). Note that if the Java
package that contains your directive provides a ``package-info.java`` file annotated with ``@Namespace``, your directive
will be available as ``@<namespace>::<type>:``.

Your directive's ``process`` method will be called whenever Gyro encounters a reference with the name of your directive
in it. Your directive will be passed in a `Scope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_ object, this gives you access to Gyro's internal scope (map of
values), and a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_ object, this gives you direct access to Gyro's AST for you to manipulate it as you please.

The ``DirectiveProcessor<s extend scope>`` acceps a ``scope`` as a genric. This allows differrent behavior based on differnt scopes passed and restrictons on where a directive can work.
Following are some of the out of the box scope flavors and corresponding restrictions:

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

You are free to extend `Scope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_ and create your own sub type to use in a custom directive, whose behavior and restrictions would be based on how you implement your version of the scope.

Optionaly if you need arguments that are more complex in nature or want them to be reusable by other extensions (i.e persist beyond just when this directive is called) you could define your own `settings <../../guides/language/directives.html#settings>`_.

Arguments
+++++++++

`DirectiveProcessor <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java>`_ provides a number of helper methods to process arguments and options. We discuss some of them here.

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
