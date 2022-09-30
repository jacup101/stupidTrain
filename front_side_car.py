import matplotlib.pyplot
import numpy as np
import math

## Fields
# Containers for lines, circles, ellipses to be drawn
lines = []
circles = []
ellipses = []
step = 1

## Define classes for 
class Line:
    x1, x2, y1, y2, color = None, None, None, None, None
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = color

class Circle:
    radius, deg0, deg1, xc, yc, color = None, None, None, None, None, None
    # Note that deg 0 and deg 1 defalut to 0 and 360, are optional
    def __init__(self, xc, yc, radius, color, deg0 = 0, deg1 = 360):
        self.xc = xc
        self.yc = yc
        self.radius = radius
        self.color = color
        self.deg0 = deg0
        self.deg1 = deg1

class Ellipse:
    radiusA, radiusB, deg0, deg1, xc, yc, color = None, None, None, None, None, None, None
    # WLOG, radA will be height, radB will be width
    # TODO: Swap to using (x1, y1) to (x2,y2) version, if better
    # Note that deg 0 and deg 1 defalut to 0 and 360, are optional
    def __init__(self, xc, yc, radiusA, radiusB, color, deg0 = 0, deg1 = 360):
        self.xc = xc
        self.yc = yc
        self.radiusA = radiusA
        self.radiusB = radiusB
        self.color = color
        self.deg0 = deg0
        self.deg1 = deg1



def plot_lines(plt):
    for line in lines:
        plot_line(plt, line)

def plot_circles(plt):
    for circle in circles:
        plot_circle(plt, circle)

def front_side_car(plt, car_top, car_bottom, car_ground):
    plt.scatter(3, 3, s = 10 , color = 'b')
    populate_lines()
    plot_lines(plt)
    populate_circles()
    plot_circles(plt)

def plot_line(plt, line: Line):
    plt.plot([line.x1, line.x2], [line.y1, line.y2], linewidth = 1, color = line.color)

def plot_circle(plt, circle: Circle):
    alpha1 = math.radians(circle.deg0)
    alpha2 = math.radians(circle.deg1)
    dalpha = math.radians(step)

    for alpha in np.arange(alpha1, alpha2, dalpha):
        x = circle.xc + circle.radius * math.cos(alpha)
        y = circle.yc + circle.radius * math.sin(alpha)
        plt.scatter(x, y, s = 3, color = circle.color)


def plot_ellipse(plt, ellipse: Ellipse):
    # To be implemented
    # WLOG, radA will be height, radB will be width
    # Refer to textbook for code, we will most likely use algebra, but try trig first bc cleaner
    return None


### Grind work
def populate_lines():
    return None
    # lines.append(Line(0, 0, 10, 10, 'b'))
    # lines.append(Line(30, 0, 50, 10, 'b'))
    # lines.append(Line(5, 5, 5, 10, 'r'))
    # lines.append(Line(0, 0, 0, 10, 'r'))

def populate_circles():
    return None
    # circles.append(Circle(5, 5, 10, 'b', 0, 325))
