Defining a Workflow
-------------------

Workflows are defined using the ``@workflow::define`` directive. This directive takes two arguments,
the resource type that will trigger this workflow on replace, and the name of the workflow.

For example:

.. code::

    @workflow::define aws::instance replace-instance

    @end

This workflow will execute any time a change to an aws::instance would trigger a replacement of the instance
due to a change that cannot be updated in-place.

The only valid configuration inside a workflow is a ``stage`` definition. Variables cannot be defined within
a workflow.
