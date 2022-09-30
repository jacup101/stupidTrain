import numpy as np
import matplotlib.pyplot as plt

x1 = 0
x2 = 40
y1 = -10
y2 = -50

def front_car(plt, car_top, car_bottom, car_ground):
    plt.plot([x1, x2], [y1, y2], color = 'k')