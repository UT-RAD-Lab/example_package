#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def callback(msg):
    rospy.loginfo(msg.data)

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.Subscriber('chatter', String, callback)
    rospy.init_node('combo')
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pub.publish("Hi")
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
