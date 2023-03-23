# x*sin(x*x)

import numpy as np
import matplotlib.pyplot as plot
import math

#sin=math.sin
#cos=math.cos
#exp=math.exp

x=np.arange(-1.5, 2, 0.05)
y=x*(np.sin(x*x))

plot.plot(x,y)
plot.show()

move=0.0005

def func(x):
    #one global maxima
    return x*(np.sin(x*x))
    
def derivative(x):
    delta_x=(np.sin(x*x))+2*(x*x)*(np.cos(x*x))
    return x+ (move*delta_x)

def hill_climb(fun ,x, next_move):
    current =x
    while True:
        current_val=func(current)
        next =next_move(current)
        if func(next)>current_val:
            current=next
            print(current,current_val)
        else:
            break;

            
start=0.8

hill_climb(func, start, derivative)