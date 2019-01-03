## GEOGM Programming for Social Sciences: Core Skills - Assignment 2
This is the repository for the second assignment in GEOGM Programming for Social Sciences: Core Skills, as part of the Integrated MSc and PhD in Data Analytics and Society that I am currently enrolled in. It consists of the code of the agent-based model that was created for a town in order to model the movements of drunks from a pub to their houses.

## DESCRIPTION
In this assignment we are required to create an agent-based model. We create 25 agents/drunks by giving them various attributes such as: their initial coordinates,which is the location of the pub, the environment they move in. First, the agent 1 leaves the pub and moves until he finds the house number, and then the next drunk begins moving until all the drunks are at their houses. The agents move freely in the environment/town, however, this movement is defined by a random number that is generated in each iteration with the restriction that they cannot get out of the dimensions of the environment and they can only go inside their own houses, in order to make the model more realistic. The environment is provided in the details of the assignment, with the name "drunk.plan.txt".

## FURTHER DETAILS

* The agents are aware of the environment that they are in.
* The agents are assigned the coordinates of the pub.
* In the class **Drunks_Framework.py** the drunks/agents are given their attributes, such as their coordinates and the movements that they are allowed are defined in the functions `moveXaxis`, `moveYaxis` and `move` .
* Finally, in the **Model_for_drunks.py**, the drunks are generated and move throughout the town starting from the pub until they find their houses. 
