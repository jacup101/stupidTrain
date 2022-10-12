'''
Student Author Name: Bryce Joseph
Group Name: Team Sanrio
Project 1
Fall 2022
COMP 313: Computer Graphics
Professor Schiffer
'''

from random import randint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pltp
import math

#parameters
car_bounds = [6, 36] #car body definition
color = 'pink' #line colors

#class constructor
def front_car(plt, axes, car_top, car_bottom, car_ground):
    kitty(plt, axes, car_top, car_bottom, car_ground)
    car_body(plt, axes, car_top, car_bottom, car_ground)
    wheels(plt, axes, car_top, car_bottom, car_ground)
    flowers(plt, axes, car_top, car_bottom, car_ground)
    
def car_body(plt, axes, car_top, car_bottom, car_ground):
    #y center of car
    yc_main = (car_top + car_bottom) / 2
    
    #x and y offset of bottom corners of car
    xoffset = 4
    yoffset = 2
    
    #car bottom
    xb = [car_bounds[0] + xoffset, car_bounds[1] - xoffset]
    yb = [car_bottom, car_bottom]
    plt.plot(xb, yb, linewidth = 1, color = color)
    
    #car sides (lines)
    plt.plot([car_bounds[0], car_bounds[0]], [car_bottom - yoffset, yc_main], linewidth = 1, color = color)
    plt.plot([car_bounds[1], car_bounds[1]], [car_bottom - yoffset, yc_main], linewidth = 1, color = color)
    
    #car bottom corners
    p1 = (car_bounds[0], car_bottom - yoffset)
    p2 = (car_bounds[0] + xoffset, car_bottom)
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    xc = p2[0]
    yc = p1[1]
    ellipse(xc, yc, a, b, 270, 360, half = 1)
    
    xc = car_bounds[1] - xoffset
    yc = car_bottom - yoffset
    ellipse(xc, yc, a, b, 0, 90, half = 1)
    
    #car head parameters
    box_top = car_top + 3.5
    box_bottom = box_top + 3
    yoffset = 1.5
    
    #car sides (arcs)
    p1 = (car_bounds[0], yc_main)
    p2 = (car_bounds[0] + yoffset, box_bottom)
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    xc = p2[0]
    yc = p1[1]
    ellipse(xc, yc, a, b, 90, 180)
    
    p1 = (car_bounds[1], yc_main)
    p2 = (car_bounds[1] - yoffset, box_bottom)
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    xc = p2[0]
    yc = p1[1]
    ellipse(xc, yc, a, b, 10, 90)
    
    #functions that depend of car head parameters
    body_details(plt, axes, car_top, car_bottom, car_ground, yoffset)
    car_head(plt, axes, car_top, car_bottom, car_ground, box_top, box_bottom, yoffset)
    windows(plt, axes, car_top, car_bottom, car_ground, box_bottom)
    
def wheels(plt, axes, car_top, car_bottom, car_ground):
    #x offset and width of wheels
    x_offset = 6
    wheel_width = 1.5
    
    #wheels
    x1c = car_bounds[0] + x_offset
    x2c = car_bounds[1] - x_offset
    x1 = [x1c, x1c + wheel_width, x1c + wheel_width, x1c, x1c]
    x2 = [x2c, x2c - wheel_width, x2c - wheel_width, x2c, x2c]
    y = [car_bottom, car_bottom, car_ground, car_ground, car_bottom]
    
    plt.plot(x1, y, linewidth = 1, color = color)
    plt.plot(x2, y, linewidth = 1, color = color)

def flowers(plt, axes, car_top, car_bottom, car_ground):
    #flowers
    add_flower(plt, axes, 7.3, 33.3, radius = 0.3, color = 'r')
    add_flower(plt, axes, 10.2, 35, radius = 0.75, color = 'b')
    add_flower(plt, axes, 14, 33.5, radius = 0.35, color = 'pink')
    add_flower(plt, axes, 14.25, 37.5, radius = 0.9, color = 'purple')
    add_flower(plt, axes, 17.5, 34, radius = 0.75, color = 'r')
    add_flower(plt, axes, 18.2, 37.5, radius = 0.6, color = 'b')
    add_flower(plt, axes, 22.26, 35.3, radius = 0.9, color = 'pink')
    add_flower(plt, axes, 26.3, 37.7, radius = 0.5, color = 'purple')
    add_flower(plt, axes, 23.2, 38.3, radius = 0.4, color = 'r')
    add_flower(plt, axes, 27.6, 34.2, radius = 0.9, color = 'b')
    add_flower(plt, axes, 32.2, 35.8, radius = 0.5, color = 'pink')
    add_flower(plt, axes, 34.4, 33.8, radius = 0.4, color = 'purple')

def body_details(plt, axes, car_top, car_bottom, car_ground, side_offset):
    #separations between front car lines
    sep1 = 0.75
    sep2 = 2.5
    
    #headlight parameters
    light_offset = 0.5
    light_width = 5
    light_sep = 3
    light_height = 2
    
    #lines
    x = [car_bounds[0], car_bounds[1]]
    y = np.array([car_bottom - side_offset - sep1, car_bottom - side_offset - sep1])
    
    plt.plot(x, y, linewidth = 1, color = color)
    y = y - sep1
    plt.plot(x, y, linewidth = 1, color = color)
    y = y - sep1
    plt.plot(x, y, linewidth = 1, color = color)
    y = y - sep2
    plt.plot(x, y, linewidth = 1, color = color)
    y = y - sep1
    plt.plot(x, y, linewidth = 1, color = color)
    y = y - sep1
    
    #lights
    xl1c = car_bounds[0] + light_offset
    xl2c = car_bounds[1] - light_offset
    yc = y[0]
    
    xl1 = [xl1c, xl1c, xl1c + light_width, xl1c + light_width, xl1c]
    xl2 = [xl2c, xl2c, xl2c - light_width, xl2c - light_width, xl2c]
    yl = [yc, yc - light_height, yc - light_height, yc, yc]
    
    plt.plot(xl1, yl, linewidth = 1, color = color)
    plt.fill(xl1, yl, color = 'yellow')
    plt.plot(xl2, yl, linewidth = 1, color = color)
    plt.fill(xl2, yl, color = 'yellow')
    plt.plot([xl1c + light_sep, xl1c + light_sep], [yc, yc - light_height], linewidth = 1, color = color)
    
    plt.plot([xl2c - light_sep, xl2c - light_sep], [yc, yc - light_height], linewidth = 1, color = color)
    
def car_head(plt, axes, car_top, car_bottom, car_ground, box_top, box_bottom, side_offset):  
    #car head sides (lines)  
    x1 = [car_bounds[0] +  side_offset, car_bounds[0] +  side_offset]
    x2 = [car_bounds[1] -  side_offset, car_bounds[1] -  side_offset]
    y = [box_top, box_bottom]
    
    plt.plot(x1, y, linewidth = 1, color = color)
    plt.plot(x2, y, linewidth = 1, color = color)
    
    #ellipses
    #cap (top ellipse)
    p1 = (x1[0], y[0])
    p2 = (x2[0], y[0])
    b = car_top - box_top
    xc = (p2[0] + p1[0]) / 2
    a = p2[0] - xc
    yc = y[0]
    ellipse(xc, yc, a, b, 0 , 180)
    
    #sub-cap (ellipse below top)
    p1 = (x1[0], y[1])
    p2 = (x2[0], y[1])
    b = (car_top - box_top) / 1
    xc = (p2[0] + p1[0]) / 2
    a = p2[0] - xc
    yc = y[1]
    ellipse(xc, yc, a, b)
    
def windows(plt, axes, car_top, car_bottom, car_ground, box_bottom):
    #vertical center of car
    yc_main = (car_top + car_bottom) / 2
    
    #separation between windows and horizontal offset
    sep = 0.5
    side_offset = 3.5
    
    #starting window positions
    x = [car_bounds[0] + side_offset, car_bounds[1] - side_offset]
    y = np.array([yc_main + 0.5 + (sep * 2), yc_main + 0.5 + (sep * 2)])
    
    #loop that creates 3 windows, changing the positions by sep each loop
    for i in range(3):
        #bottom lines
        plt.plot(x, y, linewidth = 1, color = color)
    
        #window sides
        x1 = [x[0], x[0] + sep * 2]
        x2 = [x[1], x[1] - sep * 2]
        y1 = [y[0], box_bottom - (sep * 3)]
        plt.plot(x1, y1, linewidth = 1, color = color)
        plt.plot(x2, y1, linewidth = 1, color = color)
    
        #window 1 top
        p1 = (x1[1], y1[1])
        p2 = (x2[1], y1[1])
        b = sep * 3
        xc = (p2[0] + p1[0]) / 2
        a = p2[0] - xc
        yc = y1[1]
        ellipse(xc, yc, a, b, 0 , 180)
        
        #move window by step
        x[0] += sep
        x[1] -= sep
        y -= sep

def kitty(plt, axes, car_top, car_bottom, car_ground):
    #horizontal and vertical center of kitty head
    xc = (car_bounds[0] + car_bounds[1]) / 2
    yc = 26
    
    #kitty body
    axes.add_artist(pltp.Ellipse((xc, 30), 4.5, 6, color = 'b')) #kitty overalls
    axes.add_artist(pltp.Ellipse((21, 28.5), 2, 1.25, color = 'r')) #kitty shirt
    
    #white rectangle to override bottom of kitty body
    x = (car_bounds[0], car_bounds[0], car_bounds[1], car_bounds[1], car_bounds[0])
    y = (31, 33, 33, 31, 31)
    axes.add_artist(pltp.Rectangle((car_bounds[0], 33), car_bounds[1] - car_bounds[0], -2, color = 'white'))
    
    #white ellipse to override top of kitty body
    a = xc / 6
    b = 2.5
    axes.add_artist(pltp.Ellipse((xc, yc), a * 2, b * 2, color = 'white'))
    
    #arcs to define kitty head (there are separations in the top arc to make way for the ears)
    ellipse(xc, yc, a, b, theta1 = 0, theta2 = 30, color = 'k')
    ellipse(xc, yc, a, b, theta1 = 60, theta2 = 120,  color = 'k') 
    ellipse(xc, yc, a, b, theta1 = 150, theta2 = 180,  color = 'k')
    ellipse(xc, yc, a, b, half = 1, color = 'k')
    
    #left ear
    xc = 18.25
    yc = 23.7
    a = 19.7 - xc
    b = (24.7 - 23) / 2
    ellipse(xc, yc, a, b, theta1 = 0, theta2 = 90, color = 'k')
    
    a = 0.5
    ellipse(xc, yc, a, b, theta1 = 90, theta2 = 180, color = 'k')
    ellipse(xc, yc, a, b, theta1 = 100, theta2 = 180, half = 1, color = 'k')
    
    #right ear
    xc = 23.7
    yc = 23.7
    a = xc - 22.3
    
    ellipse(xc, yc, a, b, theta1 = 90, theta2 = 190, color = 'k')

    a = 0.5
    ellipse(xc, yc, a, b, theta1 = 0, theta2 = 90, color = 'k')
    ellipse(xc, yc, a, b, theta1 = 0, theta2 = 80, half = 1, color = 'k')
    
    #eyes and nose offsets
    eye_offset = 2
    nose_offset = 1
    
    xc = (car_bounds[0] + car_bounds[1]) / 2
    yc = 26
    
    axes.add_artist(pltp.Ellipse((xc - eye_offset, yc + 0.25), 0.4, 0.6, color = 'k'))
    axes.add_artist(pltp.Ellipse((xc + eye_offset, yc + 0.25), 0.4, 0.6, color = 'k'))
    axes.add_artist(pltp.Ellipse((xc, yc + nose_offset), 0.7, 0.4, color = 'y'))
    
    #left whiskers
    x1 = np.array([17.75, 17])
    x2 = np.array([17.75, 17.25])
    x3 = np.array([18, 17.5])
    y1 = (yc, yc + 0.1)
    y2 = (yc + 0.5, yc + 0.7)
    y3 = (yc + 1, yc + 1.25)
    plt.plot(x1, y1, linewidth = 1, color = 'k')
    plt.plot(x2, y2, linewidth = 1, color = 'k')
    plt.plot(x3, y3, linewidth = 1, color = 'k')
    
    #right whiskers
    add = 7
    x1 += add + 0.25
    x2 += add
    x3 += add - 0.5
    plt.plot([x1[1], x1[0]], y1, linewidth = 1, color = 'k')
    plt.plot([x2[1], x2[0]], y2, linewidth = 1, color = 'k')
    plt.plot([x3[1], x3[0]], y3, linewidth = 1, color = 'k')
    
    #bow
    axes.add_artist(pltp.Ellipse((23, 24.25), 1, 1, color = 'r'))
    axes.add_artist(pltp.Ellipse((22.3, 23.7), 1.2, 1.5, 30, color = 'r'))
    axes.add_artist(pltp.Ellipse((23.7, 24.7), 1.2, 1.5, 30, color = 'r'))
    
#functions    

#draws an elliptical arc (half of an ellipse) centered at (xc, yc) with major axis a and minor axis b
#half specificies what half of the ellipse (-1 for top, 1 for bottom)
def ellipse(xc, yc, a, b, theta1 = 0, theta2 = 180, density = 300, half = -1, color = color):
    #convert angles to radians and get step based on density
    p1 = np.radians(theta1)
    p2 = np.radians(theta2)
    dp = (p2 - p1) / density
    
    xplast = a
    yplast = 0
    
    for p in np.arange(p1, p2 + dp, dp):
        #if statements guards against div by 0
        if (np.tan(p) != 0):
            xp = np.abs(a * b / np.sqrt(math.pow(b, 2) + (math.pow(a, 2) * math.pow(np.tan(p), 2))))
            yp = np.abs(a * b / np.sqrt(math.pow(a, 2) + math.pow(b, 2) * (1 / math.pow(np.tan(p), 2))))
            if p > np.pi / 2:
                xp = -xp
            if p1 < p < p2:
                plt.plot([xc + xplast, xc + xp], [yc + (half * yplast), yc + (half * yp)], linewidth = 1, color = color)
            #update xplast and yplast
            xplast = xp
            yplast = yp

#FLOWER CODE PROVIDED BY JOSH
def add_flower(plt, axes, xc, yc, radius, color):
    """
    Adds a flower to a given location
    :param plt: matplotlib plot instance
    :param axes: axes of plot subplot
    :param xc: center x coordinate
    :param yc: center y coordinate
    :param radius: radius of the center and leaves
    :param color: color of the leaves
    :returns: None
    """
    # Order: top leaf, bot leaf, left top, left bot, right top, right bot
    xdiff = [0, 0, 0, 0, -radius, -radius, radius, radius]
    ydiff = [0, 0, -radius, radius, -radius/2, radius/2, -radius/2, radius/2]
    for i in range(len(xdiff)):
        axes.add_artist(plt.Circle((xc + xdiff[i], yc + ydiff[i]), radius, color=color))
    center = plt.Circle((xc, yc), radius, color='yellow')
    axes.add_artist(center)