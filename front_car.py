import numpy as np
import matplotlib.pyplot as plt

def front_car(plt, car_top, car_bottom, car_ground):
    car_bounds = [10, 40]
    
    x = [car_bounds[0], car_bounds[1], car_bounds[1], car_bounds[0], car_bounds[0]]
    y = [car_top, car_top, car_bottom, car_bottom, car_top]
    
    plt.plot(x, y, color = 'k')
    plt.fill(x, y, color = 'gray')