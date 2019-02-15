^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package fetch_drivers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.8.2 (2019-02-15)
------------------
* [fetch_driver] Makefile and mk depend on rospack
  mk uses rospack internally but we don't get the rospack dependency.
  https://github.com/ros/ros/issues/204
  We also call rospack in Makefile.tarball so we should directly depend on
  it instead of assuming it is depended on by ros/core/mk.
* Contributors: Alexander Moriarty

0.8.1 (2019-02-15)
------------------
* Merge pull request `#29 <https://github.com/fetchrobotics/fetch_robots/issues/29>`_ from moriarty/fix-build-deps
  [fetch_drivers] exec_depend -> build_depend
  I left find_package in the CMakeLists.txt for these dependencies.
* Contributors: Alexander Moriarty, Carl Saldanha

0.8.0 (2019-01-30)
------------------
* Merge pull request `#27 <https://github.com/fetchrobotics/fetch_robots/issues/27>`_ from moriarty/fetch-binary-drivers
  [fetch_binary_drivers] new [fetch_drivers] package
* [fetch_drivers] add more dependencies
  All these dependencies are exec_dependencies because this
  package doesn't compile anything.
  They're also in the CMakeLists.txt in the catkin_package and find_package to be safe.
* [fetch_binary_drivers] new [fetch_drivers] package
  This is a new package providing the "fetch_drivers" which was previously
  built internally and distributed as a binary only debian package.
  We will officially announce when the upgrade from Indigo->Melodic is
  ready.
  18.04 and ROS Melodic on the Fetch Research Platforms is still being
  tested.
  The process isn't straight foward as there are calibration files
  which you will want to back-up before the upgrade.
  This `fetch_drivers` package also won't start like it use to because of
  the change from `upstart` to `systemd`.
  That requires `fetch_system_config` which will be open sourced soon.
  This `fetch_binary_drivers` package is part of a plan to distribute
  updates and upgrades to Fetch Research Platform customers faster in the future.
  This relates to `fetchrobotics/fetch_ros#63 <https://github.com/fetchrobotics/fetch_ros/issues/63>`_
  1. An officiall announcement will be made when everything is ready.
  2. We will update and document the process on:
  https://docs.fetchrobotics.com/
  3. We will also announce via our mailing list, ros discourse and post on:
  https://opensource.fetchrobotics.com/
* Contributors: Alexander Moriarty, Carl Saldanha, Eric Relson

0.8.0 / 2018.8  (2019-01-30)
----------------------------
* added public binary driver creation system for <https://github.com/fetchrobotics/fetch_binary_drivers>
* Merge pull request `#1364 <https://github.com/fetchrobotics/fetch_drivers/issues/1364>`_ from dbking77/combined_gyro_zeroing_fix_2018.8
  Have zero gyro\_ state (for dual_imu_publisher), not just output message.
* Merge pull request `#1335 <https://github.com/fetchrobotics/fetch_drivers/issues/1335>`_ from dbking77/combined_gyro_output_disable_delay_2018.8
  Don't instantly zero combined gyro when enbale_gyro_output is false, instead
  allow each invidual gyro to do their own thing.
  This is related to a feature that was implemented with
  https://github.com/fetchrobotics/fetch_drivers/pull/1103
* Merge pull request `#1309 <https://github.com/fetchrobotics/fetch_drivers/issues/1309>`_ from dbking77/accel_direction_fixup_for_2018.8
  Reorder accelerometer axes for revI and newer mainboards.
* Support for mainboard rev I and J
  Updates to docs describing adding a new board.
* Merge pull request `#1259 <https://github.com/fetchrobotics/fetch_drivers/issues/1259>`_ from dbking77/imu_param_description_fix
  Fix description of a couple IMU parameters.
* Update Dockerfile
* Merge pull request `#1202 <https://github.com/fetchrobotics/fetch_drivers/issues/1202>`_ from moriarty/compatibility-fixes
  [ROS][C++] Indigo & Melodic Compatibility fixes
  [C++] urdf/model.h upstream compatibility ptr
  This fixes `#1181 <https://github.com/fetchrobotics/fetch_drivers/issues/1181>`_ and can fix `fetchrobotics/fetch_ros#86 <https://github.com/fetchrobotics/fetch_ros/issues/86>`_
  Upstream urdf/model.h has changed, and a fix backported to indigo.
  The fix is only available if you upgrade your ROS indigo pacakges.
  This fix should work for all three cases
  backport not available, backport available, backport not needed.
* [C++] catch errors by const ref (`#1201 <https://github.com/fetchrobotics/fetch_drivers/issues/1201>`_)
  This fixes the warning as error:
  catching polymorphic type ‘class std::runtime_error’ by value
  [-Werror=catch-value=]
* Added low charge and critical charge LED effects.
  FIRM-59
* More extensive docker stuff as well as a fix for testing master (`#1186 <https://github.com/fetchrobotics/fetch_drivers/issues/1186>`_)
* Merge pull request `#1184 <https://github.com/fetchrobotics/fetch_drivers/issues/1184>`_ from dbking77/eth_state_machine
  Object-based state machine to operation Ethernet + LwIP stack
* Merge pull request `#1187 <https://github.com/fetchrobotics/fetch_drivers/issues/1187>`_ from chadrockey/1604_fixes
  Small Fixes to allow building on 16.04
* Use std::isnan instead of isnan
* Add missing catkin dependencies for actionlib messages
* Move header files shared by driver and firmware to shared directory. (`#1167 <https://github.com/fetchrobotics/fetch_drivers/issues/1167>`_)
  Also:
  - Put shared structs/enums in fetch_drivers::shared namespace.
  - Change include of stdint.h cstdint.
  - Put BoardFlags, PanelFlags, and TorsoSensorParams in a struct.
  - Update gitignore to ignore bootloader and firmware.
* Contributors: Alexander Moriarty, Andrew Parker, Carl Saldanha, Chad Rockey, Derek King, Eric Relson, Jeff Wilson, Justin Watson, Luc Bettaieb, Niharika Arora, Sarah Elliott

0.7.29 (2018-01-29)
-------------------
* Merge pull request `#1047 <https://github.com/fetchrobotics/fetch_drivers/issues/1047>`_ from dbking77/depracate_breaker_scripts
  Enable/disable breaker scripts are old and perform no error checking.
* Enable/disable breaker scripts are old and perform no error checking.
  Use breaker.py or c++ breaker tool instead.
* Merge pull request `#1043 <https://github.com/fetchrobotics/fetch_drivers/issues/1043>`_ from dbking77/read_board_unique_id_fixes
  Allow read_board to continue even if unique ID cannot be read.
* Merge pull request `#1042 <https://github.com/fetchrobotics/fetch_drivers/issues/1042>`_ from dbking77/motor_control_flags_namespace_fix
  MotorControlFlag namespace fix.
* Allow read_board to continue even if unique ID cannot be read.
* MotorControlFlag namespace fix.
* Merge pull request `#1041 <https://github.com/fetchrobotics/fetch_drivers/issues/1041>`_ from dbking77/charger_diagnostics_fix2
  Fix incorrect virtual function in ChargerStatusGenerator class.
* Fix incorrect virtual function in ChargerStatusGenerator class.
  Virtual function should be collect(void) not collect(double).
  Because base class provided default collect(), there was no compile time error, but diagnostics output for charger was mostly garbage.
  Add "override" to all sub-class virtual function definitions so this would cause a compile time error if this happens again.
  Remove virtual from all sub-class function definitions (it is redudant, and kind silly now that override exists)
* Add units to system time in read_board
* Merge pull request `#1033 <https://github.com/fetchrobotics/fetch_drivers/issues/1033>`_ from briancairl/NAV-1006
  NAV-1006 : Adds filter plugin for filtering neighborhoods which span a small distance
* Add option to prevent use of gyro1 or gyro2 in combined gyro output. (`#1032 <https://github.com/fetchrobotics/fetch_drivers/issues/1032>`_)
  * Add option to prevent use of gyro1 or gyro2 in combined gyro output.
  * Increase gyro covariance when neither gyro is available.
* Adds filter plugin for filtering neighborhoods which span a small distance
  Changes default filter plugin chain to filter small clusters (in the maximum spanning distance sense) as opposed to groups with few points
* Have imu test create CSV log of collected IMU data. (`#1031 <https://github.com/fetchrobotics/fetch_drivers/issues/1031>`_)
  Have imu test create CSV log of collected IMU data.
  Also support test option for revH boards on the command line.
  Also, added function to load saved CSV file.
* qual 0.2.30: Support new primesense topic count
  - Update restart_checker and initial_qual as well
  - Also clean up imports and whitespace
  - Add to .gitignore
* Merge pull request `#1020 <https://github.com/fetchrobotics/fetch_drivers/issues/1020>`_ from aravindsv/AVRfirmware
  Modified makefile so there is no linking step
* Merge pull request `#1027 <https://github.com/fetchrobotics/fetch_drivers/issues/1027>`_ from dbking77/robot_log_split_plots
  Put break between different logs in plots from robot_log.csv
* Merge pull request `#1026 <https://github.com/fetchrobotics/fetch_drivers/issues/1026>`_ from fetchrobotics/montana_1000
  Remaining issues for Montana
* Merge pull request `#1013 <https://github.com/fetchrobotics/fetch_drivers/issues/1013>`_ from dbking77/led_panel_test
  Combine all charger LED control into single class to allow testing.
* ADc Interrupts are working. UART bitbang timing is off, so debugging results is
  sketchy at best
* Also print dates for log start and stop times.
* fix led movement when moving very slowly
* fixes to make new led manager work with montana
  * panel and strip share same SPI interface
  * runstop state should still be sent to LED strip, so it is red
* Have option to put breaks between driver starts in logs.
  Put battery SOC data on separate plots (otherwise stuff is too confusing).
* properly set velocity/acceleration limits
* apply proper current limit for 1500
* set fault if EDM error
* use standstill flag when present
* update to flexisoft r7
* Modified uart timing so data can be read by logic analyzer
* Cleaned up some indentation and added a note in Makefile_defines
* User serial for updating logpro record
* Remove Access Panel LED test
  Stopping the robot drivers blinks all LEDs and this is a sufficient test.
* Combine all freight100 and montana panel LED control into single class to allow testing.
  - Add interface to allow test to be run on all LEDs at once
  - Time limit test mode, and also enable it for production firmware
  - For device without LED panel driver, provide "fake" interface (to avoid extra ifdefs)
  - Script to put LEDs into testing mode
* Wrote bitbanged sendString for uart
* Modified makefile so there is no linking step. Otherwise, no main
* Merge pull request `#1019 <https://github.com/fetchrobotics/fetch_drivers/issues/1019>`_ from fetchrobotics/boot_with_bms
  turn on BMS on boot
* turn on BMS on boot
* add some documentation
* Merge pull request `#1014 <https://github.com/fetchrobotics/fetch_drivers/issues/1014>`_ from dbking77/measure_joint_linearization
  Modify linearize_motor script to plot joint non-linearity
* Modify linearize_motor script to plot joint non-linearity
  Also:
  - Update command line parsing to use argparse
  - More comments about linearizing motor vs linearizing joint
* Contributors: Aravind Vadali, Brian Cairl, Derek, Derek King, Eric Relson, Michael Ferguson

0.7.28 (2017-11-16)
-------------------
* Merge pull request `#1011 <https://github.com/fetchrobotics/fetch_drivers/issues/1011>`_ from briancairl/intensity-filter-vinyl-cuts
  Updates intensity filter defaults; updates logging
* Merge pull request `#1009 <https://github.com/fetchrobotics/fetch_drivers/issues/1009>`_ from dbking77/mainboard_rev_h
  Mainboard Rev-H
* Updates intensity filter defaults; updates logging
* Update balancing testing.
* Software support for battery balancing current measurement.
* Firmware support for battery balancing current measurement.
* Merge pull request `#1007 <https://github.com/fetchrobotics/fetch_drivers/issues/1007>`_ from fetchrobotics/low_power
  add low power mode to montana
* Merge pull request `#1006 <https://github.com/fetchrobotics/fetch_drivers/issues/1006>`_ from erelson/add_local_fix
  Also remove freightXX.local from knownhosts
* Also remove freightXX.local from knownhosts
* Remove fetchcore_tools depend and bump robot_qual version
* Remove commented code blocks
* Don't remove public ssh keys in robot qual
* Remove unneccessary hmi screen check
* increased sleep time and switched to fetch_drivers charger_power reboot for power cycle
* Merge pull request `#951 <https://github.com/fetchrobotics/fetch_drivers/issues/951>`_ from erelson/arm_motor_no_joint_test
  Add test for arm joints running fake-joint firmware
* Refactors laser filter; makes configurable through plugins (`#1005 <https://github.com/fetchrobotics/fetch_drivers/issues/1005>`_)
  * Converts existing filter to proper filter plugins
  - Removes excessive scan copying between filter stages
  - Adds filter plugin which loads/runs a sequence of filters
  - Adds Chain (adds sequential filters)
  - Adds Branch (adds parallel branch of filters)
  - Adds min-neighborhood laser filter
  - Adds laser scan publisher component
  - Updates laser_filter node to use new plugin objects
* with interface
* alternate sides working
* add swirl
* Add breakfree test for jointless motors
* Add test for arm joints running fake-joint firmware
* add low power (tested, but needs interface)
* Contributors: Brian Cairl, David Moon, Derek, Derek King, Eric Relson, Michael Ferguson, Xu Han

0.7.27 (2017-11-05)
-------------------
* Add small group filtering to intensity filter
* Contributors: Brian Cairl

0.7.26 (2017-11-01)
-------------------
* Merge pull request `#1003 <https://github.com/fetchrobotics/fetch_drivers/issues/1003>`_ from aravindsv/DutyCycleCap
  Capped hmi led pulse mode at 33% duty cycle
* Merge pull request `#1001 <https://github.com/fetchrobotics/fetch_drivers/issues/1001>`_ from briancairl/intensity-filter
  Adds laser_intensity filter; refactors laser_filter module
* Capped hmi led pulse mode at 33% duty cycle
* Adds intensity filter with hooking mode
  - Adds to filter chain: pass-through with repub hook
* Refactors laser_filter module organization
* Contributors: Aravind Vadali, Brian Cairl, Derek, Michael Ferguson

0.7.25 (2017-10-27)
-------------------

* Charger firmware version 102:
  * Add flags for charger balancing and fan configs
* IO_485 firmware version 101:
  * Improve analog processing
* Montana firmware version 101: increase cutoff voltage
* montana_driver: additional diagnostics
* montana_driver: publish motor state, charger state
* montana_driver: reduce timeout to 100ms
* montana_driver: disable drives when charging
* read_board: fix some issues with lack of metadata
* read_board: add support for IO_485 board
* align_motor: improve error messages
* charger_lockout: new tool to set lockout time
* laser_self_filter: add padding option
* add support for head mcb rev D.0
* add support for round mcb rev D.0
* add support for large mcb rev E.0
* Contributors: Aravind Vadali, Brian Cairl, David Moon, Derek King, Eric Relson, Michael Ferguson

0.7.24 (2017-09-13)
-------------------
* cart_dock_driver: add diagnostics publisher, read-only updates until ready
* io_mpu_driver: add diagnostics publisher, read-only updates until ready
* gripper_driver: add diagnostics publisher, read-only updates until ready
* freight_driver: fix issue with panel led flags
* add io_485 support
* Contributors: David Moon, Derek, Michael Ferguson, Aravind Vadali

0.7.23 (2017-09-07)
-------------------
* Charger firmware version 101:
  * Send response to panel flags writes.
  * Add support for rev H.
* Mainboard firmware version 100:
  * Add support for rev H.
* Fix some issues with automatic firmware cross/downgrade
* Gripper driver: improve startup reliability
* Contributors: Derek King, Eric Relson, Michael Ferguson

0.7.22 (2017-08-29)
-------------------
* Mainboard firmware version 100:
  * Expose both gyros
* Charger firmware version 100:
  * Save SOC before rebooting
  * Add support for rev. G boards
* MCB firmware version 100:
* IO Board firmware version 100:
* Gripper firmware version 100:
  * Cancel command on board reset
* F500/1500 firmware version 100:
  * Expose both gyros
* Add automatic firmware cross/downgrade
* cart_dock_driver: add firmware management
* io_mpu_driver: add firmware management
* F500/1500 driver: improve imu filtering
* F500/1500 driver: always set robot/serial parameter
* Contributors: David Moon, Derek King, Eric Relson, Michael Ferguson

0.7.21 (2017-07-27)
-------------------
* F500/1500 firmware version 12:
  * Give gyros extra time to start up
  * Update charge LED usage
  * Update panel LED usage to match F100.
* Charger firmware version 87:
  * Move panel LED register out of board flags
* Fix F500/1500 drivers to actually update firmware
* Fix F500/1500 drivers not to stop charging on driver restart
* Add CSV logging to F500/1500 drivers
* Update read_board to work with F500/1500
* Install F500/1500 driver
* Contributors: Aaron Gemmell, David Moon, Derek King, Michael Ferguson

0.7.20 (2017-07-11)
-------------------
* IO Board firmware version 5:
  * Fix issue with LED strip lockup
* Drivers: add support for mlockall/nice
* Drivers: fix for empty motor messages
* Drivers: update Ethernet/IP devices while not ready (Freight-500/1500)
* Contributors: Alex Henning, Derek King, Eric Relson, Michael Ferguson

0.7.19 (2017-06-22)
-------------------
* Charger firmware version 86:
  * Turn off leds when in low-power notification mode
* IO Board firmware version 4:
  * Better locking around HMI led status
* Initial Freight-500 driver
* Contributors: Aaron Gemmell, Eric Relson, Michael Ferguson

0.7.18 (2017-06-19)
-------------------
* Charger firmware version 85:
  * Better low-battery indication
  * Adds battery balancing configuration
  * Blink wifi/fc/runstop LEDs when disconnected
  * Fixes issue with LED panels locking up
  * Fixes potential issue of getting stuck in a voltage ramp
* IO board firmware version 3:
  * Initial release
* Initial release of io_mpu_driver
* Initial release of field charging test
* Drivers: actually start charge lockout action server
* Drivers: also log SOC
* Drivers: update LED panel even when not "ready"
* Drivers: ignore timeouts during shutdown to avoid spurious faults
* Contributors: Brian Cairl, David Moon, Derek King, Eric Relson, Michael Ferguson, Michael Janov, Aaron Gemmell

0.7.17 (2017-03-15)
-------------------
* Charger firmware version 79:
  * Add support for LED panel on Rev. F
  * Allow faster charging at higher temperatures
* Mainboard firmware version 63
  * Allow breakers to run hotter
* Add support gripper Rev. E
* Adds robot CSV logger
* Updated laser filter with support for carts
* Add battery SOC tool
* Contributors: Brian Cairl, Derek King, Michael Ferguson

0.7.16 (2016-12-16)
-------------------
* Charger firmware version 75
  * Improves balancing of batteries for better life
  * Improves state of charge estimation during partial discharges
  * Add interface for forcing computer restart
* Add stale data detection to drivers
* Add charger_power tool
* Contributors: Derek King, Eric Relson, Michael Ferguson

0.7.15 (2016-11-29)
-------------------

* Charger firmware version 72
* Gripper firmware version 70
* MCB firmware version 76:
 * Reset hall encoder error counters when signal good
* Mainboard firmware version 62:
 * Initial support for Rev. F boards
 * Add support for dual gyro
* Breaker tool: fix typo in usage message
* Update tool: fix issues with gripper update
* Fix issue with debug packets showing as lost packets
* Add support for automatically  enabling/disabling aux breaker on startup
* Contributors: David Moon, Derek King, Eric Relson, Michael Ferguson

0.7.14 (2016-08-25)
-------------------

* MCB firmware version 75:
 * Add support for cart docking mechanism MCB
* Add support for revision F mainboard/charger
* Add support for revision D large mcb
* Add enviroment variable support to dynamically set driver ip
* Gripper driver now publish IMU data (there is no calculation of gyro offset).
* Set/Reset fault state properly in hourly logs
* Contributors: Aaron Blasdel, Aravind Vadali, Camilo Buscaron, David Moon, Derek King, Eric Relson, Michael Ferguson

0.7.13 (2016-06-21)
-------------------

* MCB firmware version 74:
  * Improve base motor alignment at higher torques
  * Reduce minimum voltage before fault
  * Recalculate joint position when offset changes
* Charger firmware version 71:
  * Improvements for faster charging, better heat management
  * Send fault log on low-battery poweroff
* Gripper firmware version 69
* Mainboard firmware version 61
* Contributors: Brian R Cairl, Derek King, Eric Relson, Michael Ferguson, Camilo Buscaron

0.7.12 (2016-06-09)
-------------------
* Increase ADC sampling time for battery inputs.
* Add aux option to breaker tool.
* Use template parameters for GPIO interrupts instead of global variables.
* Contributors: Derek King, Eric Relson, Michael Ferguson

0.7.11 (2016-05-26)
-------------------
* MCB firmware version 73:
  * Add separate error flag for joint position monitor
* Charger firmware version 69:
  * Slightly increase cyclic battery charging voltages
  * New battery voltage controller that is less likely to overshoot
* Mainboard firmware version 60:
  * Disable breakers when shutting down
* Update tool: fix identification of freights
* Drivers: publish diagnostics for aux breakers
* Contributors: Derek King, Eric Relson, Michael Ferguson

0.7.10 (2016-05-19)
-------------------
* MCB firmware version 72:
  * Fix potential overflow in callbacks
* Gripper firmware version 68:
  * Fix potential overflow in callbacks
* Mainboard firmware version 59:
  * Fix potential overflow in callbacks
* Charger firmware version 68:
  * Fix potential overflow in callbacks
* Fix issues with handling of continuous joints
* Add gripper state publishing
* Contributors: Camilo Buscaron, Derek King, Eric Relson, Michael Ferguson

0.7.9 (2016-05-08)
------------------
* MCB firmware version 71:
  * Increase base motor torque and power limits for Freight
* Firmware upload: convert board ID to int before printing
* Align motor tool: fix printed output
* Contributors: Camilo Buscaron, Derek King, Eric Relson, Michael Ferguson

0.7.8 (2016-04-27)
------------------
* Mainboard firmware version 57:
  * Fix communications lockup regression
* Fix bug when has_base is false
* Contributors: Camilo Buscaron, Derek King, Eric Relson, Michael Ferguson

0.7.7 (2016-04-14)
------------------
* Mainboard firmware version 56:
  * Block gyro glitches
  * Fix occasional communications lockup when runstopped
* Charger firmware version 67:
  * State of charge improved when robot has not fully charged in a long time
* Gripper firmware version 66:
  * Block gyro glitches
* Publish zeroed IMU data when runstopped, prevents "wandering" robot
* Enable auxillary breaker services
* Torso Calibration Tool: log results
* Read Board Tool: also get unique serial
* Breaker Tool: fix to exit when arguments are not valid
* Firmware Update Tool: better handle when ACKs are missed
* Contributors: Derek King, Eric Relson, Michael Ferguson

0.7.6 (2016-03-19)
------------------
* Mainboard firmware version 55, Gripper version 65:
  * Updates for gyro glitches
* Contributors: Derek King, Michael Ferguson


0.7.5 (2016-03-09)
------------------
* MCB firmware version 70:
  * Add filter gains for older MCBs driving new suspension and motors
  * Fix for mcb encoder error on boot
* Mainboard firmware version 54:
  * Updates for gyro data glitches
  * Check computer current before asserting computer power button signal
    to avoid turning computer back on at power-off if already shutdown
* Charger firmware version 66:
  * Fixes missed timing error that sometimes occurs when disabling charging
* Gripper firmware version 64:
  * Updates for gyro data glitches
* Assume runstopped robot is moving, do not update IMU offset.
* Gyro offset calculation improved for faster convergence
  and improved noise immunity.
* Additional locking around data published in ROS.
* New read_board, breaker, align_motor, and joint_offset tools
* Add DisableChargingAction to avoid hot unplugging
* Contributors: Brian R Cairl, Casey Duckering, Derek King, Eric Relson,
  Griswald Brooks, Michael Ferguson, Bhavya Kattapuni, Camilo Buscaron

0.7.4 (2016-01-12)
------------------
* MCB firmware version 66:
  * Increase filtering to reduce buzz on new motors with type 3 suspension.
  * Monitor joint position compared to motor sensor position.
* Charger firmware version 61:
  * Load saved battery SOC data from flash on boot.
* Fix logpro logging when robot is calibrated
* Check for zero joint_ratio value.
* Update tool: Add option to force updates of all detected boards.
* Torso calibration tool: first release.
* Contributors: Derek King, Eric Relson, Michael Ferguson, Camilo Buscaron

0.7.3 (2015-11-20)
------------------
* MCB firmware version 63:
  * Fix bug where position gains are being set instead of velocity gains.
* Contributors: Derek King, Michael Ferguson

0.7.2 (2015-11-20)
------------------
* MCB firmware version 62:
  * Add support for calibration of torso initialization sensor
* Fix occasional bug in unique ID response packet parsing
* Add additional checks on unique ID
* Contributors: Derek King, Eric Relson, Michael Ferguson, Camilo Buscaron

0.7.1 (2015-11-11)
------------------
* MCB firmware version 61
  * Add suport for mcb rev C.1
* Fix issue with unrefreshed gripper MCB register table that
  caused slow LED change action.
* Contributors: Derek King, Michael Ferguson

0.7.0 (2015-11-02)
------------------
* MCB firmware version 60
  * Updated wrist flex joint limits to match URDF
  * Disabled flash write when motor is running
* Gripper firmware version 60
* Charger firmware version 60
  * Add state of charge estimation
  * Fix occasional POWER_NOT_GOOD issue on breakers after reboot
* Mainboard firmware version 50
* LogPRO now logs calibration_date, mainboard voltage and dock usage info
* Make sure mainboard breakers are enabled after updating mainboard
* Publish current/temperature limits to ROS messages
* Support for rev2 robot hardware
* Contributors: Derek King, Michael Ferguson, Griswald Brooks, Eric Relson

0.6.3 (2015-07-21)
------------------
* Update build
* Contributors: Michael Ferguson

0.6.2 (2015-07-21)
------------------
* MCB firmware version 50
  * Better diagnostics for torso sensor values
* Contributors: Michael Ferguson

0.6.1 (2015-07-09)
------------------
* Charger firmware version 34
  * state of charge improvements
* Update names of motors/boards in diagnostics and robot_state message
* Contributors: Derek King, Michael Ferguson

0.6.0 (2015-06-28)
------------------
* MCB firmware version 49
  * Various small improvements
* Charger firmware version 32
  * Audible noise fixes when charging hard
  * Disable charging before rebooting board
* Contributors: Derek King, Michael Ferguson
* never publish NaNs to robot_state, diagnostics
* Add ability to disable gripper torque
* Contributors: Derek King, Michael Ferguson

0.5.3 (2015-06-09)
------------------
* Gripper firmware version 48
  * Increase torque limit for gripper
* Charger firmware version 30
  * Multiple improvements to charging and diagnostics
  * Disable fan dc/dc when battery breaker is disabled
* Contributors: Derek King, Michael Ferguson

0.5.2 (2015-06-08)
------------------
* Gripper firmware version 47
  * update opening amount
* Charger firmware version 28
  * increase charging current
* Contributors: Derek King, Michael Ferguson

0.5.1 (2015-06-06)
------------------
* MCB firmware version 47
  * Reduce friction compensation settings in arm.
  * Lock the gains/limits for production robots
  * Fix shoulder_lift_motor gains
* Contributors: Derek King, Michael Ferguson

0.5.0 (2015-06-05)
------------------
* move messages into fetch_driver_msgs package
* MCB firmware version 46
  * Wrap position around velocity pid,  update gains
* Charger firmware version 27
  * Add power mismatch check
  * Fill in charger information in messages
* Mainboard firmware version 27
* Gripper firmware version 46
* Contributors: Derek King, Michael Ferguson

0.4.0 (2015-05-24)
------------------
* MCB firmware version 44
  * fix intermittent head pan range issue on startup
* Charger firmware version 24
  * additional table entries for new diagnostics
* Improved diagnostics for charger
* Improved diagnostics for common error conditions
* NOTE: RobotState message has changed, MD5 breaks from 0.3.14
* Contributors: Derek King, Michael Ferguson

0.3.14 (2015-05-22)
-------------------
* MCB firmware version 40
  * Supply current limit settings for arm motors
  * Overcurrent fault fix
  * Adds motor friction feed forward
  * Adjust arm motor ratios
* reset controllers when faulted/runstopped
* Contributors: Derek King, Mark Medonis, Michael Ferguson

0.3.13 (2015-05-10)
-------------------
* add filter that removes shadow points from TIM571
* update mainboard even if stuck in bootloader
* update charger firmware if needed
* Contributors: Michael Ferguson

0.3.12 (2015-05-06)
-------------------
* update firmware build
* Contributors: Derek King, Michael Ferguson

0.3.11 (2015-05-06)
-------------------
* updates to build
* Contributors: Derek King, Michael Ferguson

0.3.10 (2015-05-06)
-------------------
* updates to build
* Contributors: Michael Ferguson

0.3.9 (2015-05-06)
------------------
* MCB firmware version 40
  * increase mcb max temperature to 80C.
* Change keys for rev C. mainboard, charger, and freight mcbs.
* Contributors: Derek King, Michael Ferguson

0.3.8 (2015-05-03)
------------------
* Gripper/MCB firmware version 39
  * adds motor trace interface
  * init velocity filter before using motor angle
* gripper_driver now updates gripper firmware automatically

0.3.7 (2015-04-24)
------------------
* install update tool
* Contributors: Michael Ferguson

0.3.6 (2015-04-22)
------------------
* Gripper firmware version 23
  * implement gripper position control
  * report consistent id for gripper
* MCB firmware version 37
  * set NOT_READY flag when position is invalid
* wait for breaker to update before responding
* new update tool for firmware
* Contributors: Michael Ferguson, Derek King

0.3.5 (2015-04-20)
------------------
* MCB firmware version 36
  * New velocity filter for base, head
  * Updated shoulder lift limits
  * Adds torso initialization
* Adds support for charger revision C
* Publish correct breaker state
* Contributors: Derek King, Michael Ferguson

0.3.4 (2015-04-07)
------------------
* Charger firmware version 20
* Fix potential race condition in packet recieve
* make joints/motors of robot_state same order
* continue read-only during a fault
* Contributors: Derek King, Michael Ferguson

0.3.3 (2015-04-04)
------------------
* limit standard log update retry rate
* Contributors: Michael Ferguson

0.3.2 (2015-04-01)
------------------
* MCB firmware version 32
* New threading model with thread pool
* Fix breakers returning wrong state when DISABLED
* Disable robot if a breaker trippers
* Support for revision C mainboard
* Contributors: Aaron Blasdel, Derek King, Michael Ferguson

0.3.1 (2015-03-28)
------------------
* MCB firmware version 31
* Do not wind up base motor position
* Set version/serial ROS params
* Contributors: Derek King, Michael Ferguson

0.3.0 (2015-03-23)
------------------
* MCB firmware version 29
* Update how we handle continuous joints
* Add stall detection to gripper driver
* Contributors: Derek King, Michael Ferguson

0.2.1 (2015-03-17)
------------------
* MCB firmware version 28
* Fix for motor alignment
* Contributors: Derek King, Michael Ferguson

0.2.0 (2015-03-16)
------------------
* MCB firmware version 27
* Load position/velocity limits from URDF
* Gripper is now fully functional
* Contributors: Derek King, Michael Ferguson

0.1.3 (2015-03-13)
------------------
* Signifigant improvements to firmware and drivers
* Contributors: Derek King, Michael Ferguson

0.1.2 (2015-01-26)
------------------
* Build and install firmware
* Add support for breakers, IMU
* Contributors: Derek King, Michael Ferguson

0.1.1 (2015-01-07)
------------------
* Initial Release
* Contributors: Derek King, Michael Ferguson
