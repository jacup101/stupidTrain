import matplotlib.pyplot as plt
import numpy as np
import front_car as fc
import front_side_car as fsc


car_top = -12
car_bottom = -47.5
car_ground = -49

# Top line is - 12
# Bottom part (above wheels): -75
# Below wheels : 
print("hello world")
print("bryce made a change")

fc.front_car(plt, car_top, car_bottom, car_ground)
fsc.front_side_car(plt, car_top, car_bottom, car_ground)

# Show the plot
plt.show()