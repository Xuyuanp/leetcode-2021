#
# @lc app=leetcode id=1690 lang=python3
#
# [1690] Stone Game VII
#
# https://leetcode.com/problems/stone-game-vii/description/
#
# algorithms
# Medium (58.56%)
# Likes:    536
# Dislikes: 113
# Total Accepted:    23K
# Total Submissions: 39.1K
# Testcase Example:  '[5,3,1,4,2]'
#
# Alice and Bob take turns playing a game, with Alice starting first.
#
# There are n stones arranged in a row. On each player's turn, they can remove
# either the leftmost stone or the rightmost stone from the row and receive
# points equal to the sum of the remaining stones' values in the row. The
# winner is the one with the higher score when there are no stones left to
# remove.
#
# Bob found that he will always lose this game (poor Bob, he always loses), so
# he decided to minimize the score's difference. Alice's goal is to maximize
# the difference in the score.
#
# Given an array of integers stones where stones[i] represents the value of the
# i^th stone from the left, return the difference in Alice and Bob's score if
# they both play optimally.
#
#
# Example 1:
#
#
# Input: stones = [5,3,1,4,2]
# Output: 6
# Explanation:
# - Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0,
# stones = [5,3,1,4].
# - Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones =
# [3,1,4].
# - Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones =
# [1,4].
# - Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
# - Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
# The score difference is 18 - 12 = 6.
#
#
# Example 2:
#
#
# Input: stones = [7,90,5,1,100,10,10,2]
# Output: 122
#
#
# Constraints:
#
#
# n == stones.length
# 2 <= n <= 1000
# 1 <= stones[i] <= 1000
#
#
#
from functools import lru_cache
from typing import List


# @lc code=start
class Solution:
    # O(n^2), O(n^2). TLE or MLE?????
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)

        # sum(stones[i:j]) == presum[j] - presum[i]
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + stones[i - 1]

        @lru_cache(maxsize=2000)  # maxsize is necessary, MLE otherwise
        def helper(i: int, j: int) -> int:
            if i == j:
                return 0

            x1 = helper(i, j - 1)
            x2 = helper(i + 1, j)

            return max(
                (presum[j] - presum[i] - x1),
                (presum[j + 1] - presum[i + 1] - x2),
            )

        return helper(0, n - 1)

    def stoneGameVII1(self, stones: List[int]) -> int:
        n = len(stones)
        # sum(stones[i:j]) == presum[j] - presum[i]
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + stones[i - 1]

        dp = [[0] * n for _ in range(n)]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(
                    presum[j] - presum[i] - dp[i][j - 1],
                    presum[j + 1] - presum[i + 1] - dp[i + 1][j],
                )

        return dp[0][n - 1]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1, 2]], 2),
            ([[1, 2, 3]], 2),
            ([[5, 3, 1, 4]], 7),
            ([[5, 3, 1, 4, 2]], 6),
            ([[7, 90, 5, 1, 100, 10, 10, 2]], 122),
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
