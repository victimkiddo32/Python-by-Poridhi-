#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self,n,trust):
        trusts_others=[0]*(n+1)
        trusted_by_others=[0]*(n+1)
        
        for u,v in trust:
            trusts_others[u]+=1
            trusted_by_others[v]+=1

        for person in range(1,n+1):
            if trusts_others[person]==0 and trusted_by_others[person]==n-1:
                return person
        return -1

# @lc code=end

if __name__ =="__main__":
    n=3
    trust = [[1,3],[2,3]]
    sol=Solution()
    print(sol.findJudge(n,trust))
    

