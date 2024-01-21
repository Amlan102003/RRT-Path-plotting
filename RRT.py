import math 
import pygame 
import random 
import sys

red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
grey=(70, 70, 70)
white=(255, 255, 255)

#This Function calculates the distance between 2 Point Coordinates (X1, Y1) and (X2, Y2)
def distance(x1, y1, x2, y2):
    return math.sqrt((float(x1)-float(x2))**2 + (float(y1)-float(y2))**2)

#This Function checks if a point Coordinate(x, y) is Colliding with any of the obstacles present in the Environment, if it does collide 1 
def point_obs_collision(x, y, obstacleslist):
    
    for i in range(0, len(obstacleslist)):
        rectangle=obstacleslist[i]
        if(rectangle.collidepoint(x, y)):
            return 1
        
    return 0

#This Function checks if the line segment between the 2 points (x1, y1) and (x2, y2) passes through any obstacle, if it does then 1 is returned else 0 ir returned

def Crossobstacle(x1, y1, x2, y2, obstacleslist):
    obs = obstacleslist.copy()
    while(len(obs)>0):
        rectangle=obs.pop()
        for i in range(0, 101):
            u=i/100
            x=x1*u+x2*(1-u)
            y=y1*u+y2*(1-u)
            if(rectangle.collidepoint(x, y)):
                return 1
            
    return 0


    
        
            



    
                



#This Function takes input as Starting point, goal point, width of display window, height of display window, list of obstacles object and a goalFlag
#The goalFlag is set to 1 when the goal is reached

#The Function Returns X=>The List of X-Coordinates of the Nodes of the Random Tree
                      #Y=>The List of Y Coordinates of the Nodes of the Random Tree
                      #parent=>This List stores the parent of all nodes, parent[i] stores the parent of  the Child Node i
                      #goalState=>Every node of the Random Tree has an identification number n, goalstate is the identification number of the goal point
                      #goalFlag=>goalFlag is  1 when goal is reached otherwise 0
                      
def RRT(Start, target, display_window_width, display_window_height, obstacleslist, goalFlag):
    
    
    
    start=Start
    goal=target
    goalstate=0 #goalstate is 1st declared here, later updated when the goal is reached
    
   
    disp_width=display_window_width
    disp_height=display_window_height
    step_size=35 #This is the length of the edge(line segment) between 2 directly connected nodes of a tree, distance between 2 nodes which are directly 
    #connected
   
    
    (xo, yo)= start
    
    
    
    
    
    
    
    
     
    X=[]#An empty list is create to store the X Coordinates of the nodes of the  random tree during traversal/expansion
    Y=[]#An empty list created to store the Y Coordinate of the nodes of the  random tree during expansion 
    X.insert(0,xo)
    Y.insert(0, yo)
    
    parent=[]#parent[i] is to store the parent of child node i of the random tree
    parent.append(0)
    
    
    
    
   
    
    #The obstacles will be represented by rectangles, The coordinates of the top-left corner of all the obstacles that the user wants to put in the path will be taken as input
    #Those coordinates as input from user will be stored in list obs-coord_lst_useinp as tuples
    #rectangles after being created will be stored in the obstacleslist
    #The number of obstacles is decided by the length of the obs_coord_userinp
    
    
    
   
        
    iterations=0 #it keeps track of the number of times a randomly sampled point node is created, checked if it meets the required conditions then 
    #judgement is made whether to add this to the list of Nodes or To discard it in case some of the conditions are not met
    
    #The while loop below has 2 Parts.Let us explain each of the parts properly
    
    ''' Part 1=> when iterations is not a multiple of 10 =>
    If this is the case we first get the current number of nodes already present in the constructed random tree from len(X),denoted by n. Then 
    we randomly generate the X and Y Coordinate, (X,Y) whose identification is gonna be n as it is the nth node if we see the order of generation
    of nodes.If the point (X, Y ) Lies inside any of the obstacles in the environment then it is discarded and the Coordinates are randomly 
    generated once again.
    This loop goes on until we get a point(X,Y) Which does not lie inside the obstacle. The obstacle will be represented by the rectangle
    For the Randomly generated point(X,Y) above, we loop through the current list of nodes already present in the tree and Find out which of them is closest to the 
    Randomly generated point(X,Y) Above. Let it be denoted by Xnear and Ynear with identification number nnear
    Then as we have mentioned above, the step size, that is the line segment joining any 2 Nodes should not be greater than the step size
    So we check if the distance between (X, Y) and (Xnear, Ynear) is greater than or smaller than the step size.If it is greater than the step size
    we find a point (Xo, Yo) which lies on the line joining (X, Y) and (Xnear, Ynear) and is at a distance =
    step size from (Xnear, Ynear).After getting (Xo, Yo) we discard (X, Y) from the list and Check if the point
    (Xo, Yo) does not lie inside the obstacle and the line segment joining (Xo, Yo) and (Xnear, Ynear) does not pass through any obstacle.
    If these conditions are met we draw the edge between (Xnear, Ynear) and (Xo, Yo) and add (Xo, Yo) To the random tree.
    if it does not we move to the next iteration of the while loop. '''
    
    
    ''' Part 2=>>when iteration is a multiple of 10
    This part is used for biasing the movement from start to goal towards the goal point.But here we do not randomly generate (X, Y) as we did in part 1.Instead we use goal point coordinates Xgoal, Ygoal instead of X, Y
    Then We find Xnear, Ynear as in part 1, which are the coordinates of the already added/present node of the random tree that is nearest to the goal point.
    If the distance between the goal point and (Xnear, Ynear) is less than step size and there is no obstacle on the path joining (Xnear, Ynear) and goal.We add goal to the list of the nodes of the random tree and hence the goal is reached
    but if the distance between goal point and (Xnear, Ynear) is more than step size orelse there is an obstacle inbetween them on the path joining them we introduce another point (Xo, Yo) as in part 1 which lies on the path joining goal point and (Xnear, Ynear) and is at a distance=step size from the (Xnear, Ynear) and check if there are no obstacles on the path joining (Xnear, Ynear) and (Xo, Yo).
    if conditions are met (Xo, Yo) is added to the list of nodes of the random tree, If not met we move to the next iteration of the while loop
    '''
    #The maximum number of iterations has been set to 5000 to stop the code from entering into infinite loop if a path does not exist
    #Also in this loop once a goal is reached following the above explained algorithm goalflag is set to 1 
    #The returned data are List of X, Y Coordinates of the Nodes of the Tree
    
     
    while(goalFlag==0 and iterations<5000):
        
        iterations=iterations+1
        
        if(iterations%10!=0): 
            
            n=len(X)

            flag=1
            while(flag==1):
                x = int(random.uniform(0, disp_width))
                y=int(random.uniform(0, disp_height))
                flag = point_obs_collision(x, y, obstacleslist)
                if(flag==0):
                    X.insert(n, x)
                    Y.insert(n, y)
                    break
                
            
                    
            nearestnode=0
            mindist=distance(x, y, xo, yo)
            for i in range(0, n):
                a=X[i]
                b=Y[i]
                if(mindist>distance(x, y, a, b)):
                    mindist=distance(x, y, a, b)
                    nearestnode = i
                    
                    
                    
            
            d=distance(X[nearestnode], Y[nearestnode], x, y)
            if(d> step_size):
                
                xnear=X[nearestnode]
                ynear=Y[nearestnode]
                
                dy= y- Y[nearestnode]
                dx= x-X[nearestnode]
                theta=math.atan2(dy, dx)
                x=int(xnear+ (step_size)*math.cos(theta))
                y=int(ynear+(step_size)*math.sin(theta))
                X.pop(n)
                Y.pop(n)
                if(math.sqrt((x-goal[0])**2+(y-goal[1])**2) <= 35 and Crossobstacle(xnear, ynear, x, y, obstacleslist)==0 and Crossobstacle(x, y, goal[0], goal[1], obstacleslist)==0):
                    
                    
                    X.insert(n, x)
                    Y.insert(n, y)
                    X.insert(n+1, goal[0])
                    Y.insert(n+1, goal[1])
                    parent.insert(n, nearestnode)
                    parent.insert(n+1, n)
                    goalstate=n+1
                    goalFlag=1
                    return X, Y, parent, goalstate, goalFlag
                    
                else:
                    X.insert(n, x)
                    Y.insert(n, y)
                    
            
            
            
                    
            X1, Y1= xnear, ynear
            X2, Y2=X[n], Y[n]
            if(Crossobstacle(X1, Y1, X2, Y2, obstacleslist)==1):
                X.pop(n)
                Y.pop(n)
            else:
                parent.insert(n, nearestnode)
                
                
        else:
            
            n=len(X)
            X.insert(n, goal[0])
            Y.insert(n, goal[1])
            x=X[n]
            y=Y[n]
            
            
            nearestnode=0
            mindist=distance(x, y, xo, yo)
            for i in range(0, n):
                a=X[i]
                b=Y[i]
                if(mindist>distance(x, y, a, b)):
                    mindist=distance(x, y, a, b)
                    nearestnode = i
                    
                    
            
            d=distance(X[nearestnode], Y[nearestnode], x, y)
            if(d> step_size):
                
                xnear=X[nearestnode]
                ynear=Y[nearestnode]
                
                dy= y- Y[nearestnode]
                dx= x-X[nearestnode]
                theta=math.atan2(dy, dx)
                x=int(xnear+ (step_size)*math.cos(theta))
                y=int(ynear+(step_size)*math.sin(theta))
                
                X.pop(n)
                Y.pop(n)
                if(math.sqrt((x-goal[0])**2+(y-goal[1])**2)<=35 and Crossobstacle(xnear, ynear, x, y, obstacleslist)==0 and Crossobstacle(x, y, goal[0], goal[1], obstacleslist)==0):
                    X.insert(n, x)
                    Y.insert(n, y)
                    X.insert(n+1, goal[0])
                    Y.insert(n+1, goal[1])
                    goalstate=n+1
                    parent.insert(n+1, n)
                    parent.insert(n, nearestnode)
                    goalFlag=1
                    return X, Y, parent, goalstate, goalFlag
                    
                else:
                    X.insert(n, x)
                    Y.insert(n, y)
                    
            
                     
            X1, Y1= xnear, ynear
            X2, Y2=X[n], Y[n]
            if(Crossobstacle(X1, Y1, X2, Y2, obstacleslist)==1):
                X.pop(n)
                Y.pop(n)
            else:
                parent.insert(n, nearestnode)
                
                

#This Function is for taking the input and Process the X, Y coordinates of the node of the random tree and the parent list obtained  from the above 
#In the input taking part of the Function, We ask the user the starting point and the goal point Coordinates, 
#Then we ask the user to enter the number of obstacles that the user wants to put in the environment
#Then we ask the user to carefully enter the Coordinates of the Obstacle.Since the obstacles will be represented by the rectangles therefore the user needs to enter the coordinates of the top-left corner of the rectangle
#For the record, Though the starting point and Goal Point are represented By Point Coordinates, we represent them by a Circle of radius 20pixels
#The center of this 20pixel radius circle is the actual starting and goal point , not the entire circle.So be careful.Drawing a bigger circle around starting and goal point is just for visual clarity
#Moreover each of the Obstacles are represented by the 30x30 Rectangle whose coordinate of the top-left corner is the coordinate entered by the user, The user can create as many obstacles as he wants
#But incase the rectangular obstacle collides with starting point or goal point we ask the user to enter the value of the coordinates again
#By obstacle colliding with the starting or goal point,what  we mean is  colliding with the CENTRE of that 20pixel radius bigger Circle around the starting or goal point , not that circle itself










def input_output_function():
    
    
    
    
    

    
    
    
    
    print("Enter the X Coordinate(integer/decimal values) of the starting point, should lie between 0 to 1000")
    start_X= int(input())
    print("Enter Y-Coordinate(integer/decimal values) of the starting point, should lie between 0 to 600")
    start_Y=int(input())
    start=(start_X, start_Y)
    
    print("Enter the X Coordinate(integer/decimal values) of the Goal point, should lie between 0 to 1000")
    goal_X= int(input())
    print("Enter Y-Coordinate(integer/decimal values) of the Goal point, should lie between 0 to 600")
    goal_Y=int(input())
    goal=(goal_X, goal_Y)
    
    
   
    goalFlag=0
    
    obs_coord_lst_userinp=[]
    
    print("Enter the number of obstacles that you wanna put in the environment")
    no_of_obs=int(input())
    count_of_obs=no_of_obs
    print("please read the below instructions before entering ")
    print("Obstacles will be represented by (30pixels x 30pixels) rectangle.You need to enter the coordinates of the top-left corner of the rectangle.If the obstacle created with that coordinates overlap with the start or goal point it will be discarded and you will have to enter the valid coordinates again.")
    print("Also make sure  that X-Coordinate lies between 0 to 1000 and Y-Coordinate should lie between 0 to 600, which is the size of the display window")
    while(no_of_obs>0):
        i=count_of_obs-no_of_obs+1
        print(f"Enter the X-Coordinate of the obstacle {i}, range  is 0-1000")
        x_coord= int(input())
        print(f"Enter the Y-Coordinate of the obstacle {i}, range is 0-600")
        y_coord=int(input())
        obs_coord=(x_coord, y_coord)
        rectangle=pygame.Rect(obs_coord, (30, 30))
        if(rectangle.collidepoint(start) or rectangle.collidepoint(goal)): 
            #This Condition checks if the obstacle created by user collides with the
            #start and goal point if it does it asks the user to enter the Coordinates again
            
            print(f"The rectangular 30x30 obstacle with coordinates of top-left corner as {x_coord}, {y_coord} collide with the start and goal coordinates")
            print(f"Please enter again the coordinates of the obstacle {i+1}")
        else:
            no_of_obs=no_of_obs-1
            obs_coord_lst_userinp.append(obs_coord)
     
     
    '''in the below while loop, we append the rectangle object(obstacles) in the obstacleslist.This list is to be returned later'''
    obstacleslist=[]       
    count_obs=0
    while(count_obs<count_of_obs):
        x,y=obs_coord_lst_userinp.pop()
        rectangle=pygame.Rect((x,y), (30, 30))
        obstacleslist.append(rectangle)
        count_obs=count_obs+1
        
    
    
   
    #Calling the function RRT      
    X, Y, parents, goalstate, goalFlag= RRT(start, goal, 1000, 800, obstacleslist, goalFlag)
    
    #This if else paragraph of the function process the parents and X, Y Lists obtained from calling the RRT Function 
    #The processing is done as Follows
    '''we declare an empty list start_to_goal_path, then we use the parents list to retrieve the identification number of the nodes(point coordinate ) from goal to start point
    then we declare an empty list start_to_goal_path_Coords to store (x,y)coordinates of the node in the final path from start to goal.
    We use X, Y and start_to_goal-path list to make it.Refer the code below to know more
    
    '''
    
    
    
    if(goalFlag==0):
        print("No path exists")
    else:
        
        start_to_goal_path=[]
        start_to_goal_path.append(goalstate)
        Node= parents[goalstate]
        while(Node!=0):
            start_to_goal_path.append(Node)
            Node=parents[Node]
            
        start_to_goal_path.append(0)
        
        start_to_goal_path_Coords=[]
        for node in start_to_goal_path:
            x=X[node]
            y=Y[node]
            start_to_goal_path_Coords.append((x,y))
        path=start_to_goal_path_Coords.copy()
            
            
        
            
            
     
            
            
        
        
    return start, goal, obstacleslist, path
        

    
    
#This Function is just to use pygame class and functions to draw start and goal point, the obstacles  and The final path from start to goal
#It uses the output from input_output_function above to draw the same 
#Start and goal point coordinates are represented by 20 pixels radius green and red circle respectively, but importantly remember that the start and goal point
#are actually the center of those circles, not the circle itself 
#The point coordinates of the nodes along the path has been shown by a red circle of just 1pixel(comparable to dot)

def Draw():
    
    pygame.init()
    start, goal, List_obs, path=input_output_function()
    
    
    disp_window=pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Rapidly exploring Random Tree")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        disp_window.fill(white)
        pygame.draw.circle(disp_window, green, start, 20)
        pygame.draw.circle(disp_window, red, goal, 20)

        while len(List_obs) > 0:
            rectangle = List_obs.pop()
            pygame.draw.rect(disp_window, grey, rectangle)
            pygame.display.update()

        while len(path) > 1:
            x, y = path.pop()
            xo, yo = path[-1]
            pygame.draw.circle(disp_window, red, (x, y), 1)
            pygame.display.update()
            pygame.draw.line(disp_window, blue, (x, y), (xo, yo), 2)
            pygame.display.update()

            if len(path) == 1:
                break

        
    





Draw()#We execute the entire code here




    
    
        
            
            
            
            
        
    
    
    
    
    
    
    
    
    
    
                    
            
                    
            
            
            
            
            
            
                
                
        
                
                
                
                
            
                
                
                
                
                    
                
                    
                
                
                
                    
                    
                    
                    
                    
                
                
                
                
                
                
                    
            
                    
            
                    
            
                    
                    
               
                    
                    
                
                    
                
                    
                
           
                    
            
                    
            
                    
                
            
            
            
            
            
        
            
        
        
        
    
    
        
    
        
        
    
        
        
        
        
        
      
    
            
            
            
           
                
                
                    
                    
            
                    
            
          
            
            
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    


