The Rapidly-exploring Random Tree (RRT) algorithm is a path-planning method designed to efficiently explore high-dimensional spaces. It incrementally builds a tree by randomly sampling the search space, extending branches toward unexplored regions, and connecting them to the nearest node in the tree. RRT is particularly effective for solving complex motion planning problems in robotics and other applications where finding a path from start to goal in the presence of obstacles is challenging.<br>
#Requirements
Python <br>
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
                                                                                        




                        
                      


  
