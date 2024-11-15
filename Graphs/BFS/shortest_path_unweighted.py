from collections import deque,defaultdict

def bfs(graph,S,par,dest):
    q=deque([S])
    dest[S]=0
    
    while q:
        node = q.popleft()
        
        for neighbor in graph[node]:
            if dest[neighbor]==float('inf'):
                q.append(neighbor)
                dest[neighbor]=dest[node]+1
                par[neighbor]=node

def print_shortest_distance(graph,S,D,V):
    par=[-1]*V 
    dest=[float('inf')]*V 

    bfs(graph,S,par,dest)
    if dest[D]==float('inf'):
        print("Source And Destination Are Not Connected")
        return 
    
    path=[]
    current_node=D 
    path.append(D)
    while par[current_node]!=-1:
        current_node=par[current_node]
        path.append(current_node)
        

    for i in range(len(path)-1,-1,-1):
        print(path[i],end=" ")









if __name__=="__main__":
    V=8
    source,destination = 2,6
    edges = [
        [0, 1], [1, 2], [0, 3], [3, 4],
        [4, 7], [3, 7], [6, 7], [4, 5],
        [4, 6], [5, 6]
    ]
    graph=defaultdict(list)

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    print_shortest_distance(graph,source,destination,V)
