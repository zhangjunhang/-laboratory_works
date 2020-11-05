#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import *

def forward():
	returns

def make_moves():
	rospy.init_node('move_turtle', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(1)
	vel = Twist()

	vel.linear.x = 0
	vel.linear.y = 0
	vel.linear.z = 0

	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = 0
	#2
	for x in range(3):
		vel.linear.x = 0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	for i in range(1):
		vel.angular.z = -90 * 3.14 / 180
		pub.publish(vel)
		rate.sleep()
	vel.angular.z = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.x = 0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	for i in range(1):
		vel.angular.z = -45 * 3.14 / 180
		pub.publish(vel)
		rate.sleep()
	vel.angular.z = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.x = 0.3
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	for i in range(1):
		vel.angular.z = 135 * 3.14 / 180
		pub.publish(vel)
		rate.sleep()
	vel.angular.z = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.x = 0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	killTurtle('turtle1')
	spawnTurtle(5.544445+1, 5.544445, 0, 'turtle1')
	#8
	for x in range(3):
		vel.linear.x = 0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.y = -0.5
		pub.publish(vel)
		rate.sleep()
	vel.linear.y = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.x = -0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.y = 0.5
		pub.publish(vel)
		rate.sleep()
	vel.linear.y = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.y = -0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.y = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.x = 0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)




	killTurtle('turtle1')
	spawnTurtle(5.544445+2, 5.544445, 0, 'turtle1')

	for j in range(2):
		for x in range(3):
			vel.linear.x = 0.25
			pub.publish(vel)
			rate.sleep()
		vel.linear.x = 0
		pub.publish(vel)

		for i in range(1):
			vel.angular.z = -90 * 3.14 / 180
			pub.publish(vel)
			rate.sleep()
		vel.angular.z = 0
		pub.publish(vel)

		for x in range(3):
			vel.linear.x = 0.5
			pub.publish(vel)
			rate.sleep()
		vel.linear.x = 0
		pub.publish(vel)

		for i in range(1):
			vel.angular.z = -90 * 3.14 / 180
			pub.publish(vel)
			rate.sleep()
		vel.angular.z = 0
		pub.publish(vel)

	killTurtle('turtle1')
	spawnTurtle(5.544445+3, 5.544445, 0, 'turtle1')

	for x in range(3):
		vel.linear.x = 0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	for i in range(1):
		vel.angular.z = -90 * 3.14 / 180
		pub.publish(vel)
		rate.sleep()
	vel.angular.z = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.x = 0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	for i in range(1):
		vel.angular.z = -45 * 3.14 / 180
		pub.publish(vel)
		rate.sleep()
	vel.angular.z = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.x = 0.3
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	for i in range(1):
		vel.angular.z = 135 * 3.14 / 180
		pub.publish(vel)
		rate.sleep()
	vel.angular.z = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.x = 0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	killTurtle('turtle1')
	spawnTurtle(5.544445+4, 5.544445, 0, 'turtle1')
	# 6
	for x in range(3):
		vel.linear.x = 0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.x = -0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.y = -0.5
		pub.publish(vel)
		rate.sleep()
	vel.linear.y = 0
	pub.publish(vel)

	for k in range(3):
		for x in range(3):
			vel.linear.x = 0.25
			pub.publish(vel)
			rate.sleep()
		vel.linear.x = 0
		pub.publish(vel)

		for i in range(1):
			vel.angular.z = 90 * 3.14 / 180
			pub.publish(vel)
			rate.sleep()
		vel.angular.z = 0
		pub.publish(vel)

	killTurtle('turtle1')
	spawnTurtle(5.544445+5, 5.544445, 0, 'turtle1')
	# 4
	for x in range(3):
		vel.linear.y = -0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.y = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.x = 0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	pub.publish(vel)

	for x in range(3):
		vel.linear.y = -0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.y = 0
	pub.publish(vel)

	for x in range(6):
		vel.linear.y = 0.25
		pub.publish(vel)
		rate.sleep()
	vel.linear.y = 0
	pub.publish(vel)


def move_forvard(vel, pub, rate, n):
	for i in range(n):
		vel.linear.x = 1
		pub.publish(vel)
		rate.sleep()
	vel.linear.x = 0
	return vel, pub

def rotate(vel, pub, angle):
	vel.angular.z = angle * 3.14 / 180
	pub.publish(vel)
	vel.angular.z = 0
	return vel, pub


if __name__ == "__main__":
	try:
		spawnTurtle = rospy.ServiceProxy('/spawn', Spawn)
		killTurtle = rospy.ServiceProxy('/kill', Kill)
		make_moves()
	except rospy.ROSInterruptException:
		pass

