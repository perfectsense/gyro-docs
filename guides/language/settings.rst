Settings
--------

Settings are how a directive accepts attributes along with arguments. Attributes could be simple as name value pairs or complex as nested maps.
Settings allow these values to be stored in the scope and used at a later time by this or other directives.

To implement your own settings class, subclass `gyro.core.scope.setting <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/scope/Settings.java>`_ with needed variables/attributes. You get an instance of this class by calling ``scope.getSettings(<Custom-Setting-Class>.class)`` and there by get access to all the variables/attributes that your ``<Custom-Setting-Class>`` defines.

For example:
