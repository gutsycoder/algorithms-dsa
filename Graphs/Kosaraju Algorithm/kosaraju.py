from collections import defaultdict,deque
class Graph:
    def __init__(self,V):
        self.graph = defaultdict(list)
        self.V=V 
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    

    def dfs(self,node,visited,stack):
        visited.add(node)
        stack.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor,visited,stack)
        
    def fill_orders(self,vertex,stack):
        visited=set()
        for i in range(vertex):
            if i not in visited:
                dfs(i,visited,stack)
        return stack

    def reverse_graph(self):
        transformed_graph= Graph(self.V)
        for i in range(self.V):
            for neighbor in self.graph:
                transformed_graph.graph[neighbor].append(i)
        self.graph=transformed_graph
        return self.graph


        for i in range(self.V):
            for neighbor 



    def kosaraju_scc():
        stack=deque([])
        fill_orders(0,stack)
        #Reverse the graph 
        reverse_graph()
        scc=[]
        while stack:
            #Making another dfs to get the items from the stack 
            node=stack.pop()
            component=[]
            dfs_util(node,component)
            scc.append(component[::])
        return scc









if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    sccs = g.kosaraju_scc()
    print("Strongly Connected Components:", sccs)