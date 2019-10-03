Workflows
=========

Workflows allow you to have multi-staged deployments of cloud resources. A workflow is made up of
one or more stages. Each stage is made up of actions to create, update, replace, or delete cloud
resources. If you have more than one stage you can connect them using a transition. A transition
allows a workflow to prompt the user on what action to take next.

**Why Workflows?**

Workflows allow you to have more control over how cloud resources are replaced. Typically when you make a
change to a cloud resource that requires it to be replaced your only options are to delete the resource, then
create a new one, or create a new one and delete the old one. This model of deployment runs the risk of
causing outages. With workflows you get more fine grained control over how cloud resources are replaced.

.. toctree::
    :maxdepth: 1

    define
    stage
    reference
