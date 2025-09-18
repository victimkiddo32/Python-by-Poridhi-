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
        wordset=set(wordDict)
        n=len(s)-1
        #memoization
        memo={}
        def f(start,end):
            if (start,end) in memo:
                return memo[(start,end)]
            # base case: entire string segmented
            if start > n:
               return True
    
            # base case: end reached end of string
            if end > n:
               return False

            not_match=f(start,end+1)
            match=False
            if s[start:end+1] in wordset:
                match=f(end+1,end+1)

            memo[(start,end)]=match or not_match
            return memo[(start,end)]
            
        return f(0,0)

if __name__ == "__main__":
    s = "aaaaaaa"
    wordDict = ["aaa","aaaa"]
    sol=Solution()
    print(sol.wordBreak(s,wordDict))



        
# @lc code=end

