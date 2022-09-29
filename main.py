import matplotlib.pyplot as plt
import numpy as np
import front_car as fc
import front_side_car as fsc
import car_body as cd

# of the form min, max, diff
xvars = [0, 220, 10]
yvars = [-60, 0, 10]

###### Set up our plot ######
# Add aspect ratio, to prevent distortion
plt.axes().set_aspect(1)
# Set up axis
plt.axis([xvars[0], xvars[1], yvars[0], yvars[1]])
# Add ticks
plt.xticks(np.arange(xvars[0], xvars[1], xvars[2]))
plt.yticks(np.arange(yvars[0], yvars[1], yvars[2]))
# Turn axis + grid on
plt.axis('on')
plt.grid(True, color = 'k')

##### Declare other important variables #####
car_top = -12
car_bottom = -47.5
car_ground = -49

##### Run the plot through each individual drawing code #####
fc.front_car(plt, car_top, car_bottom, car_ground)
fsc.front_side_car(plt, car_top, car_bottom, car_ground)
cd.car_body(plt, car_top, car_bottom, car_ground)

##### Show the plot #####
plt.show()
