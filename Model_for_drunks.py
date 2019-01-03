# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:28:53 2018

@author: gy16mg
"""

#import the modules that we will use
#the csv module will be needed so that we can read 
#the data for the environment

import csv
import matplotlib
import Drunks_Framework as drfr
import matplotlib.animation

"""In this section, we will read the data for the environment/town.
"""

f = open('drunk.plan.txt', newline='')

reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#create the environment initially as an empty list
environment = []

#read each row in the reader 
for row in reader:
    #create an empty list for all the values in each row
    rowlist = []
    #for each of the rows read the values and write them in the list above
    for value in row:
        #fill the empty rowlist with values from each one of the rows
        #change the value of the pub from 1 to 255
        if (value == 1):
            rowlist.append(255)
        else:
            rowlist.append(value)
    #fill the environment with the rowlists each time    
    environment.append(rowlist)
   #we have to close the reader now that we are done 
f.close

#density_map = environment

#create the plot for the environment
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

"""In this section, the density map will be created.
"""
#create the environment initially as an empty list, 
#the same way the environment was created.

density_map = []

#read each row in the reader 
for row in reader:
    #create an empty list for all the values in each row
    rowlist = []
    #for each of the rows read the values and write them in the list above
    for value in row:
        #fill the empty rowlist with value 0
        rowlist.append(0)
    #fill the environment with the rowlists each time    
    density_map.append(rowlist)
   #we have to close the reader now that we are done 
f.close

matplotlib.pyplot.imshow(density_map)
matplotlib.pyplot.show()

"""In this section, we will find the coordinates of the pub.
"""

#write code that will find the location of the pub
#we have to go through all the values 
#in order to find the 255s for the pub

pub = []
for j in range(len(environment)):
    for i in range(len(environment[j])):
        if environment[j][i] == 255.0:
            pub.append(j)
            pub.append(i)
            break
    else:
        continue
    break
print(pub)

"""In this section, we will generate the drunks
   and make them move.
"""

num_of_drunks = 25
drunks= []
x = pub[1]
y = pub[0]

#create a list of drunks using the Drunks_Framework.py
for i in range(num_of_drunks):
    drunks.append(drfr.Drunk(x, y, (i+1), environment, drunks))

#move the agents while the condition
# "drunks[i].is_drunk_home" is False
#when this becomes true, the next agent starts moving
for i in range(num_of_drunks):
        while drunks[i].is_drunk_home == False:
            drunks[i].move()
            density_map[drunks[i].y][drunks[i].x] = density_map[drunks[i].y][drunks[i].x] + 1
            
#plot the density map that is created from the movement of drunks
matplotlib.pyplot.imshow(density_map)
matplotlib.pyplot.show()
          
#write the density map in a new txt file named 
#"Density_map.txt"

f2 = open('Density_map.txt', 'w', newline='') 
writer = csv.writer(f2, delimiter=' ')
for row in density_map:		
	writer.writerow(row)		# List of values.
f2.close()


