Implementing a Command
----------------------

To create your own command subclass `AbstractConfigCommand
<https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/command/AbstractConfigCommand.java>`_
and implement the ``doExecute(RootScope current, RootScope pending, State state)`` method.

The ``doExecute`` method is passed the current and pending `RootScope <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/RootScope.java>`_
objects. ``RootScope`` is Gyro's internal representation of your configuration. The current state of
your configuration (i.e what exists in your cloud provider) is passed in as ``current`` and your
configuration as defined by your local Gyro configuration files is passed in as ``pending``. The
`State <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/State.java>`_ object is used
to save the state of your configuration (i.e. saves current configuration to ``.gyro/state/**``).

Gyro uses the `Airline <https://github.com/airlift/airline>`_ framework for defining commands and
options. Use the ``@command`` annotation to provide your commands name and description. Your command
will be available as ``gyro <name>``.

Example
+++++++

The following example shows the implementation of a simple command ``search`` which searches for a
resource in your configuration files and if found shows its location details (File, line and
column).

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