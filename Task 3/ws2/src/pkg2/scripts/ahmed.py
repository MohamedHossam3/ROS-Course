#!/usr/bin/env python3.8
import rospy
from std_msgs.msg import String, Int32

def answer1(msg):
    rospy.loginfo("Said answered %s", msg.data)

def answer2(msg):
    rospy.loginfo("Ali answered %s", msg.data)

def main():
    rospy.init_node('Ahmed')
    pub = rospy.Publisher('question', String, queue_size=10)
    rate = rospy.Rate(1)

    rospy.Subscriber('answer1', String, answer1)
    rospy.Subscriber('answer2', String, answer2)

    while not rospy.is_shutdown():
        hello_str = "Ahmed Asks, What is your number ?"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass