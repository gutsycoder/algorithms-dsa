
from collections import deque

def add_edge(graph,u,v):
    graph[u].append(v)


def is_cyclic(V,graph):

    in_degree=[0]*V 
    queue=deque()
    visited=0

    for u in range(V):

        for v in graph[u]:
            in_degree[v]+=1
     #enqueu all the vertices with 0 in degreee


    for u in range(V):

        for v in graph[u]:
            if in_degree[v]==0:
                queue.append(v)
    while queue:
        node = queue.popleft()
        visited+=1
        for neighbor in graph[node]:

            in_degree[neighbor]-=1
            if in_degree[neighbor]==0:
                queue.append(node)
    return visited!=V












if __name__ == "__main__":
    V = 6
    adj = [[] for _ in range(V)]

    # Adding edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 4, 1)
    add_edge(adj, 4, 5)
    add_edge(adj, 5, 3)

    # Function call to check for cycles
    if is_cyclic(V, adj):
        print("Contains cycle")
    else:
        print("No Cycle")