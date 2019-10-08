Adding a Directive
==================

Directives are how Gyro injects features/modifications to the language itself like (``@plugin`` or ``@wait``). A directive hooks on to Gyro's AST and is able to set data directly into the language scope. Gyro provides a number of out of the box directives

==================   ============
Directive            Function
==================   ============
``@print``		 	 Print something in the console.
``@repository``  	 Get access to external repositories. 
``@wait``		 	 Lets you wait between two Gyro actions conditionally.
``@extends``	 	 Ability to copy resource configurations with optional exception fields.
``@plugin``		 	 Attach a Gyro plugin to the language. Each cloud provider (``aws`` or ``azure`` or ``pingdom``) is a plugin.
==================   ============

.. toctree::
    :maxdepth: 1

    implementation
    use
