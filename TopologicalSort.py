"""
input: a directed acyclic graph G = (V, E), in adjacency list representation
# output: a topological ordering of the vertices of G
postcondition: the f-values of vertices constitute a topological ordering of G
mark all vertices as unexplored
curLabel = |V|  # keep track of ordering
for every v ∈ V do
    if v is unexplored then  # in a prior DFS
        DFS-Topo(G, v)
"""