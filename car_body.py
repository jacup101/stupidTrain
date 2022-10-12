'''
Student Author Name: Cathy Yim
Group Name: Team Sanrio
Project 1
Fall 2022
COMP 313: Computer Graphics
Professor Schiffer
'''

import matplotlib.pyplot as plt
import numpy as np

carTop = 14
carBottom = 47
sectEnd = 178.5
sectStart = 93.5

# creates pink arcs
def arcPink(xc, yc, r, a1, a2):
    p1 = a1 * np.pi / 180
    p2 = a2 * np.pi / 180
    dp = (p2-p1)/100
    xlast = xc+r*np.cos(p1)
    ylast = yc+r*np.sin(p1)
    for p in np.arange(p1 + dp, p2, dp):
        x = xc + r * np.cos(p)
        y = yc + r * np.sin(p)
        plt.plot([xlast, x], [ylast, y], color='pink')
        xlast = x
        ylast = y

# creates black arcs
def arcBlack(xc, yc, r, a1, a2):
    p1 = a1 * np.pi / 180
    p2 = a2 * np.pi / 180
    dp = (p2-p1)/100
    xlast = xc+r*np.cos(p1)
    ylast = yc+r*np.sin(p1)
    for p in np.arange(p1 + dp, p2, dp):
        x = xc + r * np.cos(p)
        y = yc + r * np.sin(p)
        plt.plot([xlast, x], [ylast, y], color='black')
        xlast = x
        ylast = y

# adds flowers (code by josh)
def add_flower(plt, axes, xc, yc, radius, color):
    # Order: top leaf, bot leaf, left top, left bot, right top, right bot
    xdiff = [0, 0, 0, 0, -radius, -radius, radius, radius]
    ydiff = [0, 0, -radius, radius, -radius / 2, radius / 2, -radius / 2, radius / 2]
    for i in range(len(xdiff)):
        axes.add_artist(plt.Circle((xc + xdiff[i], yc + ydiff[i]), radius, color=color))
    center = plt.Circle((xc, yc), radius, color='yellow')
    axes.add_artist(center)

def linesSeperatingCars():
    lineTop = carTop + 1
    lineBottom = carBottom - .5
    # right most line
    plt.plot([sectEnd, sectEnd], [carTop, carBottom], color='pink')
    # line to the left of that
    plt.plot([sectEnd + .5, sectEnd + .5], [lineTop, lineBottom], color='pink')
    # line to the left of that
    plt.plot([sectEnd + 1, sectEnd + 1], [lineTop, lineBottom], linewidth=2, color='pink')
    # line to the left of that
    plt.plot([sectEnd + 1.5, sectEnd + 1.5], [lineTop, lineBottom], color='pink')
    # longer ine that expends from top of car to bottom of car
    plt.plot([sectStart, sectStart], [carTop, carBottom], color='pink')
    # arcs that connect the lines
    arcPink(sectEnd + .25, lineTop, 0.25, 180, 360)
    arcPink(sectEnd + .25, lineBottom, 0.25, 0, 180)
    arcPink(sectEnd + .75, lineTop, 0.25, 180, 360)
    arcPink(sectEnd + .75, lineBottom, 0.25, 0, 180)
    arcPink(sectEnd + 1.25, lineTop, 0.25, 180, 360)
    arcPink(sectEnd + 1.25, lineBottom, 0.25, 0, 180)

def lineOnTopOfCar():
    plt.plot([sectStart, sectEnd], [carTop, carTop], color='pink')
    plt.plot([sectStart, sectEnd], [carTop + 1, carTop + 1], color='pink')
    plt.plot([sectStart, sectEnd], [carTop + 3, carTop + 3], color='pink')
    plt.plot([sectStart, sectEnd], [carTop + 5, carTop + 5], color='pink')
    plt.plot([sectStart, 173.5], [carTop + 7, carTop + 7], color='pink')

def createFirstWindow():
    firstWindLeft = 98.5
    firstWindRight = 113.5
    # little 90 degree dip at the top of the window frame (vertical)
    plt.plot([firstWindLeft + 1, firstWindLeft + 1], [carTop + 7, carTop + 8], color='pink')
    plt.plot([firstWindRight - 1, firstWindRight - 1], [carTop + 7, carTop + 8], color='pink')
    # little 90 degree dip at the top of the window frame (horizontal)
    plt.plot([firstWindLeft + 1, firstWindLeft], [carTop + 8, carTop + 8], color='pink')
    plt.plot([firstWindRight - 1, firstWindRight], [carTop + 8, carTop + 8], color='pink')
    # long vertical window frame line
    plt.plot([firstWindLeft, firstWindLeft], [carTop + 8, 41], color='pink')
    plt.plot([firstWindRight, firstWindRight], [carTop + 8, 41], color='pink')

def createSecondWindow():
    secondWindLeft = 117.5
    secondWindRight = 132.5
    # little 90 degree dip at the top of the window frame (vertical)
    plt.plot([secondWindLeft + 1, secondWindLeft + 1], [carTop + 7, carTop + 8], color='pink')
    plt.plot([secondWindRight - 1, secondWindRight - 1], [carTop + 7, carTop + 8], color='pink')
    # little 90 degree dip at the top of the window frame (horizontal)
    plt.plot([secondWindLeft + 1, secondWindLeft], [carTop + 8, carTop + 8], color='pink')
    plt.plot([secondWindRight - 1, secondWindRight], [carTop + 8, carTop + 8], color='pink')
    # long vertical window frame line
    plt.plot([secondWindLeft, secondWindLeft], [carTop + 8, carBottom - 10], color='pink')
    plt.plot([secondWindRight, secondWindRight], [carTop + 8, carBottom - 10], color='pink')
    # window bottom frame
    plt.plot([secondWindLeft + .5, secondWindRight - .5], [carBottom - 9.5, carBottom - 9.5], color='pink')
    # arcs in corner of window frame
    arcPink(secondWindRight - .5, carBottom - 10, .5, 0, 90)
    arcPink(secondWindLeft + .5, carBottom - 10, .5, 90, 180)

def createThirdWindow():
    thirdWindLeft = 135
    thirdWindRight = 150
    # little 90 degree dip at the top of the window frame (vertical)
    plt.plot([thirdWindLeft + 1, thirdWindLeft + 1], [carTop + 7, carTop + 8], color='pink')
    plt.plot([thirdWindRight - 1, thirdWindRight - 1], [carTop + 7, carTop + 8], color='pink')
    # little 90 degree dip at the top of the window frame (horizontal)
    plt.plot([thirdWindLeft + 1, thirdWindLeft], [carTop + 8, carTop + 8], color='pink')
    plt.plot([thirdWindRight - 1, thirdWindRight], [carTop + 8, carTop + 8], color='pink')
    # long vertical window frame line
    plt.plot([thirdWindLeft, thirdWindLeft], [carTop + 8, carBottom - 10], color='pink')
    plt.plot([thirdWindRight, thirdWindRight], [carTop + 8, carBottom - 10], color='pink')
    # window bottom frame
    plt.plot([thirdWindLeft + .5, thirdWindRight - .5], [carBottom - 9.5, carBottom - 9.5], color='pink')
    # arcs on window frame
    arcPink(thirdWindRight - .5, carBottom - 10, .5, 0, 90)
    arcPink(thirdWindLeft + .5, carBottom - 10, .5, 90, 180)

def createFourthWindow():
    fourthWindLeft = 154
    fourthWindRight = 169
    # little 90 degree dip at the top of the window frame (vertical)
    plt.plot([fourthWindLeft + 1, fourthWindLeft + 1], [carTop + 7, carTop + 8], color='pink')
    plt.plot([fourthWindRight - 1, fourthWindRight - 1], [carTop + 7, carTop + 8], color='pink')
    # little 90 degree dip at the top of the window frame (horizontal)
    plt.plot([fourthWindLeft + 1, fourthWindLeft], [carTop + 8, carTop + 8], color='pink')
    plt.plot([fourthWindRight - 1, fourthWindRight], [carTop + 8, carTop + 8], color='pink')
    # long vertical window frame line
    plt.plot([fourthWindLeft, fourthWindLeft], [carTop + 8, 41], color='pink')
    plt.plot([fourthWindRight, fourthWindRight], [carTop + 8, 41], color='pink')

def linesOnCarBottom():
    # all 5 horizontal lines that extend the train (but only before the first cutoff)
    plt.plot([sectStart, 94.5], [carBottom - 5, carBottom - 5], color='pink')
    plt.plot([sectStart, 94.5], [carBottom - 2.2, carBottom - 2.2], color='pink')
    plt.plot([sectStart, 94.5], [carBottom - 1.6, carBottom - 1.6], color='pink')
    plt.plot([sectStart, 94.5], [41, 41], color='pink')
    plt.plot([sectStart, 94.5], [42, 42], color='pink')
    # all 5 horizontal lines that extend the train (after first cutoff, before second)
    plt.plot([97, 170.5], [carBottom - 5, carBottom - 5], color='pink')
    plt.plot([97, 170.5], [carBottom - 2.2, carBottom - 2.2], color='pink')
    plt.plot([97, 170.5], [carBottom - 1.6, carBottom - 1.6], color='pink')
    plt.plot([97, 170.5], [41, 41], color='pink')
    plt.plot([97, 170.5], [42, 42], color='pink')
    # all 5 horizontal lines that extend the train (after second cutoff, to the end)
    plt.plot([173.5, sectEnd], [carBottom - 5, carBottom - 5], color='pink')
    plt.plot([173.5, sectEnd], [carBottom - 2.2, carBottom - 2.2], color='pink')
    plt.plot([173.5, sectEnd], [carBottom - 1.6, carBottom - 1.6], color='pink')
    plt.plot([173.5, sectEnd], [41, 41], color='pink')
    plt.plot([173.5, sectEnd], [42, 42], color='pink')
    # bottom two lines from start to finish
    plt.plot([sectStart, sectEnd], [carBottom - 1, carBottom - 1], color='pink')
    plt.plot([sectStart, sectEnd], [carBottom, carBottom], color='pink')

def car_body(plt, axes, car_top, car_bottom, car_ground):
    # making the train
    linesSeperatingCars()
    lineOnTopOfCar()
    createFirstWindow()
    createSecondWindow()
    createThirdWindow()
    createFourthWindow()
    linesOnCarBottom()

    # decorating the train

    # create cat
    headCenterX = ((132.5 - 117.5) / 2 + 117.5) - 1
    headCenterY = (carBottom - 5 - carTop + 7) / 2 + carTop - 1
    # cat head
    axes.add_artist(plt.Circle((((132.5 - 117.5) / 2 + 117.5) - 1, (carBottom - 5 - carTop + 7) / 2 + carTop - 1), 4, color='k'))
    # white part of eyes
    axes.add_artist(plt.Circle((headCenterX-1.5,  headCenterY-.25), 1, color='white'))
    axes.add_artist(plt.Circle((headCenterX + 1.5, headCenterY - .25), 1, color='white'))
    # pupils
    axes.add_artist(plt.Circle((headCenterX - 1.5 + .25, headCenterY - .25), .5, color='k'))
    axes.add_artist(plt.Circle((headCenterX + 1.5 - .25, headCenterY - .25), .5, color='k'))
    # nose
    axes.add_artist(plt.Circle((124, 31), .25, color='white'))
    # whiskers
    plt.plot([122, 119], [31.5, 30], linewidth = 1.5, color='grey')
    plt.plot([122, 119], [32, 32], linewidth = 1.5, color='grey')
    plt.plot([122, 119], [32.5, 33.5], linewidth=1.5, color='grey')
    plt.plot([126, 129], [31.5, 30], linewidth=1.5, color='grey')
    plt.plot([126, 129], [32, 32], linewidth = 1.5,color='grey')
    plt.plot([126, 129], [32.5, 33.5], linewidth = 1.5,color='grey')
    # body
    plt.plot([122.5, 120.5], [34.18, 37.5], linewidth = 1.5,color='black')
    plt.plot([126, 127], [34, 37.5], linewidth = 1.5,color='black')
    # ears
    plt.plot([120.5, 120.5], [28.5, 25], linewidth = 1.5,color='black')
    plt.plot([120.5, 123], [25, 26.5], linewidth = 1.5,color='black')
    plt.plot([127.5, 127.5], [28.5, 25], linewidth = 1.5,color='black')
    plt.plot([127.5, 125], [25, 26.5], linewidth = 1.5,color='black')

    # adding flowers
    add_flower(plt, axes, 126, 43.5, .75, 'purple')
    add_flower(plt, axes, 136, 40, .75, 'blue')
    add_flower(plt, axes, 147, 43.5, .75, 'green')
    add_flower(plt, axes, 150, 40, .75, 'blue')
    add_flower(plt, axes, 176, 21.25, 1, 'purple')
    add_flower(plt, axes, 175.25, 26, .5, 'blue')
    add_flower(plt, axes, 176, 31, 1, 'red')
    add_flower(plt, axes, 176, 37, .75, 'purple')
    add_flower(plt, axes, 177, 43.5, .75, 'green')
    add_flower(plt, axes, 120, 40, .75, 'purple')
    add_flower(plt, axes, 150, 40, .75, 'green')

