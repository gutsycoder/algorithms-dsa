Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.
For example, a topological sorting of the following graph is “5 4 2 3 1 0?. There can be more than one topological sorting for a graph. For example, another topological sorting of the following graph is “4 5 2 0 3 1″. The first vertex in topological sorting is always a vertex with an in-degree of 0 (a vertex with no incoming edges).

ALGORITHM FOR FINDING THE TOPOLOGICAL SORT USING KAHN'S ALGORITHM OR BFS

1. Compute the Indegree(number of incoming edges) for each vertex V present in the DAG and initialize the count of visited node as 0
2. Pick all the vertices with indegree 0 and put them in queue 
3. Remove the vertex from the queue and then :-
  a.We save the vertex in an array , topological_order.
  b.Increment the count of visited by 1 
  c.Decrease the in-degree by 1 of all it's neighboring nodes
  d.If the in-degree of any of the neighboring node becomes 1 , add it to the queue 

4. Repeat step 3 until the queue is empty 
5. If the count of the visited nodes is not equal to total vertex , then topological ordering is not possible as the graph contains the cycle .
6. If the graph has no cycle, then we print the topological_order array.