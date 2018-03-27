"""
We define a directed graph, g, such that:
The total number of nodes in the graph is g_nodes.
The nodes are numbered sequentially as 1, 2, 3, …, g_nodes.
The total number of edges in the graph is g_edges.
Each edge connects two distinct nodes (i.e., no edge connects a node to itself).
The weight of the edge connecting nodes g_from[i] and g_to[i] is g_weight[i].
The edge connecting nodes g_from[i] and g_to[i] is directed. In other words, it describes a path only in the direction g_from[i] → g_to[i].
 
We define the weight of a path from node 1 to node g_nodes to be the sum of all edges traversed on that path.
 
Complete the minCost function in the editor below. It has four parameters:
An integer, g_nodes, denoting the number of nodes in graph g.
An array of integers, g_from, where each g_from[i] denotes the starting (source) node of the ith directed edge in graph g.
An array of integers, g_to, where each g_to[i] denotes the ending (target) node of the ith directed edge in graph g.
An array of integers, g_weight, where each g_weight[i] denotes the weight of the ith directed edge in graph g.
 
You must find the path from node 1 to node g_nodes having the minimum possible weight. You can add extra directed edges having weight 1 (one) between any two distinct nodes that are not already connected by an edge. The function must return an integer denoting the minimum possible weight of any path from node 1 to node g_nodes.
 
Input Format
Locked stub code in the editor reads the following input from stdin and passes it to the function:
The first line contains two space-separated integers describing the respective values of g_nodes and g_edges.
Each line i of the g_edges subsequent lines contains three space-separated integers describing the respective values of g_from[i], g_to[i], and g_weight[i].
 
Constraints
3 ≤ g_nodes ≤ 103
1 ≤ g_edges ≤ min(104, (g_nodes × (g_nodes − 1)) ⁄ 2)
1 ≤ g_weight[i] ≤ 106
 
Output Format
The function must return an integer denoting the minimum weight of any possible path (including one created by adding the optional additional directed edges) from node 1 to node g_nodes. This is printed to stdout by locked stub code in the editor.
 
Sample Input 0
2 1
1 2 3
 
Sample Output 0
3
 
Explanation 0
A directed edge already exists from node 1 to node 2 and the path 1 → 2 is the minimum cost path, so the function returns 3.
 
Sample Input 1
3 1
1 2 3
 
Sample Output 1
1
 
Explanation 1
As graph g has no edge between node 1 and node 3, we can add an extra edge from node 1 to node 3 having weight 1. Thus, the path 1 → 3 is the minimum weight path and the function returns 1.
 
Sample Input 2
4 4
1 2 3
1 3 3
1 4 3
2 1 3
 
Sample Output 2
3
 
Explanation 2
A directed edge already exists from node 1 to node 4 and the path 1 → 4 is the minimum cost path, so the function returns 3.
"""


# not finished
# Dijkstra
import heapq
def minCost(g_nodes, g_from, g_to, g_weight):
    W = {(s, e): w for s, e, w in zip(g_from, g_to, g_weight)}
    V = {i: [float('inf'), True] for i in range(2, g_nodes+1)}.update({1: [0, True]})  # {i: d, not_in_S}
    
    Q = heapq.heapify([(0, 1)] + [(float('inf'), i) for i in range(2, g_nodes+1)])
    S = set()
    while Q:
        ud, ui = heapq.heappop(Q)
        S.add((ud, ui))
        for vi in range(1, g_nodes):
            if vi != ui:
                if (ui, vi) in W:
                    w = W[(ui, vi)]
                elif (vi, ui) not in W:
                    w = 1
                else:
                    w = float('inf')
