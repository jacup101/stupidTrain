'''
Student Author Name: Campbell Gilbert
Group Name: Team Sanrio
Project 1
Fall 2022
COMP 313: Computer Graphics
Professor Schiffer
'''

import numpy as np
import math
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------
#1. SETUP
def car_end(plt, ax, carTop, carBottom, carGround):
    #x-coordinates
    #End of "main" car section
    sectEnd = 202

    #Beginning of this section, end of green section
    sectStart = 180

    #--------------------------------------------------------------------------
    #2. HELPER FUNCTION/S
    def draw_circle(xc=20, yc=20, r=50, circColor='red', deg1=0, deg2=360, width=1):
        p1 = deg1*np.pi/180
        p2 = deg2*np.pi/180
        dp = (p2-p1)/100
        xlast = xc+r*np.cos(p1)
        ylast = yc+r*np.sin(p1)
        for p in np.arange(p1, p2+dp, dp):
            x = xc+r*np.cos(p)
            y = yc+r*np.sin(p)
            plt.plot([xlast, x], [ylast, y], linewidth = width, color=circColor)
            xlast = x 
            ylast = y
    #--------------------------------------------------------------------------
    #3. ACTUAL CODE/DRAWING FUNCTIONS

    #Lines on back of car
    def backOfCarLines(carTop, carBottom, sectEnd):
        lineTop = carTop + 1
        lineBottom = carBottom - .5
        i = .5
        while i < 2.5:
            #lines
            plt.plot([sectEnd + i, sectEnd + i], [lineTop, lineBottom], color='pink')
            
            #arcs between lines
            xc = sectEnd + (i - .25)
            r = .25
            angleT1 = 0
            angleT2 = -180
            draw_circle(xc, lineTop, r, 'pink', angleT1, angleT2)

            angleB1 = 0
            angleB2 = 180
            draw_circle(xc, lineBottom, r, 'pink', angleB1, angleB2)

            i += .5

        #Thick line between car and back-thingy
        plt.plot([sectEnd, sectEnd], [lineTop, lineBottom + .25], linewidth=2.5, color='pink')
        plt.plot([sectEnd, sectEnd], [carTop, carBottom], linewidth=1, color='pink')

    #top section of car 
    def topOfCar(sectStart, sectEnd, carTop):
        #Top of the car, below the hook
        plt.plot([sectStart, sectEnd], [carTop, carTop], color='pink')
        plt.plot([sectStart, sectEnd], [carTop + 1, carTop + 1], color='pink')
        plt.plot([sectStart, sectEnd], [carTop + 3, carTop + 3], color='pink')
        plt.plot([sectStart, sectEnd], [carTop + 5, carTop + 5], color='pink')
        plt.plot([sectStart, sectEnd], [carTop + 7, carTop + 7], color='pink')

    #hook on top
    def hook(sectStart, sectEnd, carTop):
        #Left lines on first portion
        startPointXL = sectStart + 8.5
        endPointXL = startPointXL + 6.8
        endPointYL = carTop - 3.4

        realEndPointXL = endPointXL - .2
        #Outer
        plt.plot([startPointXL, realEndPointXL], [carTop, endPointYL - .4], color='pink')
        #Inner
        plt.plot([startPointXL + 1, realEndPointXL + .8], [carTop, endPointYL], color='pink')

        #Right lines on first portion
        startPointXR = startPointXL + 6
        endPointXR = endPointXL + 4
        endPointYR = endPointYL + 1

        plt.plot([startPointXR, endPointXR], [carTop, endPointYR], color='pink')
        plt.plot([startPointXR - 1.3, endPointXR - 1.5], [carTop, endPointYR], color='pink')

        #Upper lines on second portion
        startPointXR = endPointXR
        startPointYR = endPointYR
        endPointXR = startPointXR - 12
        endPointYR = startPointYR - 6.5

        plt.plot([startPointXR, endPointXR], [startPointYR, endPointYR], color='pink')
        plt.plot([startPointXR - 1.5, endPointXR], [startPointYR, endPointYR + 1], color='pink')

        #Lower lines on second portion -- SAME ANGLE AS ABOVE
        endPointYL = endPointYR + 1.6
        startPointXL = endPointXR + 7
        startPointYL = endPointYL + 3.9

        plt.plot([startPointXL, endPointXR], [startPointYL, endPointYL], color='pink')
        plt.plot([startPointXL - .55, endPointXR], [startPointYL + .4, endPointYL + .6], color='pink')

        #Straight lines at end of hook
        lineYs = [endPointYR + 1, endPointYL, endPointYL + .6]
        hookLineXStart = endPointXR - 1.9
        for y in lineYs:
            plt.plot([endPointXR, endPointXR - 1.9], [y, y], color='pink')

        #Topmost one is a tiny bit shorter
        plt.plot([endPointXR, endPointXR - 1.5], [endPointYR, endPointYR], color='pink')

        #End of the hook
        #topmost bit:
        topHookXStart = endPointXR - 1.5
        hookLineEndY = endPointYR - 1
            #vert
        plt.plot([topHookXStart, topHookXStart], [endPointYR, endPointYR - 1], color='pink')
            #horiz
        plt.plot([topHookXStart, topHookXStart - 1.5], [endPointYR - 1, endPointYR - 1], color='pink')
            #vert down
        plt.plot([topHookXStart - 1.5, topHookXStart - 1.5], [endPointYR - 1, endPointYR + .5], color='pink')

        #second bit:
        hookLineXStart = endPointXR - 1.9
        startY = lineYs[0]
        endY = startY - 1.5

            #vert
        plt.plot([hookLineXStart, hookLineXStart], [startY, endY], color='pink')
            #horiz
        plt.plot([hookLineXStart, hookLineXStart - .8], [endY, endY], color='pink')
            #vert down
        plt.plot([hookLineXStart - .8, hookLineXStart - .8], [endY, endPointYR + .5], color='pink')
            #connecting horiz line to prev section
        plt.plot([topHookXStart - 1.5, hookLineXStart - .8], [endPointYR + .5, endPointYR + .5], color='pink')

        lineXHolder = hookLineXStart - .8

        #third bit: 
            #vert line goes to "top" and ends section
        plt.plot([hookLineXStart - .4, hookLineXStart - .4], [startY, endY], color='pink')
            #diagonal connecting line
        plt.plot([hookLineXStart, hookLineXStart - .4], [lineYs[1], startY], color='pink')

        #fourth bit: 
            #vertical line, .5 X/.2 Y from prev vert line
        plt.plot([hookLineXStart - .8, hookLineXStart - .8], [startY + .2, endY], color='pink')
            #diagonal connecting line

        plt.plot([hookLineXStart, hookLineXStart - .8], [lineYs[2], startY + .2], color='pink')

    #window
    def window(sectStart, sectEnd, carBottom):
        #Window
        windowLeft = sectStart + 3
        windowRight = sectEnd - 3

            #2 V lines below the bottom of the "top" lines, maybe 3 units in and 1 unit down
        plt.plot([windowLeft + 1, windowLeft + 1], [carTop + 7, carTop + 8], color='pink')
        plt.plot([windowRight - 1, windowRight - 1], [carTop + 7, carTop + 8], color='pink')

            #2 H lines conecting to above 2 lines, 1 unit outward
        plt.plot([windowLeft + 1, windowLeft], [carTop + 8, carTop + 8], color='pink')
        plt.plot([windowRight - 1, windowRight], [carTop + 8, carTop + 8], color='pink')
        
            #2 main window lines -- from just below above H-lines to about...3-5 U above top "bottom" line
        plt.plot([windowLeft, windowLeft], [carTop + 8, carBottom -  10], color='pink')
        plt.plot([windowRight, windowRight], [carTop + 8, carBottom -  10], color='pink')

            #Window bottom -- just a flat line
        plt.plot([windowLeft + .5, windowRight - .5], [carBottom -  9.5, carBottom -  9.5], color='pink')

            #2 arcs connecting window bottom to window sides
        #draw_circle(xc, yc, r, color, angle1, angle2)
        
        xc1 = windowLeft + .5
        xc2 = windowRight - .5
        angleR1 = 0
        angleR2 = 90
        yc = carBottom - 10 #window bottom + .5
        r = .5
        angleL1 = 90
        angleL2 = 180
        draw_circle(xc1, yc, r, 'pink', angleL1, angleL2)
        draw_circle(xc2, yc, r, 'pink', angleR1, angleR2)

    #Keroppi in window :)
    def frog(sectStart, sectEnd, carBottom, carTop):
        windowLeft = sectStart + 3
        windowRight = sectEnd - 3
        windowBottom = carBottom - 9.5
        windowTop = carTop + 7

        #face
        faceMiddle = (windowLeft + windowRight) / 2
        xc = faceMiddle
        ycFace = windowBottom - 7
        r = 4
        angle1 = -30
        angle2 = 210
        draw_circle(xc, ycFace, r, 'green', angle1, angle2, 1.5)
        #face = plt.Circle((xc, ycFace), 300, color='green')
        #plt.scatter(xc, ycFace, s=3000, color='green')

        #left eye
        xcL = xc - 1.9
        yc = windowBottom - 10
        r = 1.9
        angle1 = 0
        angle2 = 360
        draw_circle(xcL, yc, r, 'black', angle1, angle2, 2)
            #pupil
        plt.scatter(xcL + .8, yc, s=100, color='black')

        #right eye
        xcR = xc + 1.9
        angle1 = 0
        angle2 = 360
        draw_circle(xcR, yc, r, 'black', angle1, angle2, 2)
            #pupil
        plt.scatter(xcR - .8, yc, s=100, color='black')

        #left cheek
        yCheek = yc + 4
        xCheekL = xc - 2.5
        plt.scatter(xCheekL, yCheek, s=150, color='pink')
        
        #right cheek
        yCheek = yc + 4
        xCheekR = xc + 2.5
        plt.scatter(xCheekR, yCheek, s=150, color='pink')

        #mouth
        faceBottom = ycFace + 4
        plt.plot([faceMiddle, faceMiddle + 1.5], [faceBottom, faceBottom - 1.5], color='black')
        plt.plot([faceMiddle, faceMiddle - 1.5], [faceBottom, faceBottom - 1.5], color='black')
        
        #body
        plt.plot([faceMiddle + 3, faceMiddle + 3.5], [faceBottom - 1.2, windowBottom], color='blue')
        plt.plot([faceMiddle - 3, faceMiddle - 3.5], [faceBottom - 1.2, windowBottom], color='blue')
        plt.plot([faceMiddle + 3.1, faceMiddle - 3.1], [faceBottom + .5, faceBottom + .5], linewidth = 3, color='blue')
        plt.plot([faceMiddle + 3.3, faceMiddle - 3.3], [faceBottom + 2, faceBottom + 2], linewidth = 3, color='blue')
        
    #bottom section of car, including bottom "box"
    def bottomOfCar(sectStart, sectEnd, carBottom):
        #Bottom of car, above the wheels

        plt.plot([sectStart, sectEnd], [carBottom - 5, carBottom - 5], color='pink')
        plt.plot([sectStart, sectEnd], [carBottom - 2.2, carBottom - 2.2], color='pink')
        plt.plot([sectStart, sectEnd], [carBottom - 1.6, carBottom - 1.6], color='pink')
        
        plt.plot([sectStart, sectEnd], [carBottom - 5, carBottom - 5], color='pink')
        plt.plot([sectStart, sectEnd], [carBottom - 2.2, carBottom - 2.2], color='pink')
        plt.plot([sectStart, sectEnd], [carBottom - 1.6, carBottom - 1.6], color='pink')
        plt.plot([sectStart, sectEnd], [carBottom - 1, carBottom - 1], color='pink')
        plt.plot([sectStart, sectEnd], [carBottom, carBottom], color='pink')

        #Box thingy on very bottom
            #Vertical lines making up "sides" of "box"
        plt.plot([sectStart + 7, sectStart + 7], [carBottom, carGround - 1], color='pink')
        plt.plot([sectEnd - 7, sectEnd - 7], [carBottom, carGround - 1], color='pink')

            #Horizontal line at bottom of "box"
        plt.plot([sectStart + 7, sectEnd - 7], [carGround - 1, carGround - 1], color='pink')

    #Wheels
    def wheels(sectStart, sectEnd, carBottom):
        xc1 = sectStart + 3
        xc2 = sectEnd - 3
        yc = carBottom - .5
        r = 2.5
        draw_circle(xc1, yc, r, 'pink', 15, 165)
        draw_circle(xc2, yc, r, 'pink', 15, 165)


    #--------------------------------------------------------------------------
    #4. CALLING CODE FUNCTIONS
    backOfCarLines(carTop, carBottom, sectEnd)
    topOfCar(sectStart, sectEnd, carTop)
    hook(sectStart, sectEnd, carTop)
    window(sectStart, sectEnd, carBottom)
    frog(sectStart, sectEnd, carBottom, carTop)
    bottomOfCar(sectStart, sectEnd, carBottom)
    wheels(sectStart, sectEnd, carBottom)

    #just for cleanliness' sake, line in front of car as well
    plt.plot([sectStart, sectStart], [carTop, carBottom], linewidth=1, color='pink')
