from collections import defaultdict
import heapq

class Graph:
    def __init__(self,V):
        self.graph= defaultdict(list)
        self.V=V 
    
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))
    
    def shortestPath(self,src):
        pq=[]
        heapq.heappush(pq,(0,src))
        distance= [float('inf')]*V 
        distance[src]=0
        while pq:
            d,u = heapq.heappop(pq)

            for v,w in self.graph[u]:
                if distance[v]>d+w:
                    distance[v]=d+w
                    heapq.heappush(pq,(distance[v],v))
                    

        print("Short distance for the graph from {src} is", distance)






if __name__ == "__main__":
    # create the graph given in above figure
    V = 9
    g = Graph(V)

    # making above shown graph
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)
    print(g.graph)
    g.shortestPath(0)