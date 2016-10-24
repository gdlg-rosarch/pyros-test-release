#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse

delay = 30


def handle_msg(rq):
    print("Slow Node got request")
    rospy.rostime.wallsleep(delay)
    return EmptyResponse()


def empty_server():
    rospy.init_node('slow_node')
    rospy.set_param('~slow_param', delay)
    srv = rospy.Service('/test/slowsrv', Empty, handle_msg)
    rospy.spin()
    if rospy.has_param('slow_param'):
        rospy.delete_param('~slow_param')

if __name__ == '__main__':
    empty_server()
