#!/usr/bin/env python


import rospy
import pyros_test

##############################################################################
# Main
##############################################################################


if __name__ == '__main__':
    rospy.init_node('pyros_test_echo')
    node = pyros_test.EchoNode()
    node.spin()


