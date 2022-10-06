#Purple section -- by Campbell Gilbert

import numpy as np
import math
import matplotlib.pyplot as plt

"""
TODO
- top arm
- all arcs (back thingy, window bottom corners, wheels)
- bottom of car rectangle
- Keroppi in windowm (Sanrio theme)
"""


#--------------------------------------------------------------------------
#1. FUNCTIONS
def draw_arc(xc, yc, r, startAngle, endAngle):
    p1 = startAngle*np.pi/180
    p2 = endAngle*np.pi/180
    dp = (p2-p1)/100
    xlast = xc+r*np.cos(p1)
    ylast = yc+r*np.sin(p1)

    for p in np.arange(p1, p2, dp):
        x = xc+r*np.cos(p)
        y = yc+r*np.sin(p)
        plt.plot([xlast, x], [ylast, y], color='g')
        xlast = x
        ylast = y
    
    return

#--------------------------------------------------------------------------
#2. SETUP

#Setup graph 
""" 
plt.axis([170, 220, 60, 0])

plt.axis('on')
plt.grid(True)
plt.xticks(np.arange(170, 220, 10))
plt.yticks(np.arange(0, 60, 10))


#y-coordinates
carTop = 14
carBottom = 47
carGround = 49

"""

def car_end(plt, carTop, carBottom, carGround, fig, ax):

    #y-coordinates
    carTop = 14
    carBottom = 47
    carGround = 49

    #x-coordinates
    #End of "main" car section
    sectEnd = 202

    #Beginning of this section, end of green section
    sectStart = 180

    #--------------------------------------------------------------------------
    #3. ACTUAL CODE/DRAWINGS

    #Lines on back of car
    lineTop = carTop + 1
    lineBottom = carBottom - .5
    i = .5
    while i < 2.5:
        plt.plot([sectEnd + i, sectEnd + i], [lineTop, lineBottom], color='black')
        i += .5

    #Arcs between lines
    #FIXME


    #Thick line between car and back-thingy
    plt.plot([sectEnd, sectEnd],[lineTop, lineBottom + .25],linewidth=2, color='black')
    plt.plot([sectEnd, sectEnd],[carTop, carBottom],linewidth=1, color='black')


    #Top of the car, below the hook
    plt.plot([sectStart, sectEnd], [carTop, carTop], color='black')
    plt.plot([sectStart, sectEnd], [carTop + 1, carTop + 1], color='black')
    plt.plot([sectStart, sectEnd], [carTop + 3, carTop + 3], color='black')
    plt.plot([sectStart, sectEnd], [carTop + 5, carTop + 5], color='black')
    plt.plot([sectStart, sectEnd], [carTop + 7, carTop + 7], color='black')


    #Hook

    #Left lines on first portion
    startPointXL = sectStart + 8.5
    endPointXL = startPointXL + 6.8
    endPointYL = carTop - 3.4

    realEndPointXL = endPointXL - .2
    plt.plot([startPointXL, realEndPointXL], [carTop, endPointYL - .4], color='black')
    plt.plot([startPointXL + 1, realEndPointXL + .9], [carTop, endPointYL], color='black')

    #Right lines on first portion
    startPointXR = startPointXL + 6
    endPointXR = endPointXL + 4
    endPointYR = endPointYL + 1

    plt.plot([startPointXR, endPointXR], [carTop, endPointYR], color='black')
    plt.plot([startPointXR - 1.3, endPointXR - 1.5], [carTop, endPointYR], color='black')

    #Upper lines on second portion
    startPointXR = endPointXR
    startPointYR = endPointYR
    endPointXR = startPointXR - 12
    endPointYR = startPointYR - 6.5

    plt.plot([startPointXR, endPointXR], [startPointYR, endPointYR], color='black')
    plt.plot([startPointXR - 1.5, endPointXR], [startPointYR, endPointYR + 1], color='black')

    #Lower lines on second portion -- SAME ANGLE AS ABOVE
    startPointXL = 194.5
    startPointYL = 10.5
    endPointYL = endPointYR + 1.6

    plt.plot([startPointXL, endPointXR], [startPointYL, endPointYL], color='black')
    plt.plot([startPointXL - .5, endPointXR], [startPointYL + .4, endPointYL + .6], color='black')

    #Straight lines at end of hook
    lineYs = [endPointYR + 1, endPointYL, endPointYL + .6]
    hookLineXStart = endPointXR - 1.9
    for y in lineYs:
        plt.plot([endPointXR, endPointXR - 1.9], [y, y], color='black')

    #Topmost one is a tiny bit shorter
    plt.plot([endPointXR, endPointXR - 1.5], [endPointYR, endPointYR], color='black')

    #End of the hook
    #topmost bit:
    topHookXStart = endPointXR - 1.5
    hookLineEndY = endPointYR - 1
        #vert
    plt.plot([topHookXStart, topHookXStart], [endPointYR, endPointYR - 1], color='black')
        #horiz
    plt.plot([topHookXStart, topHookXStart - 1.5], [endPointYR - 1, endPointYR - 1], color='black')
        #vert down
    plt.plot([topHookXStart - 1.5, topHookXStart - 1.5], [endPointYR - 1, endPointYR + .5], color='black')

    #second bit:
    hookLineXStart = endPointXR - 1.9
    startY = lineYs[0]
    endY = startY - 1.5

        #vert
    plt.plot([hookLineXStart, hookLineXStart], [startY, endY], color='black')
        #horiz
    plt.plot([hookLineXStart, hookLineXStart - .8], [endY, endY], color='black')
        #vert down
    plt.plot([hookLineXStart - .8, hookLineXStart - .8], [endY, endPointYR + .5], color='black')
        #connecting horiz line to prev section
    plt.plot([topHookXStart - 1.5, hookLineXStart - .8], [endPointYR + .5, endPointYR + .5], color='black')

    lineXHolder = hookLineXStart - .8


    #third bit: 
        #vert line goes to "top" and ends section
    plt.plot([hookLineXStart - .4, hookLineXStart - .4], [startY, endY], color='black')
        #diagonal connecting line
    plt.plot([hookLineXStart, hookLineXStart - .4], [lineYs[1], startY], color='black')

    #fourth bit: 
        #vertical line, .5 X/.2 Y from prev vert line
    plt.plot([hookLineXStart - .8, hookLineXStart - .8], [startY + .2, endY], color='black')
        #diagonal connecting line
    plt.plot([hookLineXStart, hookLineXStart - .8], [lineYs[2], startY + .2], color='black')


    #Window
    windowLeft = sectStart + 3
    windowRight = sectEnd - 3

        #2 V lines below the bottom of the "top" lines, maybe 3 units in and 1 unit down
    plt.plot([windowLeft + 1, windowLeft + 1], [carTop + 7, carTop + 8], color='black')
    plt.plot([windowRight - 1, windowRight - 1], [carTop + 7, carTop + 8], color='black')

        #2 H lines conecting to above 2 lines, 1 unit outward
    plt.plot([windowLeft + 1, windowLeft], [carTop + 8, carTop + 8], color='black')
    plt.plot([windowRight - 1, windowRight], [carTop + 8, carTop + 8], color='black')
    
        #2 main window lines -- from just below above H-lines to about...3-5 U above top "bottom" line
    plt.plot([windowLeft, windowLeft], [carTop + 8, carBottom -  10], color='black')
    plt.plot([windowRight, windowRight], [carTop + 8, carBottom -  10], color='black')

        #Window bottom -- just a flat line
    plt.plot([windowLeft + .5, windowRight - .5], [carBottom -  9.5, carBottom -  9.5], color='black')

        #2 arcs connecting window bottom to window sides
    #FIXME




    #Bottom of car, above the wheels
    lineBottom = -48
    plt.plot([sectStart, sectEnd], [carBottom -  5, carBottom -  5], color='black')

    plt.plot([sectStart, sectEnd], [carBottom -  2.2, carBottom -  2.2], color='black')
    plt.plot([sectStart, sectEnd], [carBottom -  1.6, carBottom -  1.6], color='black')
    plt.plot([sectStart, sectEnd], [carBottom -  1, carBottom -  1], color='black')

    plt.plot([sectStart, sectEnd], [carBottom, carBottom], color='black')

    #Box thingy on very bottom

        #Vertical lines making up "sides" of "box"
    plt.plot([sectStart + 7, sectStart + 7], [carBottom, carGround - 1], color='black')
    plt.plot([sectEnd - 7, sectEnd - 7], [carBottom, carGround - 1], color='black')

        #Horizontal line at bottom of "box"
    plt.plot([sectStart + 7, sectEnd - 7], [carGround - 1, carGround - 1], color='black')


    #Wheels
        #FIXME

    #length of car / 3 = ~7
    #let's say box thingy is length 8, wheels are radius 6
    #leaves us with 1 unit in between wheels and box which looks right


    #Very bottom/ground
    #plt.plot([10, 210], [carGround, carGround], color='black')


    #plt.show()
