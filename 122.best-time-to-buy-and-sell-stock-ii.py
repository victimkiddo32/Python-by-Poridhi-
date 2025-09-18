#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        memo = {}
        def f(day, stock):
            if (day, stock) in memo:
                return memo[(day, stock)]
            if day == len(prices):
                return 0
            if stock == 1:
                # We have a stock, so we can sell or skip
                sell = f(day + 1, 0) + prices[day]
                skip = f(day + 1, 1)
                memo[(day, stock)] = max(sell, skip)
            else:
                # We don't have a stock, so we can buy or skip
                buy = f(day + 1, 1) - prices[day]
                skip = f(day + 1, 0)
                memo[(day, stock)] = max(buy, skip)
            return memo[(day, stock)]
        return f(0, 0)

prices = list(map(int, input().split()))
sol = Solution()
result = sol.maxProfit(prices)
print(result)

# ...existing code...

# @lc code=end
