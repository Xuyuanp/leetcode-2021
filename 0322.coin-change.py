#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (38.25%)
# Likes:    7678
# Dislikes: 209
# Total Accepted:    698.6K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
# Example 1:
#
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Example 3:
#
#
# Input: coins = [1], amount = 0
# Output: 0
#
#
# Example 4:
#
#
# Input: coins = [1], amount = 1
# Output: 1
#
#
# Example 5:
#
#
# Input: coins = [1], amount = 2
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#
from typing import List

# @lc code=start
from functools import lru_cache


class Solution:
    # O(n*k), O(n). n=amount, k=len(coins)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            dp[a] = min(
                dp[a], 1 + min(dp[a - c] if c <= a else float("inf") for c in coins)
            )

        return dp[amount] if dp[amount] != float("inf") else -1

    def coinChange1(self, coins: List[int], amount: int) -> int:
        coins = set(coins)

        @lru_cache(maxsize=None)
        def helper(amount: int):
            if amount == 0:
                return 0
            if amount in coins:
                return 1
            min_cnt = float("inf")
            for c in coins:
                if c > amount:
                    continue
                rest = helper(amount - c)
                if rest < 0:
                    continue
                min_cnt = min(min_cnt, rest)

            return min_cnt + 1 if min_cnt != float("inf") else -1

        return helper(amount)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (([2], 3), -1),
            (([2], 4), 2),
            (([1], 0), 0),
            (([1, 2, 5], 11), 3),
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
