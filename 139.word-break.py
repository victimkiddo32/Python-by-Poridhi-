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
            if start>n:
                return True
            if end>n:
                return False
            
            if (start,end) in memo:
                return memo[(start,end)]
            match = False
            if s[start:end+1] in wordset:
                #check if we can break the rest of the string
                match=f(end+1,end+1)
                #if not, try to extend the end index
                if not match:
                    match=f(start,end+1)
            else:
                match=f(start,end+1)
            memo[(start, end)] = match
            return match
        return f(0,0)

if __name__ == "__main__":
    s = "aaaaaaa"
    wordDict = ["aaaa","aaa"]
    sol=Solution()
    print(sol.wordBreak(s,wordDict))



        
# @lc code=end

