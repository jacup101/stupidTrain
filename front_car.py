import numpy as np
import matplotlib.pyplot as plt

<<<<<<< Updated upstream
def front_car(plt, axes, car_top, car_bottom, car_ground):
    car_bounds = [10, 40]
=======
car_bounds = [10, 40]

def front_car(plt, car_top, car_bottom, car_ground):
    car_body(plt, car_top, car_bottom, car_ground)
    
def car_body(plt, car_top, car_bottom, car_ground):
>>>>>>> Stashed changes
    
    x = [car_bounds[0], car_bounds[1], car_bounds[1], car_bounds[0], car_bounds[0]]
    y = [car_top, car_top, car_bottom, car_bottom, car_top]
    
    plt.plot(x, y, color = 'gray')
    
def wheels(plt, car_top, car_bottom, car_ground):
    wheel_offset = 20
    
    plt.plot(car_bounds[0])
    