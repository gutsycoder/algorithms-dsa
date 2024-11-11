from collections import deque,defaultdict 

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,node1,node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)


    def dfs(self,node,visited,order):
        if node is None:
            return 
        visited.add(node)
        order.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor,visited,order)


    def dfs_full_traversal(self):
        visited=set()
        order=[]
        for node in self.graph:

            if node not in visited:
                self.dfs(node,visited,order)

        return order
            
    


g= Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'F')
g.addEdge('E', 'F')

result = g.dfs_full_traversal()
print("dfs Traversal order is ")
print(result)