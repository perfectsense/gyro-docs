Adding a Directive
==================

Directives allow the Gyro language to be extended. They allow access to manipulate the current
and pending Gyro configuration, execute code, or add settings to be used later.

Directives are processed as they are encountered during parsing. This allows directives to add,
remove, or modify resources prior to the diff engine running.

The following directives are provided out-of-the-box:

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
