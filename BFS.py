"""
input: graph G = (V, E) in adjacency-list representation,
and a vertex s ∈ V.
postcondition: a vertex is reachable from s if and only if
it is marked as "explored."
1 mark s as explored, all other vertices as unexplored
2 Q = a queue data structure, initialized with s
3 while Q is not empty do
    remove the vertex from the front of Q, call it v
    for each edge (v, w) in v's adjacency list do
        if w is unexplored then
            mark w as explored
            add w to the end of Q
"""