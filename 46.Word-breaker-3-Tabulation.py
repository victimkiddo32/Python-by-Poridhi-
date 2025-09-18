#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        """ 
        Outer loop = “where can I start a word?”
        Inner loop = “how far can this word go?”
        Condition = “is this a valid word, and is the rest segmentable?
        ”"""
        wordset=set(wordDict)
        n=len(s)
        #tabulation
        dp=[False]*(n+1)
        dp[n]=True #base case: it means we have segmented the entire string

        for start in range(n,-1,-1):
            for end in range(start,n+1):
                if s[start:end+1] in wordset and dp[end+1]:
                    dp[start]=True
                    break
        return dp[0]
    


if __name__ == "__main__":
    s = "aaaaaaa"
    wordDict = ["aaa","aaaa"]
    sol=Solution()
    print(sol.wordBreak(s,wordDict))



        
# @lc code=end

