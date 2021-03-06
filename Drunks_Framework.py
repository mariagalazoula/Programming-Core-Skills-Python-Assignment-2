# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:28:53 2018

@author: gy16mg
"""


#Create an Drunk Class, where we will give the drunks all of the 
#attributes that they will need for this model. First, we create the 
#drunks by creating an initial function called __init__, where we 
#assign the attributes of the agents, such as the starting coordinates (in this case the pub), 
#environment, etc and we also create the functions needed for this model,
#in order to move the agents.

import random  

#create the class for the agents:
class Drunk:
    
#create the agents and their attributes
    def __init__(self, x_pub, y_pub, number, environment,drunks):
        """Give the drunks their attributes:
        
        In this __init__ we initialise the drunks and give them their attributes. 
        self.x = x coordinate of the pub
        self.y = y coordinate of the pub
        self.number = number of the agent 
        self.environment = environment where the drunk will move
        self.drunks = the other drunks in the town
        self.is_drunk_home = a variable that will be used later in order to stop the drunks from moving once they reach their houses.
        
        
        """
        self.x = x_pub
        self.y = y_pub
        self.number = number
        self.environment = environment
        self.drunks = drunks      
        self.is_drunk_home = False
        
        #self.drunk_density_map = self.createDrunkDensityMap()


            
    def moveXaxis(self):
        """in this function the drunks move in the X axis.
        
        Arguments:
            self -- agent
        
        Based on a random number that is generated by random.random() 
        the drunk will move either left or right. Then, the new coordinate will be checked for the
        conditions that been set: 1. to move into the environment or their house and 2. to stay in the town.
        
        Returns:
            the new position of the drunk in the x axis.
        
        """
        new_x = 0
        old_x = self.x
        # select direction
        if (random.random()<0.5):
            new_x = old_x + 1
        else:
            new_x = old_x - 1
        # check for boundaries
        if new_x < 0:
            new_x = 0
        if new_x > len(self.environment[0])-1:
            new_x = len(self.environment[0])-1
        # check for buildings
        if (self.environment[self.y][new_x] == 0 or self.environment[self.y][new_x]==(self.number*10)):
            self.x = new_x
                
        else:
            self.x = old_x
        
    
    def moveYaxis(self):
        """in this function the drunks move in the Y axis.
        
        Arguments:
            self -- agent
        
        Based on a random number that is generated by random.random() 
        the drunk will move either up or down. Then, the new coordinate will be checked for the
        conditions that been set: 1. to move into the environment or their house and 2. to stay in the town.
        
        Returns:
            the new position of the drunk in the Y axis.
        
        """
        new_y = 0
        old_y = self.y
        # select direction
        if (random.random()<0.5):
            new_y = old_y + 1
        else:
            new_y = old_y - 1
        # check for boundaries
        if new_y < 0:
            new_y = 0
        if new_y > len(self.environment)-1:
            new_y = len(self.environment)-1
        # check for buildings
        if (self.environment[new_y][self.x] == 0 or self.environment[new_y][self.x]==(self.number*10)):
            self.y = new_y
#                              
        else:
            self.y = old_y              
                
               
    def move(self):
        """in this function the drunks move.
        
        Arguments:
            self -- agent
        
        Based on the previous functions that move the drunk in each axis, in this function they move simultaneously in both the axes. 
        In this fucntion the variable "self.is_drunk_home" is used to determine when the drunks have reached their houses.
        
        Returns:
            The drunks move and they stop once they reach their homes.
        
        """
        self.moveXaxis() 
        self.moveYaxis()
        if (self.environment[self.y][self.x] == (self.number*10)):
            self.is_drunk_home = True
        print('Drunk: ', self.number, ' Position: ', self.y, self.x, ' Environment value: ', self.environment[self.y][self.x])          
                
                
    #def createDrunkDensityMap(self):
    #    """in this function the drunks have their own density map.
        
    #    Arguments:
    #        self -- agent
        
    #   Based on the movement of the drunks, a density map is created for each of them.
        
    #    Returns:
    #        the new density map of the drunk.
        
    #    """
    #    drunk_density_map = []
    #    for j in range(len(self.environment)):
    #        drunk_density_map.append([])
    #        for i in range(len(self.environment[j])):
    #            drunk_density_map[j].append(0.0)
        
    #    return drunk_density_map
                
                
                
                
                
                
                
                
                
