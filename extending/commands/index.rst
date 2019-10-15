Adding a Command
================

Gyro is a command-line cloud automation tool. Gyro exposes several commands (i.e. ``gyro up``) to allow the user to interact with Gyro. New commands can be added to extend the functionality of Gyro. For example, the `gyro-ssh-plugin <https://github.com/perfectsense/gyro-ssh-plugin>`_ adds the ``ssh`` command for logging into hosts defined in your configuration.

The following commands are provided out of the box:

==================   ============
Directive            Function
==================   ============
``up``		 	     Creates, update or deletes cloud infrastructure as per configs.
``init``  	 		 Initializes an empty gyro project. 
``plugin``		 	 Adds or removes plugins.
==================   ============

You can also use 'gyro help <command>' to learn more on how to use a specific command.

.. toctree::
    :maxdepth: 1

    implementation
