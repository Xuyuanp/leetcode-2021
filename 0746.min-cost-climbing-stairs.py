#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (53.60%)
# Likes:    3799
# Dislikes: 783
# Total Accepted:    278.9K
# Total Submissions: 518.1K
# Testcase Example:  '[10,15,20]'
#
# You are given an integer array cost where cost[i] is the cost of i^th step on
# a staircase. Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
#
# Example 1:
#
#
# Input: cost = [10,15,20]
# Output: 15
# Explanation: Cheapest is: start on cost[1], pay that cost, and go to the
# top.
#
#
# Example 2:
#
#
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping
# cost[3].
#
#
#
# Constraints:
#
#
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(n), O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        x, y = 0, 0
        for a, b in zip(cost, cost[1:]):
            x, y = y, min(x + a, y + b)
        return y

    # O(n), O(n)
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[n]


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([1, 2], 1),
        ([2, 1], 1),
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ]
    for args, want in cases:
        got = sol.minCostClimbingStairs(args)
        if want != got:
            print(f"Failed => args: {args}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
