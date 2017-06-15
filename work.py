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
ddg = text(text="%f degree"%BOARD_theta, pos=(-10,10,0), color=getColor(255.,0.,255.), height=0.5)

Lights_N = 24
Lights_pos = vector(4,0,0)
Lights = [sphere(pos=Lights_pos, radius=0.01, color=getColor(255.,255.,0.), theta=deg2rad(360/Lights_N*(_+0.5)), make_trail=True) for _ in range(Lights_N)]
Reflects = []
BALL = sphere(pos=Lights_pos, radius=0.1, color=getColor(255.,255.,0.))

pre=0
down=False
pause = False

def DOWN(evt):
	global down, pre, pause
	down=True
	pre=evt.pos.y
	pause = True
def CHANGE(evt):
	global pre, BOARD_theta, BOARD_Theta, BOXES, ddg
	if down:
		BOARD_theta+= (evt.pos.y-pre)*10
		if BOARD_theta < 0:
			BOARD_theta=0
		elif BOARD_theta > 180:
			BOARD_theta=180
		ddg.visible=False
		for _ in BOXES:
			_.visible=False
		BOARD_Theta = deg2rad(BOARD_theta)
		BOXES = [box(pos=(BOARD_Length*cos(BOARD_Theta/2),BOARD_Length*sin(BOARD_Theta/2),0), length=BOARD_Length*2, height=0.1, width=2, axis=(1, 1*tan(BOARD_Theta/2), 0)), box(pos=(BOARD_Length*cos(BOARD_Theta/2),-1*BOARD_Length*sin(BOARD_Theta/2),0), length=BOARD_Length*2, height=0.1, width=2, axis=(1, -1*tan(BOARD_Theta/2), 0))]
		ddg = text(text="%f degree"%BOARD_theta, pos=(-10,10,0), color=getColor(255.,0.,255.), height=0.5)
		pre=evt.pos.y
def UP():
	global down, pre, pause, Lights, Lights_N, Reflects, Lights_pos
	down=False
	pause=False
	for _ in Reflects:
		_.trail_object.visible=False
		_.visible=False
	Reflects=[]
	for _ in Lights:
		_.trail_object.visible=False
		_.visible=False
	Lights = [sphere(pos=Lights_pos, radius=0.01, color=getColor(255.,255.,0.), theta=deg2rad(360/Lights_N*(_+0.5)), make_trail=True) for _ in range(Lights_N)]
def changeLight(evt):
	global Lights_pos, pause, Reflects, Lights, BALL
	if not pause:
		for _ in Reflects:
			_.trail_object.visible=False
			_.visible=False
		Reflects=[]
		for _ in Lights:
			_.trail_object.visible=False
			_.visible=False	
	pause=True
	if evt.key=='left':
		Lights_pos.x-=0.1
	elif evt.key=='right':
		Lights_pos.x+=0.1
	elif evt.key=='up':
		Lights_pos.y+=0.1
	elif evt.key=='down':
		Lights_pos.y-=0.1
	else:
		return
	BALL.visible=False
	BALL = sphere(pos=Lights_pos, radius=0.1, color=getColor(255.,255.,0))
def renderLight(evt):
	global Lights, Lights_N, Reflects, pause
	pause=False
	Lights = [sphere(pos=Lights_pos, radius=0.01, color=getColor(255.,255.,0.), theta=deg2rad(360/Lights_N*(_+0.5)), make_trail=True) for _ in range(Lights_N)]
scene.bind('mousedown', DOWN)
scene.bind('mousemove', CHANGE)
scene.bind('mouseup', UP)
scene.bind('keydown', changeLight)
scene.bind('keyup', renderLight)

t, dt = 0, 0.01
while True:
    rate(3/dt)
    if pause:
	  continue
    for Light in  Reflects:
	  if abs(Light.pos.x) <= 10 and abs(Light.pos.y) <= 10:
		Light.pos -= vector(cos(Light.theta), sin(Light.theta), 0)*dt
    for Light in Lights:
	  if abs(Light.pos.x) <= 10 and abs(Light.pos.y) <= 10:
		Light.pos -= vector(cos(Light.theta), sin(Light.theta), 0)*dt
		for BOX in BOXES:
		    a, b, c=BOX.axis.y/BOX.axis.x, -1, BOX.pos.y-(BOX.axis.y/BOX.axis.x)*BOX.pos.x
		    dis = abs(a*Light.x+b*Light.y+c) / sqrt(a*a+b*b)
		    if dis <= Light.radius*2.5:
			  BOX_theta = atan(BOX.axis.y/BOX.axis.x)
			  Light.theta = 2*(BOX_theta + acos(-1)) - Light.theta
			  Reflects.append(sphere(pos=Light.pos, radius=0.01, color=getColor(255.,255.,255.), theta=Light.theta+acos(-1), make_trail=True))
			  Reflects[-1].pos.x-=cos(Light.theta)*dt*2
			  Reflects[-1].pos.y-=sin(Light.theta)*dt*2
