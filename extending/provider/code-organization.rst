Code Organization
-----------------

Provider implementations are free to organize code however they see fit, however, the following are
best practices that we've found to work well when organizing provider implementations.

Each provider should be placed in a unique Java package named for the provider. For example, the AWS provider
should be placed in the ``gyro.provider.aws`` package.

Additional packages should be used to logically separate provider services. For example, AWS CloudFront service
should be placed in the ``gyro.provider.aws.cloudfront`` package, while AWS Autoscaling service should be placed
in the ``gyro.provider.aws.autoscaling`` package.



Example:

.. code-block:: shell

    build.gradle
    src/main/java
    src/main/java/gyro/sample/compute/NetworkResource.java
    src/main/java/gyro/sample/compute/ComputeResource.java
    src/main/java/gyro/sample/compute/package-info.java
    src/main/java/gyro/sample/SampleCredentials.java
    src/main/java/gyro/sample/SampleResource.java
    src/main/java/gyro/sample/SampleResourceFinder.java
    src/main/java/gyro/sample/SampleResourceFinder.java
    src/main/java/gyro/sample/SampleProvider.java
    src/main/java/package-info.java