
This is the Python  Code for plotting the path from a start to goal point using a Random Tree. 
***Throughout the code single line comments and multi line comments have been used for properly understanding the code.You can go through it to understand the logic***
PYGAME Has been used for plotting the path
Other libraries used are math and random

INPUT=>

When you run it,  it asks the user following things =>
1.Enter X,Y Coordinate of the Starting point.
2.Enter X,Y Coordinate of the Goal Point
3.Enter Number of obstacles you want to put in the environment
4.Input the Coordinates of those obstacles one by one (The obstacles are represented by 30x30 rectangles and the user has to enter the coordinate of the Top-left corner of the rectangle).

ALGORITHM=>


The Algorithm is well explained using single line and multi line comments in the code, 
Let me explain here in brief :-

we have used 3 secondary functions =>1. distance =>To calculate distance between 2 points
                                   =>2. point_obs_collision=>This Function checks if a point Coordinate(x, y) is Colliding with any of the obstacles present in the Environment, if it does collide return 1
                                   =>3. Crossobstacle=>This Function checks if the line segment joining the 2 points (x1, y1) and (x2, y2) passes through any obstacle, if it does then 1 is returned else 0 ir returned
                                   
Then Comes 3 Primary Functions which performs the main task 
                                                           =>1. RRT()=>This Function takes input as Starting point, goal point, width of display window, height of display window, list of obstacles object and a goalFlag
                                                                    The goalFlag is set to 1 when the goal is reached
                                                                    The Function ReturnsX=>The List of X-Coordinates of the Nodes of the Random Tree***
                                                                                        Y=>The List of Y Coordinates of the Nodes of the Random Tree***
                                                                                        parent=>This List stores the parent of all nodes, parent[i] stores the parent of  the Child Node i
                                                                                        goalState=>Every node of the Random Tree has an identification number n, goalstate is the identification number of the goal point
                                                                                        goalFlag=>goalFlag is  1 when goal is reached otherwise 0

                                                                                        
                                                             =>2. input_output_function()=>This Function is for taking the input and Process the X, Y coordinates of the node of the random tree and the parent list obtained  from the above 
                                                                                        In the input taking part of the Function, We ask the user the starting point and the goal point Coordinates, 
                                                                                        Then we ask the user to enter the number of obstacles that the user wants to put in the environment
                                                                                        Then we ask the user to carefully enter the Coordinates of the Obstacle.Since the obstacles will be represented by the rectangles therefore the user needs to enter the coordinates of the top-left corner of the rectangle
                                                                                        For the record, Though the starting point and Goal Point are represented By Point Coordinates, we represent them by a Circle of radius 20pixels
                                                                                        The center of this 20pixel radius circle is the actual starting and goal point , not the entire circle.So be careful.Drawing a bigger circle around starting and goal point is just for visual clarity
                                                                                        Moreover each of the Obstacles are represented by the 30x30 Rectangle whose coordinate of the top-left corner is the coordinate entered by the user, The user can create as many obstacles as he wants
                                                                                        But incase the rectangular obstacle collides with starting point or goal point we ask the user to enter the value of the coordinates again
                                                                                        By obstacle colliding with the starting or goal point,what  we mean is  colliding with the CENTRE of that 20pixel radius bigger Circle around the starting or goal point , not that circle itself
                                                                                        This function then process the output of RRT Function and returns path list which is the list of the coordinates of the node on the final  path from start to goal
                                                                                        Along with that it also returns the start, goal point coordinates and the list of obstacles***


                                                               =>3. draw()=>This Function is just to use pygame class and functions to draw start and goal point, the obstacles  and The final path from start to goal
                                                                         It uses the output from input_output_function above to draw the same 
                                                                         Start and goal point coordinates are represented by 20 pixels radius green and red circle respectively, but importantly remember that the start and goal point
                                                                         are actually the center of those circles, not the circle itself
                                                                         The point coordinates of the nodes along the path has been shown by a red circle of just 1pixel(comparable to dot)

To execute the code we need to just call the Draw Function 

OUTPUT=> We will the see the plotted path in Pygame display window 

FOR COMPILATION AND RUN IN UBUNTU(I don't use ubuntu but as per my experience of using it in Computational phyics lab) =>
in the prompt=> 
write =>python RRT.py


It should run, If it does not please let me know 




    

                                                                                        
                                                                                        




                        
                      


  
