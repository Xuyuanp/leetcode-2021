#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#
# https://leetcode.com/problems/stone-game/description/
#
# algorithms
# Medium (67.71%)
# Likes:    1283
# Dislikes: 1481
# Total Accepted:    98.2K
# Total Submissions: 144.8K
# Testcase Example:  '[5,3,4,5]'
#
# Alex and Lee play a game with piles of stones.  There are an even number of
# piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].
#
# The objective of the game is to end with the most stones.  The total number
# of stones is odd, so there are no ties.
#
# Alex and Lee take turns, with Alex starting first.  Each turn, a player takes
# the entire pile of stones from either the beginning or the end of the row.
# This continues until there are no more piles left, at which point the person
# with the most stones wins.
#
# Assuming Alex and Lee play optimally, return True if and only if Alex wins
# the game.
#
#
# Example 1:
#
#
# Input: piles = [5,3,4,5]
# Output: true
# Explanation:
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10
# points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win
# with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we
# return true.
#
#
#
# Constraints:
#
#
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles) is odd.
#
#
#
from functools import cache
from typing import List, Tuple

# @lc code=start
class Solution:
    # Alex can always win
    def stoneGame(self, piles: List[int]) -> bool:
        FIRST, SECOND = 0, 1

        n = len(piles)
        # dp[i][j] is the (max value of the first pick, max value of the second pick) in the range piles[i:j+1]
        # when i == j, the first pick always get the only pile.
        dp = [[(piles[i] if i == j else 0, 0) for j in range(n)] for i in range(n)]

        # (0,   1), (1,   2) .. (n-3, n-2), (n-2, n-1)
        # (0,   2), (1,   3) .. (n-4, n-2)
        # ...
        # (0, n-2), (1, n-1)
        # (0, n-1)
        for shift in range(1, n):
            for i in range(0, n - shift):
                j = shift + i

                left = piles[i] + dp[i + 1][j][SECOND]
                right = piles[j] + dp[i][j - 1][SECOND]

                if left > right:
                    dp[i][j] = (left, dp[i + 1][j][FIRST])
                else:
                    dp[i][j] = (right, dp[i][j - 1][FIRST])

        return dp[0][n - 1][0] > dp[0][n - 1][1]

    # O(n^2), O(n^2)
    def stoneGame1(self, piles: List[int]) -> bool:
        n = len(piles)

        @cache
        def helper(i: int, j: int) -> Tuple[int, int]:
            if i == j:
                return piles[i], 0

            la, lb = helper(i + 1, j)  # take left
            ra, rb = helper(i, j - 1)  # take right
            return max(
                (piles[i] + lb, la),
                (piles[j] + rb, ra),
            )

        a, b = helper(0, n - 1)
        return a > b

    # O(n^2), O(n^2)
    def stoneGame2(self, piles: List[int]) -> bool:
        n = len(piles)

        @cache
        def helper(i: int, j: int) -> int:
            if i == j:
                return piles[i]
            return max(piles[i] - helper(i + 1, j), piles[j] - helper(i, j - 1))

        return helper(0, n - 1) > 0


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[5, 3, 4, 5]], True),
            ([[1, 2]], True),
            ([[1, 100, 3, 3]], True),
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
