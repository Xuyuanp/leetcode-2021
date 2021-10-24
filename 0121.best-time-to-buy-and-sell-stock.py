#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (52.20%)
# Likes:    9480
# Dislikes: 392
# Total Accepted:    1.4M
# Total Submissions: 2.7M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
#
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
#
#
# Example 1:
#
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.
#
#
# Example 2:
#
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit =
# 0.
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(n), O(1)
    def maxProfit(self, prices: List[int]) -> int:
        start = profit = 0
        for i, p in enumerate(prices[1:]):
            if p < prices[start]:
                start = i+1
            else:
                profit = max(profit, p-prices[start])

        return profit

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[1]], 0),
            ([[1,2]], 1),
            ([[2,1]], 0),
            ([[7,1,5,3,6,4]], 5),
            ([[7,6,4,3,1]], 0),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
