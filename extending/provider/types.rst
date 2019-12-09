Types of Resources
==================

There are three types of resources in Gyro provider implementations:

Resource
    This is a top-level resource such as ``aws::instance``. Resources can be defined directly within a file. They
    cannot be used inside other resources. This resource extends
    `Resource <https://github.com/perfectsense/gyro/blob/master/core/src/main/java/gyro/core/resource/Resource.java>`_.

Subresource
    This is a resource that must be defined as part of a parent resource but **can** be updated independently of the
    parent resource when changes are detected. A example of a subresource is an ``aws::security-group``
    `ingress <https://github.com/perfectsense/gyro-aws-provider/blob/master/src/main/java/gyro/aws/ec2/SecurityGroupRuleResource.java>`_ rule.

Complex type
    This is a resource that must be defined as part of a parent resource but **cannot** be updated independently of
    the parent resource.
