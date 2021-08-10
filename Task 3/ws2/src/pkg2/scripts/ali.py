#!/usr/bin/env python3.8
import rospy
from std_msgs.msg import String, Int32

def message(msg):
    rospy.loginfo("Ali Heard %s", msg.data)

def main():
    rospy.init_node("Ali")
    rospy.Subscriber('question', String, message) 
    
    pub = rospy.Publisher('answer2', String, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        hello_str = "my number is 2222"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass