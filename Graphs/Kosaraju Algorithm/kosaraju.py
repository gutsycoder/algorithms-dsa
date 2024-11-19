from collections import defaultdict,deque
class Graph:
    def __init__(self,V):
        self.graph = defaultdict(list)
        self.V=V 
    
    def add_edge(u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    

    def dfs(node,stack):





    def kosaraju_scc():
        stack=deque([])
        fill_orders(0,stack)
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