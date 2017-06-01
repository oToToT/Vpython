from visual import *
N, dis=10, 0.5
Box = box(pos=vector(0,1,0), length=2*N, height=0.1, width=5, color=(1,1,1), axis=(10,1,0))
Light = []
Theta = []
for i in range(N):
	Light.append(sphere(pos=vector(i*dis,3,0), radius=0.05, color=(1,1,0), make_trail=True))
	Theta.append(-acos(-1)/4)
dt, t=0.01, 0
while True:
	rate(1/dt)
	for i in range(N):
		Light[i].pos+=dt*vector(cos(Theta[i]), sin(Theta[i]), 0)
		if abs(norm(Box.pos+Box.axis*200 - Light[i].pos)*1000 - norm(Box.axis)*1000) < 1e-3:
			print abs(norm(Box.pos+Box.axis*200 - Light[i].pos) - norm(Box.axis))
			Theta[i]=-Theta[i]
	t+=dt
