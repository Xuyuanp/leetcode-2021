#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#
# https://leetcode.com/problems/coin-change-2/description/
#
# algorithms
# Medium (53.20%)
# Likes:    3727
# Dislikes: 82
# Total Accepted:    220.6K
# Total Submissions: 406.7K
# Testcase Example:  '5\n[1,2,5]'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
#
# Return the number of combinations that make up that amount. If that amount of
# money cannot be made up by any combination of the coins, return 0.
#
# You may assume that you have an infinite number of each kind of coin.
#
# The answer is guaranteed to fit into a signed 32-bit integer.
#
#
# Example 1:
#
#
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
#
# Example 2:
#
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
#
# Example 3:
#
#
# Input: amount = 10, coins = [10]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000
#
#
#
from typing import Counter, List


# @lc code=start
class Solution:
    # O(n*amount), O(amount)
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for j in range(len(coins)):
            for i in range(1, amount + 1):
                if i >= coins[j]:
                    dp[i] += dp[i - coins[j]]
        return dp[amount]

    # O(n*amount), O(amount)
    def change1(self, amount: int, coins: List[int]) -> int:
        dp = Counter()
        dp[0] = 1

        for c in coins:
            for i in range(1, amount + 1):
                if i >= c:
                    dp[i] += dp[i - c]
        return dp[amount]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([10, [10]], 1),
            ([3, [2]], 0),
            ([5, [1, 2, 5]], 4),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
