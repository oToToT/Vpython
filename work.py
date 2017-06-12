#!/usr/bin/env python2
from visual import *
def getColor(a, b, c):
	return (a/255, b/255, c/255)
def deg2rad(a):
	return acos(-1)*a/180
scene = display(x=0, y=0, width=600, height=600, background=(0,0,0), center=(0,0,0))

BOARD_theta = 60
BOARD_Theta = deg2rad(BOARD_theta)
BOARD_Length = 5

BOXES = [box(pos=(BOARD_Length*cos(BOARD_Theta/2),BOARD_Length*sin(BOARD_Theta/2),0), length=BOARD_Length*2, height=0.1, width=2, axis=(1, 1*tan(BOARD_Theta/2), 0)),
	box(pos=(BOARD_Length*cos(BOARD_Theta/2),-1*BOARD_Length*sin(BOARD_Theta/2),0), length=BOARD_Length*2, height=0.1, width=2, axis=(1, -1*tan(BOARD_Theta/2), 0))]
text(text="%d degree"%BOARD_theta, pos=(-10,10,0), color=getColor(255.,0.,255.), height=0.5)

Lights_N = 24
Lights = [sphere(pos=(4,0,0), radius=0.01, color=getColor(255.,255.,0.), theta=deg2rad(360/Lights_N*(_+0.5)), make_trail=True) for _ in range(Lights_N)]
Reflects = []

t, dt = 0, 0.01
while True:
	rate(1/dt)
	for Light in  Reflects:
		if abs(Light.pos.x) <= 10 and abs(Light.pos.y) <= 10:
			Light.pos -= vector(cos(Light.theta), sin(Light.theta), 0)*dt
	for Light in Lights:
		if abs(Light.pos.x) <= 10 and abs(Light.pos.y) <= 10:
			Light.pos -= vector(cos(Light.theta), sin(Light.theta), 0)*dt
			for BOX in BOXES:
				a, b, c=BOX.axis.y/BOX.axis.x, -1, BOX.pos.y-(BOX.axis.y/BOX.axis.x)*BOX.pos.x
				dis = abs(a*Light.x+b*Light.y+c) / sqrt(a*a+b*b)
				if dis <= Light.radius*2:
					BOX_theta = atan(BOX.axis.y/BOX.axis.x)
					Light.theta = 2*(BOX_theta + acos(-1)) - Light.theta
					Reflects.append(sphere(pos=Light.pos, radius=0.01, color=getColor(255.,255.,255.), theta=Light.theta+acos(-1), make_trail=True))
					Reflects[-1].pos.x-=cos(Light.theta)*dt*2
					Reflects[-1].pos.y-=sin(Light.theta)*dt*2
