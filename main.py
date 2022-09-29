import matplotlib.pyplot as plt
import numpy as np
import front_car as fc
import front_side_car as fsc
import car_body as cd

x1 = 0
x2 = 220
y1 = -60
y2 = 0
dx = 10
dy = 10

plt.axes().set_aspect(1)
plt.axis([x1, x2, y1, y2])

plt.xticks(np.arange(x1, x2, dx))
plt.yticks(np.arange(y1, y2, dy))

plt.axis('on')
plt.grid(True, color = 'k')

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
cd.front_side_car(plt, car_top, car_bottom, car_ground)

# Show the plot
plt.show()
