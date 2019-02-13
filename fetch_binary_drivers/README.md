# Fetch Binary Drivers

This is a public binary version of our drivers and firmware for the Fetch Research Platforms.

https://fetchrobotics.com/robotics-platforms/

We have two Fetch Research Platforms. Commonly known as Fetch and Freight. Fetch is the one with the arm.
The drivers and firmware in this package are for both.

https://docs.fetchrobotics.com/

# Fetch Drivers

The catkin package inside of this folder is called `fetch_drivers`, not `fetch_binary_drivers`.
This is because we've previously been releasing packages which depend on `fetch_drivers`.
We're just changing how we distribute our drivers.

# About

This package should only be needed if you're using one of the Fetch Research Platforms.

Our goal is to better support our our Fetch Research Platform customers through an improved, more automated build and release process. This will get enable us to get updates out faster.

We discussed at [ROSCon 2018](https://roscon.ros.org/2018/) in a talk "Hermetic Robot Deployment Using Multi-Stage Dockers"
by @levavakian & @bluryi some of our internal way of doing build/test/deployment using Docker:
[Video](https://vimeo.com/293626218),
[Slides](https://roscon.ros.org/2018/presentations/ROSCon2018_multistage_docker_for_robot_deployment.pdf).

This public repository, is designed to consume the output of our private `fetch_drivers` repository and enable
Fetch Research Platform users access to the drivers/firmware faster via the official ros packages.

To create the output of our private package, we have a special build job which runs inside of a docker container to ensure we don't accidentally
pull in any private dependencies, and also doesn't output any of the additional commercial robot drivers.

Previously, we built our drivers on a private buildbot, and hosted them on our own packages site.
We also had a manually synced mirror of the ros packages. This allowed us to ensure we tested the versions of dependancies which were on our mirror.
The old process was not as automated as we would like.

We're in the process of testing ROS Melodic, and setting up our hosted stable mirror, and documenting the upgrade process to ensure Fetch Research Platform customers have a smooth transition.

We will announce to our customers when we're officially ready and supporting ROS Melodic.

See https://docs.fetchrobotics.com for more information.
