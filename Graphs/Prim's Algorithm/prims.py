import heapq 
from collections import defaultdict 

def MST(V,E,edges):
    graph = defaultdict(list)
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    pq=[]
    heapq.heappush(pq,(0,0))
    visited=set()
    res=0
    
    while pq:
        w,u = heapq.heappop(pq)
        if u in visited: #For duplication , as it might be possible that it got inserted 2 times as we mark visited only when process it
            continue
        res+=w
        visited.add(u)
        for v,w in graph[u]:
            if v not in visited:
                heapq.heappush(pq,(w,v))
    return res










if __name__ == "__main__":
    graph = [[0, 1, 5],
             [1, 2, 3],
             [0, 2, 1]]
    # Function call
    print(MST(3, 3, graph))