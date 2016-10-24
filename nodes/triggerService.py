#!/usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerResponse

confirm_msg = "trigger received"


def handle_msg(rq):
    print("Trigger Node got request")
    return TriggerResponse(success=True, message=confirm_msg)


def trigger_server():
    rospy.init_node('trigger_node')
    rospy.set_param('/test/confirm_param', confirm_msg)
    srv = rospy.Service('/test/trgsrv', Trigger, handle_msg)
    rospy.spin()
    if rospy.has_param('/test/confirm_param'):
        rospy.delete_param('/test/confirm_param')


if __name__ == '__main__':
    trigger_server()
