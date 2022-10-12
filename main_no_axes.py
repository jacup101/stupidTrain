'''
Student Author Name: Joshua Pulido, Campbell Gilbert, Bryce Joseph, Cathy Yim
Group Name: Team Sanrio
Project 1
Fall 2022
COMP 313: Computer Graphics
Professor Schiffer
'''

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

# Turn axis + grid on
plt.axis('off')

##### Declare other important variables #####
car_top = 14
car_bottom = 47
car_ground = 49


##### Define a ground line with the plot (because why not lol)
plt.plot([5, 205], [car_ground, car_ground], linewidth = 1.5, color = 'black')
##### Define the text with group names, team name
team_name = "Team Sanrio"
team_name_text = plt.Text(0, 55, team_name, color='pink')
member_names = "Josh Pulido, Campbell Gilbert, Cathy Yim, Bryce Joseph"
member_names_text = plt.Text(0, 60, member_names, color='pink')
axes.add_artist(team_name_text)
axes.add_artist(member_names_text)

##### Run the plot through each individual drawing code #####
fc.front_car(plt, axes, car_top, car_bottom, car_ground)
fsc.front_side_car(plt, axes, car_top, car_bottom, car_ground)
cd.car_body(plt, axes, car_top, car_bottom, car_ground)
ce.car_end(plt, axes, car_top, car_bottom, car_ground)

##### Show the plot #####
plt.show()
