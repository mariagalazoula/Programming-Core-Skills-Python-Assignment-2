# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:28:53 2018

@author: gy16mg
"""


#Create an Agent Class, where we will give the agents all of the 
#attributes that they will need for this model. First, we create the 
#agents by creating an initial function called __init__, where we 
#assign the attributes of the agents, such as the neighbourhood, 
#environment, etc and we also create the functions needed for this model,
#in order to move the agents, to make them eat, to calculate 
#the distances between the agents and to make them share with their neighbours.

import random  

#create the class for the agents:
class Drunk:
    
#create the agents and their attributes
    def __init__(self, x_pub, y_pub, number, environment,drunks):
        """In this __init__ we initialise 
        """
        self.x = x_pub
        self.y = y_pub
        self.number = number
        self.environment = environment
        self.drunks = drunks      
        self.is_drunk_home = False
        
        self.drunk_density_map = self.createDrunkDensityMap()

#function for moving the agents using the Torus, where the modulus operator is used          
#    def move(self):
#        """Through this function we move the agents through the
#        environment. However, each drunk has to stop the movement when they reach
#        the house with the same number as them, multiplied by 10, i.e 
#        drunk 1 to house 10, drunk 2 to house 20, drunk 3 to house 30 etc. 
#        We will also check the new position of the drunks in case they get out of the 
#        environment.
#        
#        """
#        if (random.random()<0.5): 
#            #the cell environment[self.y][self.x] is the one that we are right now, the 
#            #environment[self.y][self.x+1] is the next one that we will move to using this condition of random
#            #if environment[self.y][self.x+1] == 0
#            if self.x<len(self.environment) and self.x >0: 
#                if (self.environment[self.y][self.x+1] == 0 or self.isDrunkHome(self.y, self.x+1)):
#                    self.x = (self.x + 1)
#            else:
#                self.x = self.x
#        else: #for random>0.5
#            if self.x<len(self.environment) and self.x >0: 
#                if (self.environment[self.y][self.x-1] == 0 or self.environment[self.y][self.x-1] == (self.number*10)):
#                    self.x = (self.x - 1)
#            else:
#                self.x = self.x   
#                
#        if (random.random()<0.5):
#            if self.y<len(self.environment[0]) and self.y >0: 
#                if (self.environment[self.y+1][self.x] == 0 or self.environment[self.y+1][self.x] == self.number*10):
#                    self.y = (self.y + 1)
#            else:
#                self.y = self.y 
#        else:
#            if self.y<len(self.environment[0]) and self.y >0: 
#                if (self.environment[self.y-1][self.x] == 0 or self.environment[self.y-1][self.x] == self.number*10):
#                    self.y = (self.y - 1)
#            else:
#                self.y = self.y
#                
#        if (self.isDrunkHome(self.x, self.y)):
#            self.is_drunk_home = True
#            
#        print('Drunk: ', self.number, ' Position: ', self.x, self.y, ' Environment value: ', self.environment[self.x][self.y])            
#        
#        
#    def isDrunkHome(self, x, y):
#        print ('Drunk place? ', self.environment[self.y][self.x] == self.number*10)
#        return self.environment[x][y] == self.number*10
            
   
        
        
            
            
    def moveXaxis(self):
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
            #if (self.drunk_density_map[self.y][new_x] == 0):
            self.x = new_x
                #self.drunk_density_map[self.y][self.x] = self.drunk_density_map[self.y][self.x] +1
#            else:
#                self.x = old_x
        else:
            self.x = old_x
        
    
    def moveYaxis(self):
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
            #if (self.drunk_density_map[new_y][self.x] == 0):
            self.y = new_y
#                self.drunk_density_map[self.y][self.x] = self.drunk_density_map[self.y][self.x] + 1
#            else:
            #self.y = old_y              
        else:
            self.y = old_y              
                
#    def correctXaxis(self):
#        if self.x<0:
#            self.x = 0
#        if self.x>len(self.environment)-1:
#            self.x = len(self.environment)-1
#    
#    def correctYaxis(self):
#        if self.y <0:
#            self.y = 0
#        if self.y> len(self.environment[0])-1:
#            self.y = len(self.environment[0])-1
               
    def move(self):
        self.moveXaxis() 
        self.moveYaxis()
        if (self.environment[self.y][self.x] == (self.number*10)):
            self.is_drunk_home = True
        print('Drunk: ', self.number, ' Position: ', self.y, self.x, ' Environment value: ', self.environment[self.y][self.x])          
                
                
    def createDrunkDensityMap(self):
        drunk_density_map = []
        for j in range(len(self.environment)):
            drunk_density_map.append([])
            for i in range(len(self.environment[j])):
                drunk_density_map[j].append(0.0)
        
        return drunk_density_map
                
                
                
                
                
                
                
                
                