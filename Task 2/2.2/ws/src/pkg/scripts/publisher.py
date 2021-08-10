#!/usr/bin/env python3.8
import rospy
from std_msgs.msg import String, Int32

def talker():
    rospy.init_node('node1')
    pub = rospy.Publisher('topic', String, queue_size=10)
    rate = rospy.Rate(1)
    num = 0
    while not rospy.is_shutdown():
        #hello_str = "hello world"
        num = num + 1
        rospy.loginfo(str(num))
        pub.publish(str(num))
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass