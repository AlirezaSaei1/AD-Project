# AD-Project
Algorithm Design Final Project, solving multiple real world problems. This Project is made up of 3 tasks:

Task 1 (Parking Lot Empty Target Location)
---
In this task, parking lot information is given that contains:
1. Security Camera (Marked with C)
2. Target Place (Needs to be emptied)
3. Empty Places (Marked with 0)
4. Car Locations (Marked with 1 to number of cars)

It is requested to empty the target place. Back Tracking method is used to find the answer with minimum car movements. (Car sizes range can be [1, n])


Task 2-1 (Source To Destination)
---
In this task, with given source (Parking) and destination (User input), must find and declare shrotest path between two.
There can be multiple paths and all paths are printed using Dijkstra method and storing all possible paths in parent array.


Task 2-2 (Visiting Places)
---
In this part, a start location is given and some other location are received as visiting places (Intermediate Nodes).
Shortest path is found from source to all intermediate locations and returning to source using TSP (Travelling Salesman Problem) Back Tracking Method.


Task 3 (Road Reconstruction)
---
In Final Task, It is requested to re-arrange streets in a way that all locations are accessible and length is minimum, too.
This task is solved by finidng minimum spanning tree using Greedy MST finding algorithm (PRIM).


Contributers:
---
Alireza Dastmalchi Saei__
Ali Ebrahimi
