#
# @lc app=leetcode id=714 lang=python
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        memo = {}
        def f(day, stock):
            if (day, stock) in memo:
                return memo[(day, stock)]
            if day == len(prices):
                return 0
            if stock == 1:
                # We have a stock, so we can sell or skip
                sell = f(day + 1, 0) + prices[day] -fee
                skip = f(day + 1, 1)
                memo[(day, stock)] = max(sell, skip)
            else:
                # We don't have a stock, so we can buy or skip
                buy = f(day + 1, 1) - prices[day]
                skip = f(day + 1, 0)
                memo[(day, stock)] = max(buy, skip)
            return memo[(day, stock)]
        return f(0, 0)

if __name__ == "__main__":
    prices = [1,3,7,5,10,3] 
    sol = Solution()
    print(sol.maxProfit(prices,3))
# @lc code=end

