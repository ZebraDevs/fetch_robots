#!/usr/bin/python

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

# Primarily unit tests logic of the update function. Run tests with nosetests
# from the scripts/ directory.

# Standard Library
import unittest

# Fetch
from software_runstop import SoftwareRunstop


def stub_set_breaker(*args):
    # For current tests, assume breaker was set successfully
    return True
# Use stub to replace set_breaker()
SoftwareRunstop.set_breaker = stub_set_breaker

def stub_check_robot_components(self):
    # Current tests of init don't test robot components configuration
    self._has_arm = True
    self._has_base = True
# Use stub to replace _check_robot_components()
SoftwareRunstop._check_robot_components = stub_check_robot_components


class TestInit(unittest.TestCase):

    def test_no_breakers(self):
        self.assertRaises(ValueError, SoftwareRunstop,
                          False, False, False, True)

    def test_arg_arm(self):
        c = SoftwareRunstop(True, False, False, False)
        self.assertEqual(c.desired_breaker_states,
                {"/arm_breaker": True})

    def test_arg_base(self):
        c = SoftwareRunstop(False, True, False, False)
        self.assertEqual(c.desired_breaker_states,
                {"/base_breaker": True})

    def test_arg_gripper(self):
        c = SoftwareRunstop(False, False, True, False)
        self.assertEqual(c.desired_breaker_states,
                {"/gripper_breaker": True})


class TestUpdate(unittest.TestCase):

    def setUp(self):
        self.c = SoftwareRunstop(True, True, True, True)

    def assert_default_state(self):
        self.assertFalse(self.c.hw_runstop_has_been_pressed)
        self.assertFalse(self.c.hw_runstop_state)
        self.assertFalse(self.c.sw_runstop_enabled)
        self.assertFalse(self.c.enable_breakers)
        self.assertFalse(self.c.disable_breakers)
        self.assertFalse(self.c.disable_breakers_tele)
        self.assertFalse(self.c.disable_breakers_ext)

    def test_all_params_false(self):
        # Make sure params used in TestUpdate are initially False as expected
        self.assert_default_state()

    def test_tele_pressed_released_pressed(self):
        # Receive disable request, process and 
        self.c.disable_breakers_tele = True
        self.c.update()
        self.assertFalse(self.c.disable_breakers)
        self.assertTrue(self.c.sw_runstop_enabled)
        # Next pass: no new disable signal from tele, expect no change
        self.c.update()
        self.assertFalse(self.c.disable_breakers)
        self.assertTrue(self.c.sw_runstop_enabled)
        # Next pass: button pressed again, but still no change
        self.c.disable_breakers_tele = True
        self.c.update()
        self.assertFalse(self.c.disable_breakers)
        self.assertTrue(self.c.sw_runstop_enabled)

    def test_disable_breaker_topic_received(self):
        # Receive disable request, process and 
        self.c.disable_breakers_ext = True
        self.c.update()
        self.assertFalse(self.c.disable_breakers)
        self.assertTrue(self.c.sw_runstop_enabled)
        # Next pass: no new disable signal from tele, expect no change
        self.c.update()
        self.assertFalse(self.c.disable_breakers)
        self.assertTrue(self.c.sw_runstop_enabled)
        # Next pass: button pressed again, but still no change
        self.c.disable_breakers_tele = True
        self.c.update()
        self.assertFalse(self.c.disable_breakers)
        self.assertTrue(self.c.sw_runstop_enabled)

    def test_sw_runstop_released_by_hw_runstop(self):
        self.c.sw_runstop_enabled = True
        # Hardware runstop gets pressed
        self.c.hw_runstop_state = True
        self.c.update()
        self.assertTrue(self.c.hw_runstop_has_been_pressed)
        self.assertTrue(self.c.hw_runstop_state)
        self.assertTrue(self.c.sw_runstop_enabled)
        # and then released. Takes two updates before breakers re-enabled
        self.c.hw_runstop_state = False
        self.c.update()
        self.assertFalse(self.c.hw_runstop_has_been_pressed)
        self.assertFalse(self.c.hw_runstop_state)
        self.assertTrue(self.c.sw_runstop_enabled)
        self.assertTrue(self.c.enable_breakers)
        # The second update will enable breakers
        self.c.update()
        self.assert_default_state()

    def test_default_state_hw_runstop_no_effect(self):
        self.c.hw_runstop_state = True
        self.c.update()
        self.assertTrue(self.c.hw_runstop_state)
        self.assertFalse(self.c.hw_runstop_has_been_pressed)
        self.assertFalse(self.c.sw_runstop_enabled)
        self.assertFalse(self.c.enable_breakers)
        self.assertFalse(self.c.disable_breakers)

    def test_activate_sw_runstop_when_hw_runstopped(self):
        # We allow the sw runstop to be enabled while hardware runstop
        # This allows user to holde sw runstop button(s) on controller
        # while releasing the hw runstop, and then enable the breakers
        # after e.g. moving away from robot.
        self.c.hw_runstop_state = True
        self.c.disable_breakers = True
        self.c.update()
        self.assertTrue(self.c.hw_runstop_state)
        self.assertTrue(self.c.sw_runstop_enabled)
        self.assertFalse(self.c.hw_runstop_has_been_pressed)
        self.assertFalse(self.c.disable_breakers)
        # next update will count the hw runstop as having been pressed
        self.c.update()
        self.assertTrue(self.c.hw_runstop_state)
        self.assertTrue(self.c.hw_runstop_has_been_pressed)
        self.assertTrue(self.c.sw_runstop_enabled)

    def test_enable_breakers_works(self):
        # This test is currently redundant
        self.c.sw_runstop_enabled = True
        self.c.enable_breakers = True # set e.g. by enable_topic_callback
        # Go back to default state after software runstop is no longer active
        self.c.update()
        self.assert_default_state()

