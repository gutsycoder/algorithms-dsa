from collections import defaultdict

def is_cyclic_util(node,graph,visited,rec_stack):
    visited.add(node)
    rec_stack.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited and is_cyclic_util(neighbor,graph,visited,rec_stack):
            return True 
        elif neighbor in rec_stack:
            return True 
    rec_stack.remove(node)
    return False 




def is_cyclic(graph,V):
    visited=set()
    rec_stack=set()


    for u in graph:
        if u not in visited and is_cyclic_util(u,graph,visited,rec_stack):
            return True 
    return False 





if __name__ == "__main__":
    V = 4
    adj = defaultdict(list)
    

    # Adding edges to the graph
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    adj[2].append(0)
    adj[2].append(3)
    adj[3].append(3)
    print(adj)

    # Function call
    if is_cyclic(adj, V):
        print("Contains Cycle")
    else:
        print("No Cycle")