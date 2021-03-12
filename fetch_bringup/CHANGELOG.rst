^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package fetch_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.9.2 (2021-03-12)
------------------

0.9.1 (2021-03-05)
------------------
* Changes for Noetic/Py3 (`#61 <https://github.com/fetchrobotics/fetch_robots/issues/61>`_)

  * Remove some ps3 controller references (no longer supported)
  * Update state_publisher -> robot_state_publisher
  * Changes for compatibility with new drivers:
    Drivers primarily load some params from a json file which
    end-users shouldn't need to modify. This file will live in
    /opt/ros/noetic or the catkin workspace for 99% of usecases.
  * Add explicit setting for fetch teleop param.
  * Point to a new drivers binary release (0.9.0)
  * Respawn tuck_arm node on shutdown [OPEN-48]

* Add soundplay ROS node as systemd service (`#53 <https://github.com/fetchrobotics/fetch_robots/issues/53>`_)
  Functionality existed in 14.04/indigo, and was initially left out.
* Contributors: Eric Relson

0.8.8 (2019-08-21)
------------------

0.8.7 (2019-08-06)
------------------
* Move ds4drv dep from package.xml to sys-config deb (`#48 <https://github.com/fetchrobotics/fetch_robots/issues/48>`_)
  ROS buildfarm doesn't support pip dependencies.
  Also removed outdated sixad line. We don't install sixad at all in 18.04.
* Update launch files to support PS4 teleop w/ds4drv
  - Teleop: Change default /joy/dev param to /dev/fetch_joy to match
  udev rules
  - Add ps4 flag/arg to default fetch.launch and freight.launch
  - As workaround to a weird bug, renamed 'joy' node to 'joy_node'
* remove respawn in fetch_bringup/launch/include/teleop.launch.xml (`#44 <https://github.com/fetchrobotics/fetch_robots/issues/44>`_)
  We want to enable launching the teleop node and it's components separately, without duplicate nodes continually respawning.
* Merge pull request `#37 <https://github.com/fetchrobotics/fetch_robots/issues/37>`_ from 708yamaguchi/melodic-devel
  Add params for selecting teleop part for melodic
* add joystick deadzone parameter (`#42 <https://github.com/fetchrobotics/fetch_robots/issues/42>`_)
* Add argument to select launching teleop (`#40 <https://github.com/fetchrobotics/fetch_robots/issues/40>`_)
  - add argument to select launching teleop for Fetch
  - add argument to select launching teleop for freight
* add params for selecting teleop part
* Contributors: Andrew Parker, Carl Saldanha, Eric Relson, Naoya Yamaguchi, Shingo Kitagawa

0.8.6 (2019-02-28)
------------------

0.8.5 (2019-02-26)
------------------

0.8.4 (2019-02-21)
------------------
* Add additional convenience packages as deps (`#33 <https://github.com/fetchrobotics/fetch_robots/issues/33>`_)
  * Add additional convenience packages as deps
  * system config deb pulls in rest of debs
  * Fix netplan configuration approach
* Contributors: Eric Relson

0.8.3 (2019-02-15)
------------------

0.8.2 (2019-02-15)
------------------
* Merge pull request `#30 <https://github.com/fetchrobotics/fetch_robots/issues/30>`_ from moriarty/rebased-pr-26
  [bringup] package format v2 (originally `#26 <https://github.com/fetchrobotics/fetch_robots/issues/26>`_)
* Add ps3joy exec dep; update to package.xml 2.0
  Also removed robot_controllers_msgs for fetch_bringup. This dependency
  is part of fetch_drivers package already.
* Contributors: Alex Moriarty, Eric Relson

0.8.1 (2019-02-15)
------------------

0.8.0 (2019-02-13)
------------------
* Add autodocking to default robot launch (`#28 <https://github.com/fetchrobotics/fetch_robots/issues/28>`_)
  Also update package.xml
* sixad depend not needed anymore on bionic (`#24 <https://github.com/fetchrobotics/fetch_robots/issues/24>`_)
  * sixad depend not needed anymore on bionic
  * remove sixad from fetch_bringup
* [ros param] adds robot/name robot/type (`#22 <https://github.com/fetchrobotics/fetch_robots/issues/22>`_)
  add robot specific information on rosparam, see https://github.com/ros-infrastructure/rep/pull/104
  Related to: `ros-infrastructure/rep#104 <https://github.com/ros-infrastructure/rep/issues/104>`_
* Contributors: Eric Relson, Kei Okada, Steffen Fuchs

0.7.5 (2017-06-12)
------------------
* Add diagnostics aggregator launch and config
* add cartesian twist controller to arm defaults
* Contributors: Eric Relson, Hanjun Song, Michael Ferguson

0.7.4 (2017-03-28)
------------------
* Updates for research robots
* Contributors: Michael Ferguson

0.7.3 (2016-08-26)
------------------
* Add install rule for software runstop
* Software runstop support via controller and topics
* Contributors: Eric Relson

0.7.2 (2016-06-14)
------------------

0.7.1 (2016-05-05)
------------------
* update to use /dev/ps3joy
* Contributors: Michael Ferguson

0.7.0 (2016-03-28)
------------------
* fix dependency issue with sixad
* Contributors: Michael Ferguson

0.6.1 (2016-03-22)
------------------
* require latest sixad
* Add autorepeat_rate parameter to teleop launch
* Contributors: Michael Ferguson, Michael Hwang

0.6.0 (2015-06-23)
------------------
* start tuck_arm.py as joystick teleop
* disable gripper when resetting controllers
* Contributors: Michael Ferguson

0.5.5 (2015-05-21)
------------------
* use no_delay parameter with graft
* Contributors: Michael Ferguson

0.5.4 (2015-05-10)
------------------
* filter shadow points from laser
* reorganize launch files for easier updating of calibrated robots
* Contributors: Michael Ferguson

0.5.3 (2015-05-03)
------------------
* use new laser safety feature of base controller
* add firmware param for gripper
* Contributors: Michael Ferguson

0.5.2 (2015-04-19)
------------------
* hold position when stopped
* add default calibration_date
* Contributors: Michael Ferguson

0.5.1 (2015-04-09)
------------------
* add controller reset script
* gas spring replaces gravity comp
* added debug flag for fetch drivers
* Contributors: Aaron Blasdel, Michael Ferguson

0.5.0 (2015-04-04)
------------------

0.4.2 (2015-03-23)
------------------
* add depend on joy
* Contributors: Michael Ferguson

0.4.1 (2015-03-23)
------------------

0.4.0 (2015-03-22)
------------------
* update to use fetch_teleop
* Contributors: Michael Ferguson

0.3.2 (2015-03-21)
------------------
* specify minimum version of laser drivers
* fix graft launch file include
* add head camera calibration
* update laser parameters
* Contributors: Michael Ferguson

0.3.1 (2015-03-13 19:53)
------------------------

0.3.0 (2015-03-13 18:59)
------------------------
* first release
* Contributors: Michael Ferguson
