from collections import deque

class graph:
    def __init__(self,directed):
        self.directed=directed
        self.adjlist={}

    def addedge(self,u,v):
        # u->v (directed)
        # v->u (undirected)
        self.adjlist[u].append(v)
        if not self.directed:
            self.adjlist[v].append(u)

    def dfs(self,start):
        visited=set()
        order=[]
        def rec(u):
            visited.add(u)
            order.append(u)
            for neighbour in self.adjlist[u]:
                if neighbour not in visited:
                    rec(neighbour)
        rec(start)
        return order
    
    def dfs_iter(self,start):
        visited=set()
        order=[]
        stack=[start]
        while stack:
            u=stack.pop()
            visited.add(u)
            order.append(u)
            for neighbour in self.adjlist[u]:
                if neighbour not in visited:
                    stack.append(neighbour)
        
        return order
    




