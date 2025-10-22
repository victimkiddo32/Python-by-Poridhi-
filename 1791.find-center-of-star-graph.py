#
# @lc app=leetcode id=1791 lang=python3
#
# [1791] Find Center of Star Graph
#

# @lc code=start
class Solution:
    def findCenter(self, edges):
        connected={}
        for u,v in edges:
            if u not in connected:
                connected[u]=0
            if v not in connected:
                connected[v]=0

            connected[u]+=1
            connected[v]+=1
        
        for node in connected:
            if connected[node]==len(edges):
                return node
        
        return -1
        
# @lc code=end
if __name__ =="__main__":
    n=3
    edges=[[1,2],[2,3],[4,2]]
    sol=Solution()
    print(sol.findCenter(edges))
