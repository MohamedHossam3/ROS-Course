#!/usr/bin/env python3.8
import rospy
from std_msgs.msg import String, Int32

def message(msg):
    rospy.loginfo("I Heard %s", msg.data)

def listener():
    rospy.init_node("node2")
    rospy.Subscriber('topic', String, message) 
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass