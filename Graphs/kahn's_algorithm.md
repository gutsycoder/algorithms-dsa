# Topological Sorting for Directed Acyclic Graph (DAG)

Topological sorting for a Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. It is not possible to perform topological sorting for a graph if it is not a DAG.

For example, a topological sorting of the following graph is “5 4 2 3 1 0”. There can be more than one topological sorting for a graph. Another topological sorting of the same graph can be “4 5 2 0 3 1”. The first vertex in topological sorting is always a vertex with an in-degree of 0 (a vertex with no incoming edges).

## Algorithm for Finding Topological Sort using Kahn's Algorithm or BFS

1. Compute the in-degree (number of incoming edges) for each vertex V present in the DAG and initialize the count of visited nodes as 0.

2. Pick all the vertices with in-degree 0 and put them in a queue.

3. Remove the vertex from the queue and then:
    - Save the vertex in an array, `topological_order`.
    - Increment the count of visited by 1.
    - Decrease the in-degree by 1 of all its neighboring nodes.
    - If the in-degree of any of the neighboring nodes becomes 0, add it to the queue.

4. Repeat step 3 until the queue is empty.

5. If the count of the visited nodes is not equal to the total number of vertices, then topological ordering is not possible as the graph contains a cycle.

6. If the graph has no cycle, then print the `topological_order` array.
