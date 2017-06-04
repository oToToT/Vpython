from visual import *
def getColor(a, b, c):
	return (a/255, b/255, c/255)
def deg2rad(a):
	return acos(-1)*a/180
BOX = box(pos=(0,0,0), length=20, height=0.1, width=2, axis=(10,1,0))

Light = sphere(pos=(-5,3,0), radius=0.01, color=getColor(255,255,0), theta=deg2rad(150), make_trail=True)

t, dt = 0, 0.01
while True:
	rate(1/dt)
	Light.pos -= vector(cos(Light.theta), sin(Light.theta), 0)*dt
	a, b, c=BOX.axis.y/BOX.axis.x, -1, BOX.pos.y-(BOX.axis.y/BOX.axis.x)*BOX.pos.x
	dis = abs(a*Light.x+b*Light.y+c) / sqrt(a*a+b*b)
	if dis <= Light.radius:
		BOX_theta = atan(BOX.axis.y/BOX.axis.x)
		Light.theta = BOX_theta+acos(-1)/2-(Light.theta - BOX_theta - acos(-1)/2)+acos(-1)
