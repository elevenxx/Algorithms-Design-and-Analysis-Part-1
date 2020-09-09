"""
DFS
Iterative Version
input: Graph G = (V, E) in adjacency-list representation,
and a vertex s ∈ V.
postcondition: a vertex is reachable from s if and only if
it is marked as "explored."
1 mark all vertices as unexplored
2 S = a stack data structure, initialized with s
3 while S is not empty do
    remove/pop the vertex v from the front of S
    if v is unexplored then
        mark v as explored
        for each edge (v, w) in v's adjacency list do
            add/push w to the front of S

Recursive Version
# all vertices unexplored before outer call
mark s as explored
for each edge(s, v) in s's adjacency list do
    if v is unexpected then
        DFS(G, v)
"""