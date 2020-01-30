Defining a Stage
----------------

Each stage of a workflow defines a set of actions to take on the configuration, and any transitions to
other stages. There are four directives that can be used define actions in a stage:

Directives
++++++++++

@workflow::create
    This directive defines a new cloud resource to be created when this stage executes. You can use the
    :ref:`extends` directive to quickly duplicate a resource.

    This directive takes the cloud resource type and name as arguments. Attributes to this directive are
    set on the new resource.

    .. code::

        @workflow::create aws::instance webserver-new
            @extends: $(aws::instance webserver) -exclude private-ip-address
        @end

@workflow::update
    This directive allows you to change the values of an existing resource. For instance, you may update
    the instances in a load balancer.

    This directive takes a reference to an existing resource to update. Attributes to this directive are
    updated on the referenced resource.

    .. code::

        @workflow::update $(aws::load-balancer frontend)
            instances: $(aws::instance frontend-*)
        @end

@workflow::replace
    This directive allows you to replace an existing resource in the configuration with another resource. Typically
    this new resource is one that was created in a prior stage using the ``@workflow::create`` directive.

    This directive takes two arguments: a reference to the resource to be replaced, and a reference to the resource
    to replace it with.

    .. code::

        @workflow::replace: $(aws::instance webserver) $(aws::instance webserver-new)

@workflow::delete
    This directive allows you to delete an existing resource.

    This directive takes one argument: a reference to the resource to be deleted.

    .. code::

        @workflow::delete: $(aws::instance webserver-new)

@wait
    This directive waits until an expression is true before continuing. Use this directive to wait for
    cloud resources to be in a desired state before continuing.

    This directive takes a single argument, the expression to evaluate. Optionally you can provide ``-unit``,
    ``-at-most``, and ``-check-every``.

    -unit
        What time unit the ``-at-most`` and ``-check-every`` are in. Valid values are ``milliseconds``,
        ``seconds``, ``minutes``, or ``hours``. The default is ``seconds``.

    -at-most
        The maximum amount of time to wait for the expression to be true. The default is 10 seconds.

    -check-every
        The amount of to wait between checks. The default is 1 second.

Transition
++++++++++

A transition allows you to get user confirmation before moving on to the next stage. It also allows
the user to pick which stage to transition to. This can be used to implement a rollback by going back
to a previous stage and re-running it.

Transitions take a single argument, the name of the transition. This is the name the user will type to select
the transition. Each transition can have two attributes, ``to`` and ``description``:

to
    The stage to transition to.

description
    A description of what selecting this transition will do. This description will be displayed alongside the
    transition name when the users is prompted to pick a transition.

**Example**

.. code::

    stage verify
        ...

        transition push
            to: push
            description: "Push new instances into the production load balancer."
        end

        transition reset
            to: reset
            description: "Terminate new instances and end this workflow."
    end

    stage push
        ...
    end

    stage reset
        ...
    end

Given the example above the user will receive the following prompt after the verify stage is executed.

.. code::

    push) Push new instances into the production load balancer.
    reset) Terminate new instances and end this workflow.
    Next stage?

At this point they can type ``push`` or ``reset`` followed by ``<enter>`` to transition to the next stage.

Confirmation
++++++++++++

By default each stage will execute any changes automatically. This behavior can be changed to show the user the
diff output for the changes, allowing them to confirm the changes before proceeding.

To enable confirmation add the ``confirm-diff: true`` attribute to your stage.

.. code::

    stage verify
        confirm-diff: true

        @workflow::create aws::load-balancer frontend-verify
            @extends: $(aws::load-balancer frontend) -exclude instances

            name: "$(project)-web-$(serial)-v"
        @end

        @workflow::create aws::launch-configuration frontend-verify
            @extends: $PENDING
        @end

        @workflow::create aws::autoscaling-group frontend-verify
            @extends: $(aws::autoscaling-group frontend)

            name: $(aws::launch-configuration frontend-verify).name
            launch-configuration: $(aws::launch-configuration frontend-verify)
            classic-load-balancers: [
                $(aws::load-balancer frontend-verify)
            ]

            @wait: $(aws::load-balancer frontend-verify).instance-health.InService = $desired-capacity -check-every 60 -at-most 600
        @end

        transition push
            to: push
            description: "Push new instances into the production load balancer."
        end

        transition reset
            to: reset
            description: "Terminate new instances and end this workflow."
    end

This would result in the following prompt to the user before executing the verify stage.

.. code::

    ~ Executing frontend-deploy workflow
    1 Executing verify stage
        + Create aws::load-balancer frontend-verify (gyro-web-1-v)
            + Create attribute load balancer attribute
                + Create access-log access log
                + Create connection-draining connection draining
                + Create connection-settings connection settings
                + Create cross-zone-load-balancing cross zone load balancing
            + Create listener 443
            + Create listener 80
        + Create aws::launch-configuration frontend-verify (gyro frontend prod v1 ami-011b8228283d287be builds/deploy/4.2 184 ae02f82819e15345104272351b42c761)
        + Create aws::autoscaling-group frontend-verify (gyro frontend prod v1 ami-011b83l8283d287be builds/deploy/4.2 184 ae02f82819e15345104272351b42c761)
            + Create scaling-policy Scale Up SimpleScaling
            + Create scaling-policy Scale Down SimpleScaling

        Continue with verify stage? (Y/n)


