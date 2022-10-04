import matplotlib.pyplot
import numpy as np
import math

## Fields
# Containers for lines, circles, ellipses to be drawn
lines = []
circles = []
ellipses = []
step = 1
x_frame_begin = 65
x_frame_end = 93.5

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
    populate_lines(car_top, car_bottom, car_ground)
    plot_lines(plt)
    populate_circles()
    plot_circles(plt)

def plot_line(plt, line: Line):
    plt.plot([line.x1, line.x2], [line.y1, line.y2], linewidth = 1, color = line.color)

def plot_circle(plt, circle: Circle):
    alpha1 = math.radians(circle.deg0)
    alpha2 = math.radians(circle.deg1)
    dalpha = math.radians(step)

    xlast = circle.xc + circle.radius * math.cos(alpha1)
    ylast = circle.yc + circle.radius * math.sin(alpha1)

    for alpha in np.arange(alpha1, alpha2 + dalpha, dalpha):
        x = circle.xc + circle.radius * math.cos(alpha)
        y = circle.yc + circle.radius * math.sin(alpha)
        plt.plot([xlast, x], [ylast, y], linewidth = 1, color = circle.color)
        xlast = x
        ylast = y


def plot_ellipse(plt, ellipse: Ellipse):
    # To be implemented
    # WLOG, radA will be height, radB will be width
    # Refer to textbook for code, we will most likely use algebra, but try trig first bc cleaner
    return None


### Grind work
def populate_lines(top, bottom, ground):
    # Bottom Car Line
    lines.append(Line(70, bottom, 90, bottom, 'black'))
    # lines.append(Line(67.5, bottom, 66, 45, 'black'))

    # Slightly above line
    lines.append(Line(67, 45, 90, 45, 'black'))
    # lines.append(Line(66, 45, 66, 44.5, 'black'))

    # Slightly above that
    lines.append(Line(66.4, 44.5, 90, 44.5, 'black'))
    # lines.append(Line(65.5, 44.5, 65.5, 44, 'black'))

    # Slightly above that
    lines.append(Line(66.4, 44, 90, 44, 'black'))

    # Lines above those
    lines.append(Line(66.3, 42, 90, 42, 'black'))
    lines.append(Line(66.8, 41, 90.04, 41, 'black'))




    # Front Window Lines
    # Left most
    lines.append(Line(66.5, 42 ,69.5, 32.5, 'black'))
    lines.append(Line(69.5, 32.5, 77, 17, 'black'))

    # Line between them
    lines.append(Line(69.5, 32.5, 70, 32.5, 'black'))

    # Almost left most
    lines.append(Line(67, 42, 70, 32.5, 'black'))
    lines.append(Line(70, 32.5, 77.5, 17, 'black'))

    window_bot_left = 73.5
    # Continued diags
    lines.append(Line(71, 41, window_bot_left, 31.5, 'black'))
    lines.append(Line(window_bot_left, 31.5, 79, 18, 'black'))
    lines.append(Line(window_bot_left, 31.5, 79.5, 18.5, 'black'))
    
    # Window bot line
    lines.append(Line(window_bot_left, 32.5, 90, 32.5, 'black'))
    lines.append(Line(window_bot_left, 32.0, 90, 32.0, 'black'))
    lines.append(Line(75, 31.5, 90, 31.5, 'black'))

    # one rand diag
    lines.append(Line(75, 31.5, 80, 19, 'black'))




    # Bottom Car Below Rect
    lines.append(Line(73.69, 48.424, 82.465, 48.424, 'black'))
    lines.append(Line(73.69, bottom, 73.69, 48.424, 'black'))
    lines.append(Line(82.465, bottom, 82.465, 48.424, 'black'))

    # Connector
    return None
    # lines.append(Line(0, 0, 10, 10, 'b'))
    # lines.append(Line(30, 0, 50, 10, 'b'))
    # lines.append(Line(5, 5, 5, 10, 'r'))
    # lines.append(Line(0, 0, 0, 10, 'r'))

def populate_circles():
    # Bottom Left Bumper
    circles.append(Circle(70.1, 43.5, 4, 'black', deg0 = 90, deg1 = 210))
    return None
    # circles.append(Circle(5, 5, 10, 'b', 0, 325))
