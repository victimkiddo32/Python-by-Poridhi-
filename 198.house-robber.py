#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        house=len(nums)-1
        memo={}
        def f(house):
            if house in memo:
                return memo[house]
            if house < 0:
                return 0
            if house ==0:
                return nums[0]
            memo[house]=max(f(house-1),f(house-2)+nums[house])
            return memo[house]
        return f(house)
    
if __name__ == "__main__":
    prices = [2,7,9,3,1]
    sol = Solution()
    print(sol.rob(prices))
# @lc code=end

