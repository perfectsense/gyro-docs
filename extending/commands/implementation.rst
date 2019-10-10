Implementing a Command
----------------------

To create your own command, you have a couple of choices. If you are creating a command targeting configs then subclass `gyro.core.command.AbstractConfigCommand <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/command/AbstractConfigCommand.java>`_. This gives you access to the current existing configuration (state) as well the pending configuration (your current configuration). If on the other hand you want to load the configurations in a differnt way and also control file scoping, subclass the more generic `gyro.core.command.AbstractCommand <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/command/AbstractCommand.java>`_. For both the case implement the method **doExecute**.

We use the `Airline <https://github.com/airlift/airline>`_ framefork for defining command and options. The ``@command`` annotation lets you specify the **name** of the command and a **description** enabling you to see a what the command does when help is called. ``@Option`` and ``@Argument`` annotations are used to customize the commands to add options and arguments to them. Annotate the class with the ``@command(name=string, description=string)`` annotation to give this command a name and a description.  The ``@command`` annotation lets you specify the **name** of the command and a **description** enabling you to see a what the command does when help is called. The name provided by this annotation is the name that will be exposed to the Gyro language, (i.e. ``gyro <command-name>``). 

Example
+++++++

The following example shows the implementation of a simple command ``search`` which searches for a resource in your configuration files and if found shows its location details (File, line and column). 

.. code-block:: java

	@Command(name = "search", description = "Searches for a resources and if found displays the file and location.")
	public class SearchCommand extends AbstractConfigCommand {

	    @Option(name = "name", required = true)
	    private String name;

	    @Override
	    protected void doExecute(RootScope current, RootScope pending, State state) throws Exception {
	        List<Resource> resources;

	        if (name == null || !name.contains("::")) {
	            throw new GyroException("please provide a name (<provider>::<resource>) to search for.");
	        }

	        resources = pending.findResources().stream().filter(o -> o.toString().split(" ")[0].equals(name)).collect(Collectors.toList());

	        GyroUI ui = GyroCore.ui();

	        if (!resources.isEmpty()) {
	            ui.write(String.format("\nFound %s in the following places:\n", name));

	            for(Resource resource : resources) {
	                BlockNode block = DiffableInternals.getScope(resource).getBlock();
	                String name = ((ResourceNode) block).getName().toString();
	                ui.write(String.format("\n\tResource name: %s, File: %s, Line: %s, Col: %s", name, block.getFile(), block.getStartLine(), block.getStartColumn()));
	            }
	        } else {
	            ui.write(String.format("\n%s Not found.\n", name));
	        }
	    }
	}