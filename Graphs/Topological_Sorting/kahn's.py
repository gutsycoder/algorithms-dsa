#IMPLEMENTATION OF TOPOLOGICAL SORTING USING KAHN'S ALGORITHM
#Source :- https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/



from collections import defaultdict,deque 

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing the adjace
        self.V= vertices

