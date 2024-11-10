from collections import deque,defaultdict 

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,node1,node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)


    def bfs(self,start_node):
        if start_node is None: return 
        queue = deque([start_node])
        order=[]
        visited=set()
        visited.add(start_node)
        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return order
            
    


g= Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'F')
g.addEdge('E', 'F')

result = g.bfs('A')
print("BFS Traversal order is ")
print(result)