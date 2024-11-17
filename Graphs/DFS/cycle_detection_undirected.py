from collections import defaultdict 


def is_cyclic_util(node,graph,visited,parent):
    visited[node]=True 
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if is_cyclic_util(neighbor,graph,visited,node):
                return True
        
        elif neighbor!=parent:
            return True
    return False 


def is_cyclic(V,graph):

    visited=[False]*V 
    for u in range(V):
        if not visited[u]:
            if is_cyclic_util(u,graph,visited,-1):
                return True 
    return False 







if __name__=="__main__":
    V = 3
    adj = [[] for _ in range(V)]

    adj[1].append(0)
    adj[0].append(1)
    adj[0].append(2)
    adj[2].append(0)
    adj[1].append(2)
    adj[2].append(1)
    print("Contains cycle" if is_cyclic(V, adj) else "No Cycle")

    V = 3
    adj2 = [[] for _ in range(V)]

    adj2[0].append(1)
    adj2[1].append(0)
    adj2[1].append(2)
    adj2[2].append(1)

    print("Contains Cycle" if is_cyclic(V, adj2) else "No Cycle")