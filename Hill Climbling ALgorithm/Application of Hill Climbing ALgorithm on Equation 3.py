# e^(-(x*x+y*y))

import numpy as np
import matplotlib.pyplot as plot
import math

#sin=math.sin
#cos=math.cos
exp=math.exp

x=np.arange(-1.5, 2, 0.05)
y=np.arange(-1.5, 2, 0.05)
z=x*x+y*y
z=-1*z
z=exp(z)


plot.plot(x,z)
plot.show()

move=0.0005
lower_bound=0
upper_bound=2500

def func(x,y):
    #one global maxima
    z=x*x+y*y
    z=-1*z
    z=exp(z)
    return z
    
def derivative(x,y):
    d=x*x+y*y
    d=-1*d
    d=exp(d)
    d=-2*x*d
    delta_x=d
    return x+ (move*delta_x)

def hill_climb(fun ,x, y, next_move):
    currentx,currenty =x,y
    while True:
        current_val=func(currentx, currenty)
        next =next_move(current)
        if func(next)>current_val:
            current=next
            print(current,current_val)
        else:
            if func(next)>upper_bound:
                current=next
            if func(next)<lower_bound:
                current=next
            break;
            
startx=0.8
starty=0.8

hill_climb(func, startx, starty, derivative)