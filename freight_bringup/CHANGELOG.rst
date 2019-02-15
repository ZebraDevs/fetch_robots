^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package freight_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.8.2 (2019-02-15)
------------------
* Merge pull request `#30 <https://github.com/fetchrobotics/fetch_robots/issues/30>`_ from moriarty/rebased-pr-26
  [bringup] package format v2 (originally `#26 <https://github.com/fetchrobotics/fetch_robots/issues/26>`_)
* Remove unsupported PMD camera configuration
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
* Contributors: Eric Relson, Michael Ferguson

0.7.4 (2017-03-28)
------------------
* Updates for research robots
* Contributors: Michael Ferguson

0.7.3 (2016-08-26)
------------------
* added calibration_date param
* remove extra nodelet manager
* Contributors: Michael Ferguson, Niharika Arora

0.7.2 (2016-06-14)
------------------
* add launch_camera argument
* Contributors: Michael Ferguson

0.7.1 (2016-05-05)
------------------
* update to use /dev/ps3joy
* Contributors: Michael Ferguson

0.7.0 (2016-03-28)
------------------
* fix dependency issue with sixad
* Added PMD to freight.launch
* Contributors: Alex Henning, Michael Ferguson

0.6.1 (2016-03-22)
------------------
* require latest sixad
* Raised acceleration limits to 2.0
* Add autorepeat_rate parameter to teleop launch
* Contributors: Alex Henning, Michael Ferguson, Michael Hwang

0.6.0 (2015-06-23)
------------------

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
* Contributors: Michael Ferguson

0.5.2 (2015-04-19)
------------------
* hold position when stopped
* Contributors: Michael Ferguson

0.5.1 (2015-04-09)
------------------

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
* update laser parameters
* Contributors: Michael Ferguson

0.3.1 (2015-03-13 19:53)
------------------------

0.3.0 (2015-03-13 18:59)
------------------------
* initial release
* Contributors: Michael Ferguson
