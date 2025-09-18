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

        wordset = set(wordDict)
        n = len(s)

        # next_row[i] corresponds to dp[start+1][i]
        next_row = [False] * (n + 1)
        next_row[n] = True  # base case: empty string

        # iterate start index from n-1 down to 0
        for start in range(n - 1, -1, -1):
            curr_row = [False] * (n + 1)
            curr_row[n] = True  # empty substring at the end

            for end in range(n - 1, start - 1, -1):
                not_match = curr_row[end + 1]  # extend current substring
                match = False
                if s[start:end + 1] in wordset:
                    match = next_row[end + 1]  # cut and restart from next_row
                curr_row[end] = not_match or match

            next_row = curr_row  # roll the row for next iteration

        return curr_row[0]







if __name__ == "__main__":
    s = "aaaaaaa"
    wordDict = ["aaa","aaaa"]
    sol=Solution()
    print(sol.wordBreak(s,wordDict))



        
# @lc code=end

