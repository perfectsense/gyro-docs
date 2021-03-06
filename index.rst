.. title:: Gyro

.. cssclass:: gyro-hello
.. figure:: images/gyro-hello.png
    :width: 400px
    :align: right

    Gyro makes infrastructure-as-code possible

    `Download <guides/getting-started/installing.html#installing-gyro>`_

    `Github <https://github.com/perfectsense/gyro>`_

    `Learn More <https://getgyro.io/introducing-gyro>`_

Gyro
====

Gyro is an open source command-line tool for creating, updating, and maintaining cloud infrastructure. Gyro makes
infrastructure-as-code possible. Gyro is licensed under the `Apache 2.0 license <https://github.com/perfectsense/gyro/blob/master/LICENSE>`_.

Using Gyro allows you to model your infrastructure using the Gyro language and then create, update, and
maintain that infrastructure using the ``gyro`` command-line tool.

The Gyro language is designed specifically for defining cloud infrastructure. It was built with
readability and organizational flexbility in mind. The language provides the ability to concisely
define cloud infrastructure resources along with language constructs such a ``@for`` loops, ``@if``
conditionals, and ``@virtual`` definitions for packaging resources into reusable components.

Why Use Gyro?
+++++++++++++

Gyro is ideal for anyone looking to automate managing infrastructure in a cloud provider such as AWS, or Azure. Here
are several areas Gyro can help:

**Cloud Operations Teams**

Gyro can help teams develop processes for infrastructure changes. Traditionally cloud infrastructure changes
were accomplished using cloud vendor web interfaces which make it difficult verify and track changes. Using
Gyro to define infrastructure-as-code, teams can manage infrastructure changes using more formal processes
of review. Infrastructure changes can be reviewed to ensure only the requested changes are being made. Changes can
be tracked using any version control sytem.

**Self Service**

Gyro can help organizations implement self service infrastructure. Traditionally cloud infrastructure creation has to
go through a central operations team. As a company grows the ability for an operations team keep pace with these
requests can be difficult or require growing the operations team. Using Gyro common infrastructure can be defined and
shared across an organization allow teams outside the operations team to build and maintain their own infrastructure.

.. toctree::
   :maxdepth: 1
   :caption: Basics
   :name: basics

   guides/getting-started/installing
   guides/getting-started/index
   guides/contribute/index
   guides/language/index

.. toctree::
   :caption: Cloud Providers
   :maxdepth: 1
   :name: providers

   providers/aws/index
   providers/azure/index
   providers/google/index
   providers/pingdom/index

.. toctree::
   :maxdepth: 1
   :caption: Advanced
   :name: advanced

   guides/virtual-resources/index
   guides/workflows/index
   guides/state/index

.. toctree::
   :maxdepth: 1
   :caption: Extending Gyro
   :name: extending

   extending/directive/index
   extending/provider/index
   extending/commands/index
   extending/resolver/index
