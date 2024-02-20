#!/usr/bin/env python3

import rospy
from tkinter import*
from std_msgs.msg import Int16
from geometry_msgs.msg import Twist
from std_msgs.msg import String


frame = Tk()
frame.title("REMOTE")
frame.geometry("500x500") # ขนาดของ frame

rospy.init_node("Turtle_control") #สร้างโนดชื่อ GUI_Remote
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10) #ส่งไปที่เต่า
pubtesx = rospy.Publisher("ch1",String, queue_size=10) #ส่งไปที่เต่า

def fw():
    print("fw")
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z=0.0
    pub.publish(cmd)
sub1 = rospy.Subscriber("Topic_s0", Int16, callback = fw)

def bw():
    print("bw")
    cmd = Twist()
    cmd.linear.x = -1.0
    cmd.angular.z=0.0
    pub.publish(cmd)
sub1 = rospy.Subscriber("Topic_s1", Int16, callback = bw)


pubon = rospy.Publisher("Topic_led",Int16, queue_size=10) #ส่งไปที่เต่า
def Pen_on():
    print("Pen_on")
    # response = setpen_service()
    # rospy.loginfo("Reset Turtlesim Service Response: %s", response)
    # setpen_service = rospy.ServiceProxy('/turtle1/set_pen')
    pubon.publish(1)

puboff = rospy.Publisher("Topic_led",Int16, queue_size=10) #ส่งไปที่เต่า
def Pen_off():
    print("Pen_off")
    # t = StringVar()
    # t.penup()
    puboff.publish(0)

def rol():
    print("rotate L")
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= 1.0
    cmd.linear.y = 0.0
    pub.publish(cmd)
sub2 = rospy.Subscriber("Topic_s2", Int16, callback = rol)


def ror():
    print("rotate R")
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= -1.0
    cmd.linear.y = 0.0
    pub.publish(cmd)
sub3 = rospy.Subscriber("Topic_s3", Int16, callback = ror)


# def reset_tur():
#     print("Reset")
#     rospy.wait_for_service('/reset')  # รอให้บริการ "reset" พร้อมใช้งาน
#     try:
#         reset_service = rospy.ServiceProxy('/reset', Empty)
#         response = reset_service()
#         rospy.loginfo("Reset Turtlesim Service Response: %s", response)
#     except rospy.ServiceException as e:
#         rospy.logerr("Service call failed: %s", e)

B1 = Button(text = "Forward", command= fw, bg="#4F80C0") #โครงสร้างปุ่ม โดยเรียกไปที่ฟังก์ชั่น
B1.place(x=73, y=20)                 #ตำแหน่ง

B2 = Button(text = "Backward", command= bw)
B2.place(x=73, y=130)

B5 = Button(text = "Turn Left", command= rol)
B5.place(x=20, y=80)

B6 = Button(text = "Turn Right", command= ror)
B6.place(x=128, y=80)


B4 = Button(text = "Pen on", command= Pen_on)
B4.place(x=300, y=80)

B7 = Button(text = "Pen off", command=Pen_off)
B7.place(x=300, y=130)

frame.mainloop()