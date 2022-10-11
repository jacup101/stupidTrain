import matplotlib.pyplot as plt
import numpy as np
import math

def arc(xc, yc, r, a1, a2):
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

def ellipse(xc, yc, a, b, deg0=0, deg1=180, step=0.5, half=1, color='k'):
    alpha1 = np.radians(deg0)
    alpha2 = np.radians(deg1)
    dalpha = np.radians(step)

    # Starting values are null at start, since we want to account for non standard angles. This allows us to use the ellipse function to draw arcs
    xlast = 'null'
    ylast = 'null'

    for alpha in np.arange(alpha1, alpha2 + dalpha, dalpha):
        # Note here that x and y stand for delta x and delta y
        # To avoid the div by zero, we place in an if statement
        if (np.tan(alpha) != 0):
            x = np.abs(a * b / np.sqrt(math.pow(b, 2) + (math.pow(a, 2) * math.pow(np.tan(alpha), 2))))
            y = np.abs(a * b / np.sqrt(math.pow(a, 2) + math.pow(b, 2) * (1 / math.pow(np.tan(alpha), 2))))

            if alpha > np.pi / 2:
                x = -x
            # Divide by zero condition
            if xlast == 'null':
                xlast = x
            if ylast == 'null':
                ylast = y
            plt.plot([xc + xlast, xc + x], [yc + half * ylast, yc + half * y], linewidth=1, color=color)

            xlast = x
            ylast = y

def car_body(plt, axes, car_top, car_bottom, car_ground):
    carTop = 14
    carBottom = 47

    # x-coordinates for start and end of section
    sectEnd = 178.5
    sectStart = 93.5

    # line seperating car sections
    lineTop = carTop + 1
    lineBottom = carBottom - .5
    plt.plot([sectEnd + .5, sectEnd + .5], [lineTop, lineBottom],  linewidth = 2, color='black')
    plt.plot([sectEnd + 1, sectEnd + 1], [lineTop, lineBottom], color='black')
    plt.plot([sectEnd + 1.5, sectEnd + 1.5], [lineTop, lineBottom], color='black')

    plt.plot([sectStart, sectStart], [carTop, carBottom], color='black')

   # car top
    plt.plot([sectStart, sectEnd], [carTop, carTop], color='black')
    plt.plot([sectStart, sectEnd], [carTop + 1, carTop + 1], color='black')
    plt.plot([sectStart, sectEnd], [carTop + 3, carTop + 3], color='black')
    plt.plot([sectStart, sectEnd], [carTop + 5, carTop + 5], color='black')
    plt.plot([sectStart, 173.5], [carTop + 7, carTop + 7], color='black')

    # first window
    firstWindLeft = 98.5
    firstWindRight = 113.5
    plt.plot([firstWindLeft + 1, firstWindLeft + 1], [carTop + 7, carTop + 8], color='black')
    plt.plot([firstWindRight - 1, firstWindRight - 1], [carTop + 7, carTop + 8], color='black')

    plt.plot([firstWindLeft + 1, firstWindLeft], [carTop + 8, carTop + 8], color='black')
    plt.plot([firstWindRight - 1, firstWindRight], [carTop + 8, carTop + 8], color='black')

    plt.plot([firstWindLeft, firstWindLeft], [carTop + 8, carBottom - 5], color='black')
    plt.plot([firstWindRight, firstWindRight], [carTop + 8, carBottom-5], color='black')

    # second window
    secondWindLeft = 117.5
    secondWindRight = 132.5

    plt.plot([secondWindLeft + 1, secondWindLeft + 1], [carTop + 7, carTop + 8], color='black')
    plt.plot([secondWindRight - 1, secondWindRight - 1], [carTop + 7, carTop + 8], color='black')

    plt.plot([secondWindLeft + 1, secondWindLeft], [carTop + 8, carTop + 8], color='black')
    plt.plot([secondWindRight - 1, secondWindRight], [carTop + 8, carTop + 8], color='black')

    plt.plot([secondWindLeft, secondWindLeft], [carTop + 8, carBottom - 10], color='black')
    plt.plot([secondWindRight, secondWindRight], [carTop + 8, carBottom - 10], color='black')

    plt.plot([secondWindLeft + .5, secondWindRight - .5], [carBottom - 9.5, carBottom - 9.5], color='black')
    arc(secondWindRight - .5, carBottom - 10, .5 , 0, 90)
    arc(secondWindLeft + .5, carBottom - 10, .5 , 90, 180)

    # third window
    thirdWindLeft = 135
    thirdWindRight = 150
    plt.plot([thirdWindLeft + 1, thirdWindLeft + 1], [carTop + 7, carTop + 8], color='black')
    plt.plot([thirdWindRight - 1, thirdWindRight - 1], [carTop + 7, carTop + 8], color='black')

    plt.plot([thirdWindLeft + 1, thirdWindLeft], [carTop + 8, carTop + 8], color='black')
    plt.plot([thirdWindRight - 1, thirdWindRight], [carTop + 8, carTop + 8], color='black')

    plt.plot([thirdWindLeft, thirdWindLeft], [carTop + 8, carBottom - 10], color='black')
    plt.plot([thirdWindRight, thirdWindRight], [carTop + 8, carBottom - 10], color='black')

    plt.plot([thirdWindLeft + .5, thirdWindRight - .5], [carBottom - 9.5, carBottom - 9.5], color='black')

    arc(thirdWindRight - .5, carBottom - 10, .5, 0, 90)
    arc(thirdWindLeft + .5, carBottom - 10, .5, 90, 180)

    # fourth window
    fourthWindLeft = 154
    fourthWindRight = 169
    plt.plot([fourthWindLeft + 1, fourthWindLeft+ 1], [carTop + 7, carTop + 8], color='black')
    plt.plot([fourthWindRight - 1, fourthWindRight - 1], [carTop + 7, carTop + 8], color='black')

    plt.plot([fourthWindLeft+ 1, fourthWindLeft], [carTop + 8, carTop + 8], color='black')
    plt.plot([fourthWindRight - 1, fourthWindRight], [carTop + 8, carTop + 8], color='black')

    plt.plot([fourthWindLeft, fourthWindLeft], [carTop + 8, carBottom - 5], color='black')
    plt.plot([fourthWindRight, fourthWindRight], [carTop + 8, carBottom - 5], color='black')

    # vertical lines on car
    plt.plot([94.5, 94.5], [carTop + 7, carBottom - 1], color='black')
    plt.plot([96, 96], [carTop + 7, carBottom - 1], color='black')

    plt.plot([97, 97], [carTop + 7, carBottom], color='black')
    plt.plot([115, 115], [carTop + 7, carBottom], color='black')

    plt.plot([152.5, 152.5], [carTop + 7, carBottom], color='black')
    plt.plot([170.5, 170.5], [carTop + 7, carBottom], color='black')

    plt.plot([172, 172], [carTop + 7, carBottom-1], color='black')
    plt.plot([173.5, 173.5], [carTop + 7, carBottom-1], color='black')

    # bottom of car lines

    plt.plot([sectStart, 94.5], [carBottom - 5, carBottom - 5], color='black')
    plt.plot([sectStart, 94.5], [carBottom - 2.2, carBottom - 2.2], color='black')
    plt.plot([sectStart, 94.5], [carBottom - 1.6, carBottom - 1.6], color='black')

    plt.plot([97, 170.5], [carBottom - 5, carBottom - 5], color='black')
    plt.plot([97, 170.5], [carBottom - 2.2, carBottom - 2.2], color='black')
    plt.plot([97, 170.5], [carBottom - 1.6, carBottom - 1.6], color='black')

    plt.plot([173.5, sectEnd], [carBottom - 5, carBottom - 5], color='black')
    plt.plot([173.5, sectEnd], [carBottom - 2.2, carBottom - 2.2], color='black')
    plt.plot([173.5, sectEnd], [carBottom - 1.6, carBottom - 1.6], color='black')




    plt.plot([sectStart, sectEnd], [carBottom - 1, carBottom - 1], color='black')
    plt.plot([sectStart, sectEnd], [carBottom, carBottom], color='black')


