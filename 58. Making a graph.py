class graph:
    def __init__(self):
        self.graph={}

    def addedge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self,start,visited=None):
        if visited is None:
            visited=set()
        if start not in visited:
            print(start,end=" ")
            visited.add(start)


        for neighbour in self.graph[start]:
            if neighbour not in visited:
                self.dfs(neighbour,visited)

    def bfs(self, start):
        visited = set()
        queue = []
        queue.append(start)
        visited.add(start)

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

        

    def printgraph(self):
        for node in self.graph:
            print(f"{node}->{self.graph[node]}")

g=graph()
g.addedge(12,5)
g.addedge(12,23)
g.addedge(12,3)
g.addedge(25,5)
g.addedge(25,23)
g.addedge(25,3)


g.printgraph()

g.dfs(12)
print()
g.bfs(12)
