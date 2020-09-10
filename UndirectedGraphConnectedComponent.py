"""
input: undirected graph G = (V, E) in adjacency list
representation, with V = {1, 2, 3, ..., n}
postcondition: for every u, v ∈ V, cc(u) = cc(v) if
and only if u, v are in same connected component.
algorithm:
mark all vertices as unexplored
numCC = 0
for i = 1 to n do
    if i is unexpected then
        numCC ++
        # call BFS starting at i
        Q: a queue data structure, initialized with i
        while Q is not empty do
            remove the vertex from the front of Q, call it v
            cc(v) = numCC
            for each (v, w) in v's adjacency list do
                if w is unexplored then
                    mark w as explored
                    add w to the end of Q
"""