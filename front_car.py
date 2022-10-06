import numpy as np
import matplotlib.pyplot as plt

#params
car_bounds = [10, 40]

def front_car(plt, axes, car_top, car_bottom, car_ground):
    car_sketch(plt, axes, car_top, car_bottom, car_ground)
    car_body(plt, axes, car_top, car_bottom, car_ground)
    wheels(plt, axes, car_top, car_bottom, car_ground)
    
def car_sketch(plt, axes, car_top, car_bottom, car_ground):
    
    x = [car_bounds[0], car_bounds[1], car_bounds[1], car_bounds[0], car_bounds[0]]
    y = [car_top, car_top, car_bottom, car_bottom, car_top]
    
    plt.plot(x, y, linewidth = 1, color = 'gray')
    
def wheels(plt, axes, car_top, car_bottom, car_ground):
    wheel_offset = 6
    wheel_width = 1.5
    
    plt.plot(car_bounds[0])
    
    x1c = car_bounds[0] + wheel_offset
    x2c = car_bounds[1] - wheel_offset
    x1 = [x1c, x1c + wheel_width, x1c + wheel_width, x1c, x1c]
    x2 = [x2c, x2c - wheel_width, x2c - wheel_width, x2c, x2c]
    y = [car_bottom, car_bottom, car_ground, car_ground, car_bottom]
    
    plt.plot(x1, y, linewidth = 1, color = 'k')
    plt.plot(x2, y, linewidth = 1, color = 'k')
    
def car_body(plt, axes, car_top, car_bottom, car_ground):
    yc = (car_top + car_bottom) / 2
    
    bottom_offset = 3
    side_offset = 2
    
    xb = [car_bounds[0] + bottom_offset, car_bounds[1] - bottom_offset]
    yb = [car_bottom, car_bottom]
    
    plt.plot(xb, yb, linewidth = 1, color = 'k')
    plt.plot([car_bounds[0], car_bounds[0]], [car_bottom - side_offset, yc], linewidth = 1, color = 'k')
    plt.plot([car_bounds[1], car_bounds[1]], [car_bottom - side_offset, yc], linewidth = 1, color = 'k')
    
    body_details(plt, axes, car_top, car_bottom, car_ground, side_offset)

def body_details(plt, axes, car_top, car_bottom, car_ground, side_offset):
    
    sep1 = 0.75
    sep2 = 2.5
    
    light_offset = 0.5
    light_width = 5
    light_sep = 3
    light_height = 2
    
    x = [car_bounds[0], car_bounds[1]]
    y = np.array([car_bottom - side_offset, car_bottom - side_offset])
    
    plt.plot(x, y, linewidth = 1, color = 'k')
    y = y - sep1
    plt.plot(x, y, linewidth = 1, color = 'k')
    y = y - sep1
    plt.plot(x, y, linewidth = 1, color = 'k')
    y = y - sep2
    plt.plot(x, y, linewidth = 1, color = 'k')
    y = y - sep1
    plt.plot(x, y, linewidth = 1, color = 'k')
    y = y - sep1
    
    xl1c = car_bounds[0] + light_offset
    xl2c = car_bounds[1] - light_offset
    yc = y[0]
    
    xl1 = [xl1c, xl1c, xl1c + light_width, xl1c + light_width, xl1c]
    xl2 = [xl2c, xl2c, xl2c - light_width, xl2c - light_width, xl2c]
    yl = [yc, yc - light_height, yc - light_height, yc, yc]
    
    plt.plot(xl1, yl, linewidth = 1, color = 'k')
    plt.plot(xl2, yl, linewidth = 1, color = 'k')
    plt.plot([xl1c + light_sep, xl1c + light_sep], [yc, yc - light_height], linewidth = 1, color = 'k')
    plt.plot([xl2c - light_sep, xl2c - light_sep], [yc, yc - light_height], linewidth = 1, color = 'k')