Credentials
-----------

Every provider must implement a subclass of the ``gyro.core.Credentials`` class. This class is responsible for
loading credential information necessary to use the cloud provider's API.

.. code:: java

    public abstract class Credentials {

        public void refresh() {
        }

    }

It is up to the implementor to determine the best method for storing credentials. Typically storing credentials
should follow the cloud provider's API convention. For example, the AWS provider can use environment variables or
the ``$HOME/.aws/credentials`` file to load credentials.

Example
+++++++

Below is an example implementation of credentials used by the AWS provider:

.. code:: java

    public class AwsCredentials extends Credentials {

        private String profileName;
        private String region;
        private AwsCredentialsProvider provider;

        public AwsCredentials() {
            this.provider = AwsCredentialsProviderChain.builder()
                .credentialsProviders(DefaultCredentialsProvider.create())
                .build();
        }

        public String getProfileName() {
            return profileName;
        }

        public void setProfileName(String profileName) {
            this.profileName = profileName;

            this.provider = AwsCredentialsProviderChain.builder()
                .credentialsProviders(
                    ProfileCredentialsProvider.create(profileName),
                    DefaultCredentialsProvider.create()
                )
                .build();
        }

        public String getRegion() {
            return region;
        }

        public void setRegion(String region) {
            this.region = region;
        }

        public AwsCredentialsProvider provider() {
            return provider;
        }

        @Override
        public void refresh() {
            provider().resolveCredentials();
        }

    }

Usage
+++++

Credentials are always defined in ``.gyro/init.gyro``. Given the AWS credentials implementation above the user
would provide the following in ``.gyro/init.gyro``:

.. code::

    @credentials 'aws::default'
        profile-name: 'my-project'
        region: 'us-east-1'
    @end


