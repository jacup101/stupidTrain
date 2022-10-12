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

def add_flower(plt, axes, xc, yc, radius, color):
    # Order: top leaf, bot leaf, left top, left bot, right top, right bot
    xdiff = [0, 0, 0, 0, -radius, -radius, radius, radius]
    ydiff = [0, 0, -radius, radius, -radius / 2, radius / 2, -radius / 2, radius / 2]
    for i in range(len(xdiff)):
        axes.add_artist(plt.Circle((xc + xdiff[i], yc + ydiff[i]), radius, color=color))
    center = plt.Circle((xc, yc), radius, color='yellow')
    axes.add_artist(center)

def car_body(plt, axes, car_top, car_bottom, car_ground):
    carTop = 14
    carBottom = 47

    # x-coordinates for start and end of section
    sectEnd = 178.5
    sectStart = 93.5

    # line seperating car sections
    lineTop = carTop + 1
    lineBottom = carBottom - .5
    plt.plot([sectEnd, sectEnd], [carTop, carBottom], color='pink')
    plt.plot([sectEnd + .5, sectEnd + .5], [lineTop, lineBottom],  linewidth = 2, color='pink')
    plt.plot([sectEnd + 1, sectEnd + 1], [lineTop, lineBottom], color='pink')
    plt.plot([sectEnd + 1.5, sectEnd + 1.5], [lineTop, lineBottom], color='pink')
    plt.plot([sectStart, sectStart], [carTop, carBottom], color='pink')
    arcPink(sectEnd+.25, lineTop, 0.25, 180, 360)
    arcPink(sectEnd + .75, lineTop, 0.25, 180, 360)
    arcPink(sectEnd + 1.25, lineTop, 0.25, 180, 360)
    arcPink(sectEnd + .25, lineBottom, 0.25, 0, 180)
    arcPink(sectEnd + .75, lineBottom, 0.25, 0, 180)
    arcPink(sectEnd + 1.25, lineBottom, 0.25, 0, 180)

   # car top
    plt.plot([sectStart, sectEnd], [carTop, carTop], color='pink')
    plt.plot([sectStart, sectEnd], [carTop + 1, carTop + 1], color='pink')
    plt.plot([sectStart, sectEnd], [carTop + 3, carTop + 3], color='pink')
    plt.plot([sectStart, sectEnd], [carTop + 5, carTop + 5], color='pink')
    plt.plot([sectStart, 173.5], [carTop + 7, carTop + 7], color='pink')

    # first window
    firstWindLeft = 98.5
    firstWindRight = 113.5
    plt.plot([firstWindLeft + 1, firstWindLeft + 1], [carTop + 7, carTop + 8], color='pink')
    plt.plot([firstWindRight - 1, firstWindRight - 1], [carTop + 7, carTop + 8], color='pink')

    plt.plot([firstWindLeft + 1, firstWindLeft], [carTop + 8, carTop + 8], color='pink')
    plt.plot([firstWindRight - 1, firstWindRight], [carTop + 8, carTop + 8], color='pink')

    plt.plot([firstWindLeft, firstWindLeft], [carTop + 8, carBottom - 5], color='pink')
    plt.plot([firstWindRight, firstWindRight], [carTop + 8, carBottom-5], color='pink')

    # second window
    secondWindLeft = 117.5
    secondWindRight = 132.5

    plt.plot([secondWindLeft + 1, secondWindLeft + 1], [carTop + 7, carTop + 8], color='pink')
    plt.plot([secondWindRight - 1, secondWindRight - 1], [carTop + 7, carTop + 8], color='pink')

    plt.plot([secondWindLeft + 1, secondWindLeft], [carTop + 8, carTop + 8], color='pink')
    plt.plot([secondWindRight - 1, secondWindRight], [carTop + 8, carTop + 8], color='pink')

    plt.plot([secondWindLeft, secondWindLeft], [carTop + 8, carBottom - 10], color='pink')
    plt.plot([secondWindRight, secondWindRight], [carTop + 8, carBottom - 10], color='pink')

    plt.plot([secondWindLeft + .5, secondWindRight - .5], [carBottom - 9.5, carBottom - 9.5], color='pink')
    arcPink(secondWindRight - .5, carBottom - 10, .5 , 0, 90)
    arcPink(secondWindLeft + .5, carBottom - 10, .5 , 90, 180)

    # cat
    arcBlack(((secondWindRight - secondWindLeft) / 2 + secondWindLeft)-1, (carBottom - 5 - carTop + 7) / 2 + carTop - 1, 4, 0, 360)
    headCenterX = ((secondWindRight - secondWindLeft) / 2 + secondWindLeft) - 1
    headCenterY = (carBottom - 5 - carTop + 7) / 2 + carTop - 1
    arcBlack(headCenterX-1.5,
             headCenterY-.25, 1,
             0, 360)
    arcBlack(headCenterX + 1.5,
             headCenterY - .25, 1,
             0, 360)

    plt.scatter(headCenterX - 1.5 +.25,  headCenterY - .25, s=150, color='black')
    plt.scatter(headCenterX + 1.5 -.25, headCenterY - .25, s=150, color='black')
    arcBlack(124, 31, .25, 0 ,360)
    plt.plot([122, 119], [31.5, 30], linewidth = 1.5,color='black')
    plt.plot([126, 129], [31.5, 30], linewidth = 1.5, color='black')
    plt.plot([122, 119], [32, 32], linewidth = 1.5, color='black')
    plt.plot([126, 129], [32, 32], linewidth = 1.5,color='black')
    plt.plot([122, 119], [31.5, 30], linewidth = 1.5,color='black')
    plt.plot([126, 129], [31.5, 30], linewidth = 1.5,color='black')
    plt.plot([122, 119], [32.5, 33.5], linewidth = 1.5,color='black')
    plt.plot([126, 129], [32.5, 33.5], linewidth = 1.5,color='black')
    plt.plot([122.5, 120.5], [34.18, 37.5], linewidth = 1.5,color='black')
    plt.plot([126, 127], [34, 37.5], linewidth = 1.5,color='black')


    plt.plot([120.5, 120.5], [28.5, 25], linewidth = 1.5,color='black')
    plt.plot([120.5, 123], [25, 26.5], linewidth = 1.5,color='black')
    plt.plot([127.5, 127.5], [28.5, 25], linewidth = 1.5,color='black')
    plt.plot([127.5, 125], [25, 26.5], linewidth = 1.5,color='black')

    # third window
    thirdWindLeft = 135
    thirdWindRight = 150
    plt.plot([thirdWindLeft + 1, thirdWindLeft + 1], [carTop + 7, carTop + 8], color='pink')
    plt.plot([thirdWindRight - 1, thirdWindRight - 1], [carTop + 7, carTop + 8], color='pink')

    plt.plot([thirdWindLeft + 1, thirdWindLeft], [carTop + 8, carTop + 8], color='pink')
    plt.plot([thirdWindRight - 1, thirdWindRight], [carTop + 8, carTop + 8], color='pink')

    plt.plot([thirdWindLeft, thirdWindLeft], [carTop + 8, carBottom - 10], color='pink')
    plt.plot([thirdWindRight, thirdWindRight], [carTop + 8, carBottom - 10], color='pink')

    plt.plot([thirdWindLeft + .5, thirdWindRight - .5], [carBottom - 9.5, carBottom - 9.5], color='pink')

    arcPink(thirdWindRight - .5, carBottom - 10, .5, 0, 90)
    arcPink(thirdWindLeft + .5, carBottom - 10, .5, 90, 180)

    # fourth window
    fourthWindLeft = 154
    fourthWindRight = 169
    plt.plot([fourthWindLeft + 1, fourthWindLeft+ 1], [carTop + 7, carTop + 8], color='pink')
    plt.plot([fourthWindRight - 1, fourthWindRight - 1], [carTop + 7, carTop + 8], color='pink')

    plt.plot([fourthWindLeft+ 1, fourthWindLeft], [carTop + 8, carTop + 8], color='pink')
    plt.plot([fourthWindRight - 1, fourthWindRight], [carTop + 8, carTop + 8], color='pink')

    plt.plot([fourthWindLeft, fourthWindLeft], [carTop + 8, carBottom - 5], color='pink')
    plt.plot([fourthWindRight, fourthWindRight], [carTop + 8, carBottom - 5], color='pink')

    # vertical lines on car
    plt.plot([94.5, 94.5], [carTop + 7, carBottom - 1], color='pink')
    plt.plot([96, 96], [carTop + 7, carBottom - 1], color='pink')

    plt.plot([97, 97], [carTop + 7, carBottom], color='pink')
    plt.plot([115, 115], [carTop + 7, carBottom], color='pink')

    plt.plot([152.5, 152.5], [carTop + 7, carBottom], color='pink')
    plt.plot([170.5, 170.5], [carTop + 7, carBottom], color='pink')

    plt.plot([172, 172], [carTop + 7, carBottom-1], color='pink')
    plt.plot([173.5, 173.5], [carTop + 7, carBottom-1], color='pink')

    # bottom of car lines

    plt.plot([sectStart, 94.5], [carBottom - 5, carBottom - 5], color='pink')
    plt.plot([sectStart, 94.5], [carBottom - 2.2, carBottom - 2.2], color='pink')
    plt.plot([sectStart, 94.5], [carBottom - 1.6, carBottom - 1.6], color='pink')

    plt.plot([97, 170.5], [carBottom - 5, carBottom - 5], color='pink')
    plt.plot([97, 170.5], [carBottom - 2.2, carBottom - 2.2], color='pink')
    plt.plot([97, 170.5], [carBottom - 1.6, carBottom - 1.6], color='pink')

    plt.plot([173.5, sectEnd], [carBottom - 5, carBottom - 5], color='pink')
    plt.plot([173.5, sectEnd], [carBottom - 2.2, carBottom - 2.2], color='pink')
    plt.plot([173.5, sectEnd], [carBottom - 1.6, carBottom - 1.6], color='pink')

    plt.plot([sectStart, sectEnd], [carBottom - 1, carBottom - 1], color='pink')
    plt.plot([sectStart, sectEnd], [carBottom, carBottom], color='pink')

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

