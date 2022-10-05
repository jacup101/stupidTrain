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
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = color

class Circle:
    # Note that deg 0 and deg 1 defalut to 0 and 360, are optional
    def __init__(self, xc, yc, radius, color, deg0 = 0, deg1 = 360):
        self.xc = xc
        self.yc = yc
        self.radius = radius
        self.color = color
        self.deg0 = deg0
        self.deg1 = deg1

class Ellipse:
    # Radius A is width
    # Radius B i height
    # tdeg0 and tdeg1 are the radians for which we plot the upper half of the ellipse, if top is True - defaults described below
    # similar for  bdeg0, bdeg1, and bot
    def __init__(self, xc, yc, radiusA, radiusB, color, tdeg0 = 0, tdeg1 = 360, bdeg0 = 0, bdeg1 = 360, bot = True, top = True):
        self.xc = xc
        self.yc = yc
        self.radiusA = radiusA
        self.radiusB = radiusB
        self.color = color
        self.tdeg0 = tdeg0
        self.tdeg1 = tdeg1
        self.bdeg0 = bdeg0
        self.bdeg1 = bdeg1
        self.bot = bot
        self.top = top

def plot_lines(plt):
    """
    Plots lines in the global circles list
    :param plt: plot var from matplotlib
    :returns: None
    """
    for line in lines:
        plot_line(plt, line)

def plot_circles(plt):
    """
    Plots circles in the global circles list
    :param plt: plot var from matplotlib
    :returns: None
    """
    for circle in circles:
        plot_circle(plt, circle)

def plot_ellipses(plt):
    """
    Plots specified halves of ellipses in the global ellipses list
    :param plt: plot var from matplotlib
    :returns: None
    """
    for ellipse in ellipses:
        if ellipse.top:
            plot_ellipse(plt, ellipse, ellipse.tdeg0, ellipse.tdeg1, -1)
        if ellipse.bot:
            plot_ellipse(plt, ellipse, ellipse.bdeg0, ellipse.bdeg1, 1)

def front_side_car(plt, axes, car_top, car_bottom, car_ground):
    """
    Constructs the front side portion of the train/car for the project
    :param plt: plot var from matplotlib
    :car_top: predefined y coordinate for top of the car
    :car_bottom: predefined y coordinate for bottom of the car
    :car_ground: predefined y coordinate for the ground
    :returns: None
    """
    populate_lines(car_top, car_bottom, car_ground)
    plot_lines(plt)
    populate_circles(car_bottom)
    plot_circles(plt)
    populate_ellipses()
    plot_ellipses(plt)

def plot_line(plt, line: Line):
    """
    Tool used to plot a line
    :param plt: plot var from matplotlib
    :param line: instance of line class
    :returns: None
    """
    plt.plot([line.x1, line.x2], [line.y1, line.y2], linewidth = 1.5, color = line.color)

def plot_circle(plt, circle: Circle):
    """
    Tool used to plot a circle
    :param plt: plot var from matplotlib
    :param circle: instance of circle class
    :returns: None
    """
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

def plot_ellipse(plt, ellipse: Ellipse, deg0, deg1, half):
    """
    Tool used to plot a half of an ellipse
    :param plt: plot var from matplotlib
    :param ellipse: instance of ellipse class
    :param deg0: starting degree (in degrees)
    :param deg1: ending degree (in degrees)
    :param half: top or bottom, specified by 1 for bottom, -1 for top
    :returns: None
    """
    alpha1 = np.radians(deg0)
    alpha2 = np.radians(deg1)
    dalpha = np.radians(step)

    # Starting values are null at start, since we want to account for non standard angles. This allows us to use the ellipse function to draw arcs  
    xlast = 'null'
    ylast = 'null'

    for alpha in np.arange(alpha1, alpha2 + dalpha, dalpha):
        # Note here that x and y stand for delta x and delta y
        # To avoid the div by zero, we place in an if statement
        if(np.tan(alpha) != 0):
            x = np.abs(ellipse.radiusA * ellipse.radiusB / np.sqrt(math.pow(ellipse.radiusB, 2) + (math.pow(ellipse.radiusA, 2) * math.pow(np.tan(alpha), 2))))
            y = np.abs(ellipse.radiusA * ellipse.radiusB / np.sqrt(math.pow(ellipse.radiusA, 2) + math.pow(ellipse.radiusB, 2) * (1 / math.pow(np.tan(alpha), 2))))

            if alpha > np.pi / 2:
                x = -x
            # Divide by zero condition
            if xlast == 'null':
                xlast = x
            if ylast == 'null':
                ylast = y
            # print statement used for debug purposes
            # print([ellipse.xc + xlast, ellipse.xc + x, ellipse.yc + half * ylast, ellipse.yc + half * y])
            plt.plot([ellipse.xc + xlast, ellipse.xc + x], [ellipse.yc + half * ylast, ellipse.yc + half * y], linewidth = 1, color = ellipse.color)
            
            xlast = x
            ylast = y

### Grind work
def populate_lines(top, bottom, ground):
    """
    Defines the various lines in the train image
    :param top: predefined y coord for top of the car
    :param bottom: predefined y coord for bottom of the car
    :param ground: predefined y coord for the ground
    :returns: None
    """
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
    window_bot = 31.5
    # Continued diags
    lines.append(Line(71, 41, window_bot_left, window_bot, 'black'))
    lines.append(Line(window_bot_left, 31.5, 79, 18, 'black'))
    lines.append(Line(window_bot_left, 31.5, 79.5, 18.5, 'black'))
    
    # Window bot line
    lines.append(Line(window_bot_left, 32.5, 90, 32.5, 'black'))
    lines.append(Line(window_bot_left, 32.0, 90, 32.0, 'black'))
    lines.append(Line(75, 31.5, 90, 31.5, 'black'))

    # one rand diag
    lines.append(Line(75, 31.5, 80, 19, 'black'))
    # horizontal line connected to rand diag
    lines.append(Line(80, 19, 90, 19, 'black'))
    # vert perpendicular line to above
    lines.append(Line(88, window_bot, 88, 19, 'black'))

    # car back
    lines.append(Line(90, top, 90, bottom, 'black'))

    # Bottom Car Below Rect
    bot_rect_height = bottom + .75
    lines.append(Line(75, bot_rect_height, 84, bot_rect_height, 'black'))
    lines.append(Line(75, bottom, 75, bot_rect_height, 'black'))
    lines.append(Line(84, bottom, 84, bot_rect_height, 'black'))

    # Connector
    # Goes from 90 to about 94
    top_connect = top + .5
    bot_connect = bottom - .5
    lines.append(Line(90.5, top_connect, 90.5, bot_connect, 'black'))
    lines.append(Line(91, top_connect, 91, bot_connect, 'black'))
    lines.append(Line(91.5, top_connect, 91.5, bot_connect, 'black'))
    lines.append(Line(92, top_connect, 92, bot_connect, 'black'))
    # Top connector pieces
    lines.append(Line(90, top_connect, 93, top_connect, 'black'))
    lines.append(Line(90, bot_connect, 93, bot_connect, 'black'))

def populate_circles(bottom):
    """
    Defines the various circles in the train image
    :param bottom: predefined y coord for bottom of the car
    :returns: None
    """
    # Bottom Left Bumper
    circles.append(Circle(70.1, 43, 4, 'black', deg0 = 90, deg1 = 210))
    # Left Wheel
    wheel_center_y = bottom - .5
    circles.append(Circle(72, wheel_center_y, 2.5, 'black', deg0 = 15, deg1 = 165))
    # Right Wheel
    circles.append(Circle(87, wheel_center_y, 2.5, 'black', deg0 = 15, deg1 = 165))

def populate_ellipses():
    """
    Defines the various ellipses in the train image
    :returns: None
    """
    # Front arc
    ellipses.append(Ellipse(90, 17.5, 13, 3.9, 'black', bot = False, tdeg0 = 92, tdeg1 = 270))
    # Second left front arc
    ellipses.append(Ellipse(90, 18, 11, 3, 'black', bot = False, tdeg0 = 110, tdeg1 = 270))
    # Third from left
    ellipses.append(Ellipse(90, 18.5, 10.5, 3, 'black', bot = False, tdeg0 = 110, tdeg1 = 270))
    # Fourth from left
    ellipses.append(Ellipse(90, 19, 10, 3, 'black', bot = False, tdeg0 = 110, tdeg1 = 270))
    # Upside down arc in window
    ellipses.append(Ellipse(90, 19, 9.5, 1.8, 'black', top = False, bdeg0 = 110, bdeg1 = 270))
    


    

