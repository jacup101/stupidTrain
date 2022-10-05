import matplotlib.pyplot as plt
import numpy as np
import front_car as fc
import front_side_car as fsc
import car_body as cd
import car_end as ce

# of the form min, max, diff
xvars = [0, 220, 5]
yvars = [60, 0, -5]




###### Set up our plot ######
# Add aspect ratio, to prevent distortion
figure, axes = plt.subplots()
axes.set_aspect(1)
# Set up axis
plt.axis([xvars[0], xvars[1], yvars[0], yvars[1]])
# Add ticks
plt.xticks(np.arange(xvars[0], xvars[1], xvars[2]))
plt.yticks(np.arange(yvars[0], yvars[1], yvars[2]))
# Turn axis + grid on
plt.axis('on')
plt.grid(True, color = '0.5')

##### Declare other important variables #####
car_top = 14
car_bottom = 47
car_ground = 49


##### Define a ground line with the plot (because why not lol)
plt.plot([5, 205], [car_ground, car_ground], linewidth = 1.5, color = 'black')

##### Run the plot through each individual drawing code #####
fc.front_car(plt, axes, car_top, car_bottom, car_ground)
fsc.front_side_car(plt, axes, car_top, car_bottom, car_ground)
cd.car_body(plt, axes, car_top, car_bottom, car_ground)
ce.car_end(plt, axes, car_top, car_bottom, car_ground)

##### Show the plot #####
plt.show()
