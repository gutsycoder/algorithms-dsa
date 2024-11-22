from collections import defaultdict,deque
class Graph:

    def __init__(self,V):
        self.graph = defaultdict(list)
        self.V=V 
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    

    def dfs(self,node,visited,stack):
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor,visited,stack)
        stack.append(node)
        # print(stack)
        return stack

        
    def fill_orders(self,vertex,stack):
        visited=set()
        for i in range(vertex):
            if i not in visited:
                self.dfs(i,visited,stack)
        return stack

    def reverse_graph(self):
        transformed_graph= Graph(self.V)
        for i in self.graph:
            for neighbor in self.graph[i]:
                transformed_graph.graph[neighbor].append(i)
        print(self.graph)
        print("transformed graph")
        print(transformed_graph.graph)
        self.graph=transformed_graph.graph
        return self.graph
    
    def dfs_util(self,node,visited,component):
        visited.add(node)
        component.append(node)
        for neighbor in self.graph[node]:
            if node not in visited:
                self.dfs_util(node,visited,component)
        return component
    def kosaraju_scc(self):
        stack=deque([])
        self.fill_orders(self.V,stack)
        #Reverse the graph 
        print(stack)
        self.reverse_graph()
        scc=[]
        visited=set()
        while stack:


            #Making another dfs to get the items from the stack 
            node=stack.pop()
            component=[]
            if node not in visited:
                self.dfs_util(node,visited,component)
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