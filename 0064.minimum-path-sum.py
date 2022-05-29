#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (57.10%)
# Likes:    5242
# Dislikes: 87
# Total Accepted:    569.6K
# Total Submissions: 994.2K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
#
# Example 1:
#
#
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
#
#
# Example 2:
#
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(m*n), O(1)
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                elif i > 0:
                    grid[i][j] += grid[i - 1][j]
                elif j > 0:
                    grid[i][j] += grid[i][j - 1]

        return grid[-1][-1]


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([[1]], 1),
        ([[1, 2]], 3),
        ([[1, 2], [1, 1]], 3),
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 2, 3], [4, 5, 6]], 12),
    ]
    for grid, want in cases:
        got = sol.minPathSum(grid)
        if want != got:
            print(f"Failed => args: {grid}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
