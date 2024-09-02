
#Requirements
Python (Ensure pygame, math, and random libraries are installed)<br>
#Usage
Run the Script: Execute python RRT.py.<br>
Provide Inputs:<br>
Start Point: Enter X, Y coordinates.<br>
Goal Point: Enter X, Y coordinates.<br>
Number of Obstacles: Enter the number of obstacles.<br>
Obstacle Coordinates: Enter the top-left corner coordinates for each obstacle (30x30 rectangles). The script ensures obstacles do not collide with start or goal points.<br>
#Function Overview
RRT(): Generates the random tree and attempts to connect the start point to the goal.<br>
input_output_function(): Handles user input and processes the generated path.<br>
draw(): Visualizes the start, goal, obstacles, and final path in a Pygame window.<br>
#Output
The path from start to goal is displayed in a Pygame window, with:<br>

Start point: Green circle<br>
Goal point: Red circle<br>
Obstacles: 30x30 rectangles<br>
Path: Red dots<br>
                                                                                        




                        
                      


  
