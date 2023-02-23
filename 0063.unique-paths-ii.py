#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (36.09%)
# Likes:    3254
# Dislikes: 307
# Total Accepted:    406.1K
# Total Submissions: 1.1M
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
#
# An obstacle and space is marked as 1 and 0 respectively in the grid.
#
#
# Example 1:
#
#
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#
# Example 2:
#
#
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#
#
#
# Constraints:
#
#
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.
#
#
#
import itertools
from typing import List


# @lc code=start
class Solution:
    # O(m*n), O(1)
    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1
        for i, j in itertools.product(range(m), range(n)):
            if i == j == 0:
                continue
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
                continue
            if i > 0:
                obstacleGrid[i][j] += obstacleGrid[i - 1][j]
            if j > 0:
                obstacleGrid[i][j] += obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]

    # O(m*n), O(m*n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1
        for i, j in itertools.product(range(1, m + 1), range(1, n + 1)):
            if i == j == 1 or obstacleGrid[i - 1][j - 1] == 1:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[[0, 1]]], 0),
            ([[[1, 0]]], 0),
            ([[[0, 0, 0], [0, 1, 0], [0, 0, 0]]], 2),
            ([[[0, 1], [0, 0]]], 1),
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
