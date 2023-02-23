#
# @lc app=leetcode id=741 lang=python3
#
# [741] Cherry Pickup
#
# https://leetcode.com/problems/cherry-pickup/description/
#
# algorithms
# Hard (35.54%)
# Likes:    1918
# Dislikes: 103
# Total Accepted:    42.6K
# Total Submissions: 119.3K
# Testcase Example:  '[[0,1,-1],[1,0,-1],[1,1,1]]'
#
# You are given an n x n grid representing a field of cherries, each cell is
# one of three possible integers.
#
#
# 0 means the cell is empty, so you can pass through,
# 1 means the cell contains a cherry that you can pick up and pass through,
# or
# -1 means the cell contains a thorn that blocks your way.
#
#
# Return the maximum number of cherries you can collect by following the rules
# below:
#
#
# Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right
# or down through valid path cells (cells with value 0 or 1).
# After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up
# through valid path cells.
# When passing through a path cell containing a cherry, you pick it up, and the
# cell becomes an empty cell 0.
# If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries
# can be collected.
#
#
#
# Example 1:
#
#
# Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
# Output: 5
# Explanation: The player started at (0, 0) and went down, down, right right to
# reach (2, 2).
# 4 cherries were picked up during this single trip, and the matrix becomes
# [[0,1,-1],[0,0,-1],[0,0,0]].
# Then, the player went left, up, up, left to return home, picking up one more
# cherry.
# The total number of cherries picked up is 5, and this is the maximum
# possible.
#
#
# Example 2:
#
#
# Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
# Output: 0
#
#
#
# Constraints:
#
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# grid[i][j] is -1, 0, or 1.
# grid[0][0] != -1
# grid[n - 1][n - 1] != -1
#
#
#
from functools import cache
from typing import List


# @lc code=start
class Solution:
    # O(n^3), O(n^3)
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 2 players start at (0, 0) and move at the same time.
        # Both of them try to pick as manay cherries as possible.
        @cache
        def helper(row1: int, col1: int, row2: int) -> int:
            # they move the same steps => row1 + col1 == row2 + col2
            col2 = row1 + col1 - row2

            # ignore cells out of bound
            if n in (row1, col1, row2, col2):
                return -float("inf")
            # ignore thorns
            if grid[row1][col1] == -1 or grid[row2][col2] == -1:
                return -float("inf")

            # players can only go down or right,
            # they will reach the end at the same time.
            if row1 == col1 == n - 1:
                return grid[row1][col1]

            # player1 picks the cherry
            res = grid[row1][col1]
            # cherry can be picked by only 1 player
            if (row1, col1) != (row2, col2):
                res += grid[row2][col2]

            # move forward
            res += max(
                helper(row1 + 1, col1, row2),
                helper(row1 + 1, col1, row2 + 1),
                helper(row1, col1 + 1, row2),
                helper(row1, col1 + 1, row2 + 1),
            )

            return res

        return max(0, helper(0, 0, 0))


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[[1, 1, -1], [1, -1, 1], [-1, 1, 1]]], 0),
            ([[[0, 1, -1], [1, 0, -1], [1, 1, 1]]], 5),
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
