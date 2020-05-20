Creating Infrastructure
-----------------------

This chapter will walk you through configuring your first Gyro project as well as creating
and managing your first resource.

Setting up a Gyro Project
+++++++++++++++++++++++++

Before you can start managing cloud resources with Gyro you need to initialize a Gyro project. To
initialize your Gyro we'll use the ``gyro init`` command. This command takes a list of plugins to
load and creates a the ``.gyro`` directory and the ``.gyro/init.gyro`` configuration file.

Since this tutorial will walk you through creating and managing a resource in AWS, we'll 
initialize our project with the AWS provider plugin:

.. code:: shell

    $ gyro init gyro:gyro-aws-provider:0.99.1
    + Creating a new .gyro directory
    + Writing to the .gyro/init.gyro file

Setting up Provider Authentication
++++++++++++++++++++++++++++++++++

Before we can create any resources we'll need to configure Gyro so it knows how to authenticate
to AWS to make API calls. Each cloud provider has a different mechanism for authentication. The AWS
provider uses the same authentication mechanism that the AWS CLI uses, which is to provide
access keys in the ``$HOME/.aws/credentials`` file.

Ensure you have credentials for AWS defined in ``$HOME/.aws/credentials``. If you have the AWS
CLI installed you can run the following to configure your credentials:

.. code:: shell

    $ aws configure --profile gyro
    AWS Access Key ID [None]: AEVOO9PAHC4THIE6UB3G
    AWS Secret Access Key [None]: UvkNum4VB025EHVtBKQxzYcuOLSYNAF6e300yfVf
    Default region name [us-east-1]:
    Default output format [None]:
    $

Verify the credentials:

.. code:: shell

    $ grep -A3 gyro $HOME/.aws/credentials
    [gyro]
    aws_access_key_id = AEVOO9PAHC4THIE6UB3G
    aws_secret_access_key = UvkNum4VB025EHVtBKQxzYcuOLSYNAF6e300yfVf

Now that we have the credentials file configured we need to tell Gyro which credentials we want to use. For this
we use an ``@credentials`` directive in ``.gyro/init.gyro``. Add the following to ``.gyro/init.gyro``:

.. code:: shell

    @credentials aws::credentials
        profile-name: "gyro"
        region: "us-east-1"
    @end

Configure a Resource
++++++++++++++++++++

Resources define cloud infrastructure configuration. For this example we'll configure a single ``aws::instance``
resource.

Create a file named ``instance.gyro`` with the following resource configuration in it:

.. code::

    ami-id: $(external-query aws::ami {
        name: 'ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-20190628',
        architecture: 'x86_64',
        root-device-type: 'ebs',
        virtualization-type: 'hvm',
        owner-id: '099720109477',
        state: 'available'
    }).0.id

    aws::instance webserver
        ami: $(ami-id)
        instance-type: "t3.nano"
    end

This configuration demonstrates how to query for a resource, and how to create a new resource.

Using the ``$(external-query ...)`` resolver we can search for resources that are not managed by Gyro. In this case
we're looking up the ``ami-id`` for an Ubuntu Linux machine image. Each resource has a different set of parameters
that it can filter by. The advantage to looking up the ``ami-id`` this way is that we'll get the appropriate
``ami-id`` no matter what region we have configured in our credentials above.

We use the ``ami-id`` to create a single ``aws::instance``. The only required setting is the ``instance-type`` which
we'll set to ``t3.nano``.

Creating an Instance
++++++++++++++++++++

.. note:: The following instructions  will create a ``t3.nano`` instance which will incur charges on your
          AWS account.

Now that we have our configuration we can tell Gyro to apply it by using the ``gyro up`` command.

.. code::

    $ gyro up
    ↓ Loading plugin: gyro:gyro-aws-provider:0.99.1

    Looking for changes...

    + Create aws::instance webserver

    Are you sure you want to change resources? (y/N) y

    + Creating aws::instance webserver OK

The ``gyro up`` command will compare local state (of which there is none right none) with the configuration
we just added and present you with the actions necessary to effect the changes in the configuration. By default
Gyro only shows the action (create, update, replace, delete) that will be taken for any resources that have
changed. For a more detailed view use the ``--verbose`` option of ``gyro up``. This will show you exactly which
fields have changed.

.. code::

    $ gyro up --verbose
    ↓ Loading plugin: gyro:gyro-aws-provider:0.99.1

    Looking for changes...

    + Create aws::instance webserver
    · ami: aws::ami id=ami-0cfee17793b08a293
    · instance-type: 't3.nano'

    Are you sure you want to change resources? (y/N) y

    + Creating aws::instance webserver OK

We now have ``t3.nano`` instance running in our AWS account. At this point if we run ``gyro up``
again it shouldn't find any changes.

.. code::

    $ gyro up --verbose
    ↓ Loading plugin: gyro:gyro-aws-provider:0.99.1
    ⟳ Refreshed resources: 1

    Looking for changes...

    No changes.

In the next section will show you how Gyro makes changes to infrastructure easy and safe.
