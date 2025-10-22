#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
class Solution:
    def validPath (self,n,edges,source,destination):
        graph={}
        for u,v in edges:
            if u not in graph:
                graph[u]=[]
            if v not in graph:
                graph[v]=[]
            graph[u].append(v)
            graph[v].append(u)

        visited=set()
        def dfs(node):
            if node==destination:
                return True
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour):     
                        return True
            return False   
        
        return dfs(source)
        
        
# @lc code=end

if __name__ =="__main__":
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    sol=Solution()
    print(sol.validPath(n,edges,source,destination))



