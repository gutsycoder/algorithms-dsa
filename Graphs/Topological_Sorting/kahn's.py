#IMPLEMENTATION OF TOPOLOGICAL SORTING USING KAHN'S ALGORITHM
#Source :- https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/



from collections import defaultdict,deque 

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing the adjacency list 
        self.V= vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topologicalSort(self):

        indegree= [0]*self.V 
        

        for node in self.graph:
            for neighbor in self.graph[node]:
                indegree[neighbor]+=1
        queue=deque([])
        count_visited=0
        for node in range(self.V):
            if indegree[node]==0:
                queue.append(node)
        topological_order=[]
        while queue:
            node = queue.popleft()
            topological_order.append(node)
            count_visited+=1
            for neighbor in self.graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
                
        if count_visited!=self.V:
            print("There Exists A Cycle In The Graph. Hence, Can't Be Sorted Topologically")
        else:
            print(topological_order)


g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
 
print ("Following is a Topological Sort of the given graph")
g.topologicalSort()


