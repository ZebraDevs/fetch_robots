#!/usr/bin/env python

# Copyright (c) 2016, Fetch Robotics Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Fetch Robotics Inc. nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL FETCH ROBOTICS INC. BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Author: Eric Relson

# Script launches a ROS node which can disable breakers. Node can be
# controlled via the /enable_software_runstop topic.
# Script is launched via e.g. teleop.launch.xml (or can be run by itself.)
#
# With the tele option the right two trigger buttons simultaneously pressed
# will cause breakers to be disabled on the robot.
# Software runstop is canceled by toggling the physical runstop (assuming the
# controller buttons have been released).
#
# Note that if script is ended while software runstop is enabled, script
# will need to be run again and controller buttons pressed again before
# physical runstop will disable software runstop, due to breaker states set via
# power_msgs persisting.

# Standard Library
from argparse import ArgumentParser

# Third Party
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Bool

# Fetch
from fetch_driver_msgs.msg import RobotState
from power_msgs.srv import BreakerCommand


# Listen to joy messages, when button held, reset controllers
class SoftwareRunstop(object):
    """Monitor /Joy and /RobotState to implement a software runstop.

    Parameters
    ----------
    arm, base, gripper : bools
        If True, corresponding breaker will be disabled by software runstop.
    tele : bool
        If True, will create a subscriber to /Joy which will monitor for
        button presses triggering the software runstop.

    Attributes
    ----------
    hw_runstop_has_been_pressed : bool
        Records if hardware runstop has been pressed while software runstop
        was enabled. Set by update().
    sw_runstop_enabled : bool
        If True, then the software runstop is enabled.
        Set by update().
    hw_runstop_state : bool
        True = hardware runstop is pressed.
        Set by /robot_state callback.
    enable_breakers : bool
        If True, will disable software runstop and re-power breakers.
        Set by update() or by callback for /enable_software_runstop.
    disable_breakers : bool
        If True, will enable software runstop and disable the breakers.
        Set by update() based on /Joy and /enable_software_runstop callback
        methods.
    disable_breakers_tele : bool
        Indicates that controller wants breakers to be disabled (i.e.
        enable the software runstop).
        Requires the --tele option for related subscriber to be created.
        Set by joy_callback; disabled by update().
    disable_breakers_ext : bool
        Indicates that /enable_software_runstop topic wants the breakers to be
        disabled (i.e. enable the software runstop).
        Set by /enable_topic_callback; disabled by update().
    desired_breaker_states : dict of bools
        Stores the desired breaker state (True = on) for all breakers being
        controlled.
    """
    def __init__(self, arm, base, gripper, tele):
        if not any([arm, base, gripper]):
            raise ValueError("SoftwareRunstop invoked without any "
                    "breakers to be controlled.")

        self._check_robot_components()

        self.desired_breaker_states = {}
        if arm and self._has_arm:
            self.desired_breaker_states["/arm_breaker"] = True
        if base and self._has_base:
            self.desired_breaker_states["/base_breaker"] = True
        # Gripper requiring arm is same assumption used in drivers
        if gripper and self._has_arm:
            self.desired_breaker_states["/gripper_breaker"] = True
        self.tele = tele

        # Booleans; See class docstring
        self.hw_runstop_has_been_pressed = False
        self.sw_runstop_enabled = False
        self.hw_runstop_state = False
        # These two store whether we want to enable/disable breakers
        self.enable_breakers = False
        self.disable_breakers = False
        self.disable_breakers_tele = False
        self.disable_breakers_ext = False

    def _check_robot_components(self):
        """Check ROS params"""
        self._has_arm = rospy.get_param('robot_driver/has_arm', False)
        self._has_base = rospy.get_param('robot_driver/has_base', False)

    def setup_and_run(self):
        """Connect to topics and start running software runstop"""
        # Buttons
        self.deadman_button_a = rospy.get_param(
                "~deadman_button_a", 11) # default is top right trigger
        self.deadman_button_b = rospy.get_param(
                "~deadman_button_b", 9) # default is bottom right trigger 

        # Subscribers
        self.robot_state_sub = rospy.Subscriber(
                "/robot_state", RobotState, self.robot_state_callback)
        self.enable_sub = rospy.Subscriber(
                "/enable_software_runstop", Bool, self.enable_topic_callback)
        if self.tele:
            self.joy_sub = rospy.Subscriber("/joy", Joy, self.joy_callback)

        # Publisher to topic /software_runstop_enabled
        self.pub = rospy.Publisher(
                "/software_runstop_enabled", Bool, queue_size=1)

        # Run
        self.r = rospy.Rate(10)
        self.run_node()


    def joy_callback(self, msg):
        """Callback for Joy messages published by teleop"""
        try:
            if (msg.buttons[self.deadman_button_a] > 0 and
                    msg.buttons[self.deadman_button_b] > 0):
                self.disable_breakers_tele = True
            else:
                self.disable_breakers_tele = False
        except KeyError:
            rospy.logwarn("deadman_button values may be out of range")


    def enable_topic_callback(self, msg):
        """Callback for requests to enable software runstop"""
        if msg.data:
            self.disable_breakers_ext = True
        else:
            self.enable_breakers = True


    def robot_state_callback(self, msg):
        """Check hardware runstop status if software runstop is enabled"""
        if msg.runstopped:
            self.hw_runstop_state = True
        else:
            self.hw_runstop_state = False


    def update(self):
        """Primary logic for enabling/disabling software runstop

        Logic uses five booleans to track controller and runstop and the
        next step to take. In normal operation, everything is False:

        - self.hw_runstop_has_been_pressed
        - self.sw_runstop_enabled
        - self.hw_runstop_state
        - self.enable_breakers
        - self.disable_breakers
        """
        # Handle external inputs that can disable breakers
        if self.disable_breakers_ext or self.disable_breakers_tele:
            self.disable_breakers = True
            self.disable_breakers_ext = False
            self.disable_breakers_tele = False
            # Want to disable breakers
            for breaker in self.desired_breaker_states:
                self.desired_breaker_states[breaker] = False
        else:
            # Want to enable breakers
            for breaker in self.desired_breaker_states:
                self.desired_breaker_states[breaker] = True

        # If want to disable breakers and sw runstop not already active
        if self.disable_breakers and not self.sw_runstop_enabled:
            # Disable the breakers; software runstop is active
            if all(self.set_breaker(breaker, val) for breaker, val in
                    self.desired_breaker_states.items()):
                self.disable_breakers = False
                self.sw_runstop_enabled = True
        # If receive disable signal and software runstop is already active,
        elif self.disable_breakers and self.sw_runstop_enabled:
            # Clear disable_breakers and also enable_breakers
            self.disable_breakers = False
            self.enable_breakers = False
        # Elif want to enable breakers and software runstop is enabled
        # and hw runstop is not currently engaged
        elif self.enable_breakers and self.sw_runstop_enabled and \
                not self.hw_runstop_state:
            # No longer want software runstop; turn breakers back on
            if all(self.set_breaker(breaker, val) for breaker, val in
                    self.desired_breaker_states.items()):
                self.enable_breakers = False
                self.sw_runstop_enabled = False
        # If software runstopped, and waiting for hw runstop to be toggled
        elif self.sw_runstop_enabled:
            # If hw runstop is currently pressed
            if self.hw_runstop_state:
                self.hw_runstop_has_been_pressed = True
            # Else if hw runstop is released and was previously pressed since
            # software runstop was activated
            elif self.hw_runstop_has_been_pressed:
                self.enable_breakers = True
                self.hw_runstop_has_been_pressed = False
            # Else continue waiting for hw runstop action
        # Clear enable_breakers if software runstop already disabled
        elif not self.sw_runstop_enabled and self.enable_breakers:
            self.enable_breakers = False
        # Not actively disabling or enabling breaker, or waiting for hw runstop
        else:
            pass


    def run_node(self):
        """Run update function and publish software runstop state"""
        while not rospy.is_shutdown():
            self.update()
            self.pub.publish(self.sw_runstop_enabled)
            # For debugging if issues arise with an invalid state, etc.
            #print("{}\t{}\t{}\t{}\t{}".format(self.enable_breakers, self.disable_breakers, self.sw_runstop_enabled, self.hw_runstop_state, self.hw_runstop_has_been_pressed))
            self.r.sleep()


    def set_breaker(self, service_name, enable):
        """Toggle a breaker via power_msgs service

        Returns
        -------
        bool
            False if a service call failed. Otherwise True.
        """
        rospy.loginfo("Software runstop waiting for %s service...", service_name)
        rospy.wait_for_service(service_name)
        try:
            breaker = rospy.ServiceProxy(service_name, BreakerCommand)
            resp = breaker(enable)
            rospy.loginfo("Server sent response : \n" + str(resp))
        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: %s" % e)
            return False
        return True


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-a", "--arm", action="store_true",
                        help="Software runstop will disable arm breaker.")
    parser.add_argument("-b", "--base", action="store_true",
                        help="Software runstop will disable base breaker.")
    parser.add_argument("-g", "--gripper", action="store_true",
                        help="Software runstop will disable gripper breaker.")
    parser.add_argument("-t", "--tele", action="store_true", help="Allow "
                        "controller to trigger software runstop.")

    args, unknown = parser.parse_known_args()

    rospy.init_node("software_runstop")
    c = SoftwareRunstop(args.arm, args.base, args.gripper, args.tele)
    c.setup_and_run()

    rospy.spin()
