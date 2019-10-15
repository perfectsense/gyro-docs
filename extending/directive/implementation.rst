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

Arguments and Attributes
++++++++++++++++++++++++

Directives can have both arguments and attributes depending on how it's used in configuration. For example, if a
directive only takes arguments it will have the following syntax:

.. code-block:: gyro

    @print: "hello world"

If a directive takes arguments and attributes it will have the following syntax:

.. code-block:: gyro

    @file-backend 'aws::s3', 'builds'
        bucket: 'builds-bucket'
    @end

Processing Arguments
++++++++++++++++++++

The following methods are used to process directive arguments:

.. rst-class:: method
.. list-table::
    :widths: 40 60
    :header-rows: 1

    * - Method
      - Description

    * - `List<Node> validateArguments(DirectiveNode node, int minimum, int maximum) <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java#L71>`_
      - This method accepts a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_
        , min and max value. This validates if the number of arguments being passed is between
        the min and max range set, throws a error otherwise.

    * - `List<Node> validateOptionArguments(DirectiveNode node, String name, int minimum, int maximum) <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java#L83>`_
      - This method accepts a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_
        , the name of the option, and the minimum and maximum number of arguments. Similar to ``validateArguments`` this validates the
        correct number of arguments for the option specified by the name.

    * - `List<T> getArguments(Scope scope, DirectiveNode node, Class<T> valueClass) <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java#L120>`_
      - This method accepts a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_
        , a `Scope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_
        , and a class that specifies the expected type for all arguments. This method returns all the argument values passed in
        the the directive as a list.

    * - `T getArgument(Scope scope, DirectiveNode node, Class<T> valueClass, int index) <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java#L116>`_
      - This method accepts a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_
        , a `Scope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_
        , a class that specifies the expected type for the value at position specified by index. Similar to ``getArguments``
        but this method gets the argument at the position specified by index.

    * - `T getOptionArgument(Scope scope, DirectiveNode node, String name, Class<T> valueClass, int index) <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java#L126>`_
      - This method accepts a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_
        , a `Scope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_
        , the name of the option, a class that specifies the expected type for the value at position specified by index.
        Similar to ``getArgument`` but this method gets the option's argument for position specified by index.

Processing Attributes
+++++++++++++++++++++

To process directive attributes use the following method to get a ``Scope`` object for the directive. This ``Scope``
can then be used to read attributes for the directive, as follows:

.. code-block:: java

    Scope bodyScope = evaluateBody(scope, node);
    String bucket = (String) bodyScope.get("bucket");

.. rst-class:: method
.. list-table::
    :widths: 40 60
    :header-rows: 1

    * - Method
      - Description

    * - `Scope evaluateBody(Scope scope, DirectiveNode node) <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/directive/DirectiveProcessor.java#L131>`_
      - This method accepts a `DirectiveNode <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/lang/ast/block/DirectiveNode.java>`_ object and a `Scope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Scope.java>`_ object.
