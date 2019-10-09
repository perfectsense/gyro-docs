Implementing a Command
----------------------

To create your own command, you have a couple of choices. If you are creating a command targeting configs then subclass `gyro.core.command.AbstractConfigCommand <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/command/AbstractConfigCommand.java>`_ and implement the method **doExecute**. If on the other hand it is a plug-in based command then subclass `gyro.core.command.PluginCommand <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/command/PluginCommand.java>`_ and implement the method **execute**. For a generic command subclass `gyro.core.command.AbstractCommand <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/command/AbstractCommand.java>`_ and implement the method **doExecute**.

Annotated this class with the ``@command(name=string, description=string)`` annotation to give this command a name and a description. The name provided by this
annotation is the name that will be exposed to the Gyro language, (i.e. ``gyro <command-name>``). 

Example
+++++++

The following example shows the implementation of a simple command. 
