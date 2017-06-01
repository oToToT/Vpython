from visual import *
BOX = box(pos=(0,1,0), length=10, height=0.1,width=10, axis=(1,1,0))
BALL = sphere(pos=(BOX.pos+BOX.axis*5), radius=0.5)
