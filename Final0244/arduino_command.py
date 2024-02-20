#!/usr/bin/env python3
from tkinter import *
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import String
from std_srvs.srv import Empty

root = Tk()
root.geometry("300x300")

rospy.init_node('arduino_command')
rate = rospy.Rate(10)
rate.sleep()
pubs0 = rospy.Publisher("s0", Int16, queue_size = 10)
pubs1 = rospy.Publisher("s1", Int16, queue_size = 10)
pubs2 = rospy.Publisher("s2", Int16, queue_size = 10)
pubs3 = rospy.Publisher("s3", Int16, queue_size = 10)

def read1(num):
    sensor_read = num.data
    if(sensor_read == 1):{
        pubs1.publish()
    }
    else:{
        pubs0.publish()
    }
sub1 = rospy.Subscriber("Topic_s1", Int16, callback = read1)

def read2(num):
    sensor_read = num.data
    pubs2.publish()
sub1 = rospy.Subscriber("Topic_s2" , Int16, callback = read2)

def read3(num):
    sensor_read = num.data
    pubs3.publish()
sub1 = rospy.Subscriber("Topic_s3", Int16, callback = read3)


def reset_tur():
    print("Reset")
    rospy.wait_for_service('/reset')  # รอให้บริการ "reset" พร้อมใช้งาน
    try:
        reset_service = rospy.ServiceProxy('/reset', Empty)
        response = reset_service()
        rospy.loginfo("Reset Turtlesim Service Response: %s", response)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == "__main__":
    # sub = rospy.Subscriber("ch1", String, callback=run_motion)

    ActLabel = Label(text="Motion", font=("", 18))
    ActLabel.place(x=113, y=10)

    ActOut = Text(root, height=7, width=10, bg="light cyan", font=("", 16))
    ActOut.place(x=83, y=50)

    ClearBtn = Button(root, height=1, width=10, text="Clear", command=reset_tur)
    ClearBtn.place(x=103, y=250)


    root.mainloop()