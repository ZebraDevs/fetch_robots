cmake_minimum_required(VERSION 3.5)
project(fetch_drivers)

###
#
# This is the public version of fetch_drivers.
# 
# This is a binary only release of our dirvers and firmware.
# The drivers and firmware have been compiled for our research robots, inside of Docker containers on our TeamCity build servers.
#
# The resulting output of that build job a tar.gz, where the build job should only copy in what is required for the research robots.
# This public repository, just pulls in that tar.gz and extracts installs it into ROS/catkin paths.
##

find_package(catkin REQUIRED
  COMPONENTS
    mk
)

## System dependencies are found with CMake's conventions
find_package(Boost REQUIRED
  COMPONENTS
    chrono
    filesystem
    program_options
    regex
    system
    thread
)
find_package(CURL REQUIRED)
find_package(PythonLibs REQUIRED)
find_package(yaml-cpp REQUIRED)

add_custom_target(
  binary_driver ALL
  COMMAND cmake -E chdir ${PROJECT_SOURCE_DIR} $(MAKE) -f Makefile.tarball
  COMMAND cmake -E make_directory ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_LIB_DESTINATION}/${PROJECT_NAME}
  COMMAND cmake -E copy_if_different ${PROJECT_SOURCE_DIR}/build/output/lib/libfetch_drivers.so               ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_LIB_DESTINATION}/libfetch_drivers.so
  COMMAND cmake -E copy_if_different ${PROJECT_SOURCE_DIR}/build/output/lib/libfetch_drivers_odva.so          ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_LIB_DESTINATION}/libfetch_drivers_odva.so
  COMMAND cmake -E copy_if_different ${PROJECT_SOURCE_DIR}/build/output/lib/liblaser_filter_plugins.so        ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_LIB_DESTINATION}/liblaser_filter_plugins.so
  COMMAND cmake -E copy_if_different ${PROJECT_SOURCE_DIR}/build/output/lib/liblaser_self_filter.so           ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_LIB_DESTINATION}/liblaser_self_filter.so
  COMMAND cmake -E copy ${PROJECT_SOURCE_DIR}/build/output/lib/${PROJECT_NAME}/*                              ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_LIB_DESTINATION}/${PROJECT_NAME}/
  COMMAND cmake -E make_directory ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_SHARE_DESTINATION}/${PROJECT_NAME}
  COMMAND cmake -E copy_if_different ${PROJECT_SOURCE_DIR}/build/output/share/${PROJECT_NAME}/firmware.tar.gz   ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_SHARE_DESTINATION}/${PROJECT_NAME}/
  COMMAND cmake -E copy_if_different ${PROJECT_SOURCE_DIR}/build/output/share/${PROJECT_NAME}/laser_filters.xml ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_SHARE_DESTINATION}/${PROJECT_NAME}/
)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
   LIBRARIES fetch_drivers
   CATKIN_DEPENDS
     actionlib
     actionlib_msgs
     diagnostic_msgs
     fetch_driver_msgs
     fetch_auto_dock_msgs
     nav_msgs
     power_msgs
     robot_calibration_msgs
     roscpp
     sensor_msgs
   DEPENDS
     Boost
     CURL
     PYTHON
     YAML_CPP
)

###########
## Build ##
###########

#############
## Install ##
#############

install(
  FILES build/output/lib/libfetch_drivers.so build/output/lib/libfetch_drivers_odva.so
  DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
)

install(
  DIRECTORY build/output/lib/fetch_drivers
  DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  PATTERN "build/output/lib/fetch_drivers/*"
  PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
              GROUP_EXECUTE GROUP_READ
              WORLD_EXECUTE WORLD_READ
)

install(
  FILES build/output/share/${PROJECT_NAME}/firmware.tar.gz build/output/share/${PROJECT_NAME}/laser_filters.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
