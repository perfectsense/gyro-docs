Destroying Infrastructure
-------------------------

After creating temporary resources for testing or performing other activities, it may be necessary to destroy infrastructure.
Gyro will never destroy infrastructure without prompting.

Delete actions completely remove resources from the cloud.

In order to remove a resource from the existing infrastructure, remove the configs from the resource file.

.. code::

   aws::route route-example
    route-table: $(aws::route-table route-table-example)
    destination-cidr-block: "0.0.0.0/0"
    gateway: $(aws::internet-gateway ig-example)
  end


Removing the route resource will delete the internet-bound traffic route from the route table.

.. code:: shell

  $ /usr/local/bin/gyro up vpc.gyro

   ↓ Loading plugin: gyro:gyro-aws-provider:0.15-SNAPSHOT
   ↓ Loading plugin: gyro:gyro-brightspot-plugin:0.15-SNAPSHOT
   ⟳ Refreshed resources: 5

   Looking for changes...

   - Delete aws::route route-example

   Are you sure you want to change resources? (y/N) y

   - Deleting aws::route route-example OK

Gyro confirms the deletion. Typing y will execute the delete request. All resource deletions work the same way in gyro: remove the resource section from the config file.

In order to remove the entire virtual private cloud network instead of associated resources, remove the entire VPC config section from vpc.gyro file.
Gyro will start deleting the parent resource along with the associated resources.

Example given below : remove this entire section from the vpc.gyro file :

.. code::

   aws::vpc vpc-example
       cidr-block: "10.0.0.0/16"

       tags: {
           Name: "vpc-example-1"
       }
   end

   aws::subnet subnet-public-us-east-2a
       vpc: $(aws::vpc vpc-example)
       cidr-block: "10.0.0.0/26"
       availability-zone: "us-east-2a"

       tags: {
           Name: "subnet-public-us-east-2a"
       }
   end

   aws::internet-gateway ig-example
       vpc: $(aws::vpc vpc-example)

       tags: {
           Name: "ig-example"
       }
   end

   aws::route-table route-table-example
       vpc: $(aws::vpc vpc-example)
       subnets: [$(aws::subnet subnet-public-us-east-2a)]

       tags: {
           Name: "route-table-example"
       }
   end

The resource vpc and associated resources will get deleted after ``y`` is given at the prompt.

.. code:: shell

   $/usr/local/bin/gyro up vpc.gyro

    ↓ Loading plugin: gyro:gyro-aws-provider:0.15-SNAPSHOT
    ↓ Loading plugin: gyro:gyro-brightspot-plugin:0.15-SNAPSHOT

    ⟳ Refreshed resources: 4

    Looking for changes...

    - Delete aws::vpc vpc-example (vpc-0db28818a6cb91795)
    - Delete aws::subnet subnet-public-us-east-2a (subnet-00ef07cf7a507d64c)
    - Delete aws::internet-gateway ig-example (igw-04463fa091c36aff6)
    - Delete aws::route-table route-table-example (rtb-09c6c85e550100385)

    Are you sure you want to change resources? (y/N) y

    - Deleting aws::route-table route-table-example (rtb-09c6c85e550100385) OK
    - Deleting aws::internet-gateway ig-example (igw-04463fa091c36aff6) OK
    - Deleting aws::subnet subnet-public-us-east-2a (subnet-00ef07cf7a507d64c) OK
    - Deleting aws::vpc vpc-example (vpc-0db28818a6cb91795) OK
