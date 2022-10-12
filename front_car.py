'''
Student Author Name: Bryce Joseph
Group Name: Team Sanrio
Project 1
Fall 2022
COMP 313: Computer Graphics
Professor Schiffer
'''

import numpy as np
import matplotlib.pyplot as plt
import math

#params
car_bounds = [6, 36]

def ellipse(xc, yc, a, b, theta1 = 0, theta2 = 180, density = 300, half = -1, color = 'k'):
    p1 = np.radians(theta1)
    p2 = np.radians(theta2)
    dp = (p2 - p1) / density
    
    xplast = a
    yplast = 0
    
    for p in np.arange(p1, p2 + dp, dp):
        if (np.tan(p) != 0):
            xp = np.abs(a * b / np.sqrt(math.pow(b, 2) + (math.pow(a, 2) * math.pow(np.tan(p), 2))))
            yp = np.abs(a * b / np.sqrt(math.pow(a, 2) + math.pow(b, 2) * (1 / math.pow(np.tan(p), 2))))
            if p > np.pi / 2:
                xp = -xp
            if p1 < p < p2:
                plt.plot([xc + xplast, xc + xp], [yc + (half * yplast), yc + (half * yp)], linewidth = 1, color = color)
            xplast = xp
            yplast = yp
    
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
    
    x1c = car_bounds[0] + wheel_offset
    x2c = car_bounds[1] - wheel_offset
    x1 = [x1c, x1c + wheel_width, x1c + wheel_width, x1c, x1c]
    x2 = [x2c, x2c - wheel_width, x2c - wheel_width, x2c, x2c]
    y = [car_bottom, car_bottom, car_ground, car_ground, car_bottom]
    
    plt.plot(x1, y, linewidth = 1, color = 'k')
    plt.plot(x2, y, linewidth = 1, color = 'k')
    
def car_body(plt, axes, car_top, car_bottom, car_ground):
    yc_main = (car_top + car_bottom) / 2
    
    bottom_offset = 4
    side_offset = 2
    
    xb = [car_bounds[0] + bottom_offset, car_bounds[1] - bottom_offset]
    yb = [car_bottom, car_bottom]
    
    plt.plot(xb, yb, linewidth = 1, color = 'k')
    plt.plot([car_bounds[0], car_bounds[0]], [car_bottom - side_offset, yc_main], linewidth = 1, color = 'k')
    plt.plot([car_bounds[1], car_bounds[1]], [car_bottom - side_offset, yc_main], linewidth = 1, color = 'k')
    
    #ellipses
    p1 = (car_bounds[0], car_bottom - side_offset)
    p2 = (car_bounds[0] + bottom_offset, car_bottom)
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    xc = p2[0]
    yc = p1[1]
    ellipse(xc, yc, a, b, 270, 360, half = 1)
    
    xc = car_bounds[1] - bottom_offset
    yc = car_bottom - side_offset
    ellipse(xc, yc, a, b, 0, 90, half = 1)
    
    #head ellipse
    box_top = car_top + 3.5
    box_bottom = box_top + 3
    side_offset = 1.5
    
    p1 = (car_bounds[0], yc_main)
    p2 = (car_bounds[0] + side_offset, box_bottom)
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    xc = p2[0]
    yc = p1[1]
    ellipse(xc, yc, a, b, 90, 180)
    
    p1 = (car_bounds[1], yc_main)
    p2 = (car_bounds[1] - side_offset, box_bottom)
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    xc = p2[0]
    yc = p1[1]
    ellipse(xc, yc, a, b, 10, 90)
    
    body_details(plt, axes, car_top, car_bottom, car_ground, side_offset)
    car_head(plt, axes, car_top, car_bottom, car_ground, box_top, box_bottom, side_offset)
    windows(plt, axes, car_top, car_bottom, car_ground, box_bottom)

def body_details(plt, axes, car_top, car_bottom, car_ground, side_offset):
    
    sep1 = 0.75
    sep2 = 2.5
    
    light_offset = 0.5
    light_width = 5
    light_sep = 3
    light_height = 2
    
    x = [car_bounds[0], car_bounds[1]]
    y = np.array([car_bottom - side_offset - sep1, car_bottom - side_offset - sep1])
    
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
    
def car_head(plt, axes, car_top, car_bottom, car_ground, box_top, box_bottom, side_offset):    
    x1 = [car_bounds[0] +  side_offset, car_bounds[0] +  side_offset]
    x2 = [car_bounds[1] -  side_offset, car_bounds[1] -  side_offset]
    y = [box_top, box_bottom]
    
    plt.plot(x1, y, linewidth = 1, color = 'k')
    plt.plot(x2, y, linewidth = 1, color = 'k')
    
    #ellipses
    p1 = (x1[0], y[0])
    p2 = (x2[0], y[0])
    b = car_top - box_top
    xc = (p2[0] + p1[0]) / 2
    a = p2[0] - xc
    yc = y[0]
    
    ellipse(xc, yc, a, b, 0 , 180)
    
    p1 = (x1[0], y[1])
    p2 = (x2[0], y[1])
    b = (car_top - box_top) / 1
    xc = (p2[0] + p1[0]) / 2
    a = p2[0] - xc
    yc = y[1]
    
    ellipse(xc, yc, a, b)
    
def windows(plt, axes, car_top, car_bottom, car_ground, box_bottom):
    yc_main = (car_top + car_bottom) / 2
    sep = 0.5
    side_offset = 3.5
    
    #bottom line 1
    x = [car_bounds[0] + side_offset, car_bounds[1] - side_offset]
    y = np.array([yc_main + 0.5 + (sep * 2), yc_main + 0.5 + (sep * 2)])
    plt.plot(x, y, linewidth = 1, color = 'k')
    
    #side lines 1
    x1 = [x[0], x[0] + sep * 2]
    x2 = [x[1], x[1] - sep * 2]
    y1 = [y[0], box_bottom - (sep * 3)]
    plt.plot(x1, y1, linewidth = 1, color = 'k')
    plt.plot(x2, y1, linewidth = 1, color = 'k')
    
    #elliptical arc 1
    p1 = (x1[1], y1[1])
    p2 = (x2[1], y1[1])
    b = sep * 3
    xc = (p2[0] + p1[0]) / 2
    a = p2[0] - xc
    yc = y1[1]
    ellipse(xc, yc, a, b, 0 , 180)
    
    #bottom line 2
    x[0] += sep
    x[1] -= sep
    y -= sep
    plt.plot(x, y, linewidth = 1, color = 'k')
    
    #side lines 2
    x1 = [x[0], x[0] + sep * 2]
    x2 = [x[1], x[1] - sep * 2]
    y1 = [y[0], box_bottom - (sep * 2)]
    plt.plot(x1, y1, linewidth = 1, color = 'k')
    plt.plot(x2, y1, linewidth = 1, color = 'k')
    
    #elliptical arc 2
    p1 = (x1[1], y1[1])
    p2 = (x2[1], y1[1])
    b = sep * 3
    xc = (p2[0] + p1[0]) / 2
    a = p2[0] - xc
    yc = y1[1]
    ellipse(xc, yc, a, b, 0 , 180)
    
    #bottom line 3
    x[0] += sep
    x[1] -= sep
    y -= sep
    plt.plot(x, y, linewidth = 1, color = 'k')
    
    #side lines 3
    x1 = [x[0], x[0] + sep * 2]
    x2 = [x[1], x[1] - sep * 2]
    y1 = [y[0], box_bottom - (sep * 1)]
    plt.plot(x1, y1, linewidth = 1, color = 'k')
    plt.plot(x2, y1, linewidth = 1, color = 'k')
    
    #elliptical arc 3
    p1 = (x1[1], y1[1])
    p2 = (x2[1], y1[1])
    b = sep * 3
    xc = (p2[0] + p1[0]) / 2
    a = p2[0] - xc
    yc = y1[1]
    ellipse(xc, yc, a, b, 0 , 180)