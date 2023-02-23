#
# @lc app=leetcode id=1872 lang=python3
#
# [1872] Stone Game VIII
#
# https://leetcode.com/problems/stone-game-viii/description/
#
# algorithms
# Hard (51.03%)
# Likes:    193
# Dislikes: 8
# Total Accepted:    4K
# Total Submissions: 7.7K
# Testcase Example:  '[-1,2,-3,4,-5]'
#
# Alice and Bob take turns playing a game, with Alice starting first.
#
# There are n stones arranged in a row. On each player's turn, while the number
# of stones is more than one, they will do the following:
#
#
# Choose an integer x > 1, and remove the leftmost x stones from the row.
# Add the sum of the removed stones' values to the player's score.
# Place a new stone, whose value is equal to that sum, on the left side of the
# row.
#
#
# The game stops when only one stone is left in the row.
#
# The score difference between Alice and Bob is (Alice's score - Bob's score).
# Alice's goal is to maximize the score difference, and Bob's goal is the
# minimize the score difference.
#
# Given an integer array stones of length n where stones[i] represents the
# value of the i^th stone from the left, return the score difference between
# Alice and Bob if they both play optimally.
#
#
# Example 1:
#
#
# Input: stones = [-1,2,-3,4,-5]
# Output: 5
# Explanation:
# - Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her
# score, and places a stone of
# ⁠ value 2 on the left. stones = [2,-5].
# - Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places
# a stone of value -3 on
# ⁠ the left. stones = [-3].
# The difference between their scores is 2 - (-3) = 5.
#
#
# Example 2:
#
#
# Input: stones = [7,-6,5,10,5,-2,-6]
# Output: 13
# Explanation:
# - Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to
# her score, and places a
# ⁠ stone of value 13 on the left. stones = [13].
# The difference between their scores is 13 - 0 = 13.
#
#
# Example 3:
#
#
# Input: stones = [-10,-12]
# Output: -22
# Explanation:
# - Alice can only make one move, which is to remove both stones. She adds
# (-10) + (-12) = -22 to her
# ⁠ score and places a stone of value -22 on the left. stones = [-22].
# The difference between their scores is (-22) - 0 = -22.
#
#
#
# Constraints:
#
#
# n == stones.length
# 2 <= n <= 10^5
# -10^4 <= stones[i] <= 10^4
#
#
from functools import cache
from typing import List


# @lc code=start
class Solution:
    # O(n^2), O(n). TLE
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + stones[i - 1]

        @cache
        def helper(i: int) -> int:
            if n - i == 1:
                return 0

            res = -float("inf")
            for x in range(2, n - i + 1):
                res = max(res, presum[i + x] - helper(i + x - 1))
            return res

        return helper(0)

    # O(n^2), O(n). TLE
    def stoneGameVIII1(self, stones: List[int]) -> int:
        n = len(stones)
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + stones[i - 1]

        dp = [-float("inf")] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            for x in range(2, n - i + 1):
                dp[i] = max(dp[i], presum[i + x] - dp[i + x - 1])

        return dp[0]

    # Alice's turn to pick in stones[i:n], best solution is f(i).
    # She can choose to pick 2 or more tones.
    # if she picks the first two tones:
    #   presum[i+2] score was gain => f(i) = presum[i+2] - f(i+1)
    # otherwise, f(i, n) => f(i+1)
    # We want get the maximize score. so f(i) = max(presum[i+2] - f(i+1), f(i+1))
    # O(n), O(n).
    def stoneGameVIII2(self, stones: List[int]) -> int:
        n = len(stones)
        presum = [0] * (n + 1)

        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + stones[i - 1]

        dp = [-float("inf")] * n
        dp[-1] = 0
        dp[-2] = presum[-1]

        for i in range(n - 3, -1, -1):
            dp[i] = max(presum[i + 2] - dp[i + 1], dp[i + 1])

        return dp[0]

    # O(n), O(n)
    def stoneGameVIII3(self, stones: List[int]) -> int:
        n = len(stones)
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + stones[i - 1]

        @cache
        def helper(i: int) -> int:
            if n - i == 1:
                return 0
            if n - i == 2:
                return presum[n]

            next_score = helper(i + 1)
            res = max(presum[i + 2] - next_score, next_score)
            return res

        return helper(0)

    # O(n), O(1).
    def stoneGameVIII4(self, stones: List[int]) -> int:
        n = len(stones)

        for i in range(1, n):
            stones[i] += stones[i - 1]

        res = stones[-1]
        for i in range(n - 2, 0, -1):
            res = max(stones[i] - res, res)

        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1, 2]], 3),
            ([[1, 2, 3]], 6),
            ([[-1, -2, -3]], 3),
            ([[-10, -12]], -22),
            ([[7, -6, 5, 10, 5, -2, -6]], 13),
            ([[-1, 2, -3, 4, -5]], 5),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
