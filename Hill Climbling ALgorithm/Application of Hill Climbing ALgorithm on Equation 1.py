# -x*x

import numpy as np
import matplotlib.pyplot as plot

x=np.arange(-10, 10, 0.005)
y=-x*x

plot.plot(x,y)
plot.show()

move=0.0005

def func(x):
    #one global maxima
    return -x*x
    
def derivative(x):
    delta_x=-2.0*x
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
            
start=-10

hill_climb(func, start, derivative)