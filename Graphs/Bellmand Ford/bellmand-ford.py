







def bellmanFord(V,edges,src):
    dist = [float('inf')]*V 
    dist[src]=0

    for i in range(V):
        for edge in edges:
            u,v,wt=edge 
            # Write the logic for relaxation of the edge 
            if dist[u]+wt<dist[v]:
                dist[v]=dist[u]+wt
                if i==V-1:
                    return None
    return dist








if __name__=="__main__":
    V=5
    edges= [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
    src=0
    ans = bellmanFord(V,edges,src)
    if not ans:
        print("Negative Cycle Detected")
    print(' '.join(map(str,ans)))

