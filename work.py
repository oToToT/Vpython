from visual import *
Box = box(pos=vector(0,0,0), length=10, height=0.1, width=5, color=(1,1,1))
Light=sphere(pos=vector(2,3,0), radius=0.05, color=(1,1,0), make_trail=True)
Target_pos=vector(-3,0,0)
Theta = acos(dot(Light.pos-Target_pos, Box.axis-Target_pos)/abs(Light.pos-Target_pos)/abs(Box.axis-Target_pos))
dt=0.01
t=0
while True:
	rate(1/dt)
	Light.pos-=dt*vector(cos(Theta), sin(Theta), 0)
	if abs(Light.pos-Target_pos)<=0.005:
		Theta=-Theta
	t+=dt
