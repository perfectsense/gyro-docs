Directives
----------

Directives are Gyro language extensions that add functionality to the base language. Directives begin with
the ``@`` symbol, for example, the line ``@plugin: 'gyro:gyro-aws-provider:0.15-SNAPSHOT'`` in the "Test Your Installation"
section of this document is actually a directive that loads an external plugin.

Simple directives, such as ``@plugin``, are defined in the format ``@<directive>: <arguments>``. All
single line directives take at least one argument and must be on a single line, for example:

.. code::

    @plugin: 'gyro:gyro-aws-provider:0.15-SNAPSHOT'

Advanced directives, such as ``@credentials`` take both an argument and one or more attributes. All advanced
directives end with ``@end``, for example:

.. code::

    @credentials 'enterprise::aws-credentials'
        enterprise-url: "https://enterprise.example.com"
        project: $(project)
        account: $(account)
        region: "us-east-2"
    @end

Settings
--------

Settings are how a directive accepts attributes along with arguments. Attributes could be simple as name value pairs or complex as nested maps.
Settings allow these values to be stored in the scope and used at a later time by this or other directives.

To implement your own settings class, subclass `gyro.core.scope.setting <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Settings.java>`_ with needed variables/attributes. You get an instance of this class by calling ``scope.getSettings(<Custom-Setting-Class>.class)`` and there by get access to all the variables/attributes that your ``<Custom-Setting-Class>`` defines.

For example:
