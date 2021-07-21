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
from typing import List

# @lc code=start
class Solution:
    # Alex can always win
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # dp[i][j] is value of the game piles[i:j+1]
        dp = [[(piles[i] if i == j else 0, 0) for j in range(n)] for i in range(n)]

        # (0,   1), (1,   2) .. (n-3, n-2), (n-2, n-1)
        # (0,   2), (1,   3) .. (n-4, n-2)
        # ...
        # (0, n-2), (1, n-1)
        # (0, n-1)
        for shift in range(1, n):
            for i in range(0, n-shift):
                j = shift + i

                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]

                if left > right:
                    dp[i][j] = (left, dp[i+1][j][0])
                else:
                    dp[i][j] = (right, dp[i][j-1][0])

        return dp[0][n-1][0] > dp[0][n-1][1]

# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([5, 3, 4, 5], True),
        ([1, 2], True),
        ([1, 100, 3, 3], True),
    ]
    for piles, want in cases:
        got = sol.stoneGame(piles)
        if got != want:
            print(f"Failed => args: {piles}; want: {want}, but got: {got}")
            break
    else:
        print('All Passed')
