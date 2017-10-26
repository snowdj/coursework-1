#!/usr/bin/env python3
"""
Algorithms on graphs.
"""


def BFS(s, adj):
    """
    Code from MIT 6.006 Fall 2011, Lec 13 BFS.
    https://www.youtube.com/watch?v=s-CYnVz-uh4 34:10
    Time: \theta(V+E)

    :param s: starting vertex
    :param adj: adjacency lists representing a graph
    """
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        next_ = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next_.append(v)
        frontier = next_
        i += 1


def DFS(V, adj):
    """
    Code from MIT 6.006 Fall 2011, Lec 14 DFS.
    https://www.youtube.com/watch?v=AfSk24UTFS8  3:50
    Time: \theta(V+E)
    """
    def DFS_visit(adj, s):
        for v in adj[s]:
            if v not in parent:  # not visited before
                parent[v] = s
                DFS_visit(adj, v)

    parent = {}
    for s in V:
        if s not in parent:
            parent[s] = None
            DFS_visit(adj, s)
