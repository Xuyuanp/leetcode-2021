#
# @lc app=leetcode id=1463 lang=python3
#
# [1463] Cherry Pickup II
#
# https://leetcode.com/problems/cherry-pickup-ii/description/
#
# algorithms
# Hard (68.60%)
# Likes:    925
# Dislikes: 12
# Total Accepted:    30.4K
# Total Submissions: 44.4K
# Testcase Example:  '[[3,1,1],[2,5,1],[1,5,5],[2,1,1]]'
#
# Given a rows x cols matrix grid representing a field of cherries. Each cell
# in grid represents the number of cherries that you can collect.
#
# You have two robots that can collect cherries for you, Robot #1 is located at
# the top-left corner (0,0) , and Robot #2 is located at the top-right corner
# (0, cols-1) of the grid.
#
# Return the maximum number of cherries collection using both robots  by
# following the rules below:
#
#
# From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1,
# j+1).
# When any robot is passing through a cell, It picks it up all cherries, and
# the cell becomes an empty cell (0).
# When both robots stay on the same cell, only one of them takes the
# cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in the grid.
#
#
#
# Example 1:
#
#
#
#
# Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24
# Explanation: Path of robot #1 and #2 are described in color green and blue
# respectively.
# Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
# Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
# Total of cherries: 12 + 12 = 24.
#
#
# Example 2:
#
#
#
#
# Input: grid =
# [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
# Output: 28
# Explanation: Path of robot #1 and #2 are described in color green and blue
# respectively.
# Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
# Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
# Total of cherries: 17 + 11 = 28.
#
#
# Example 3:
#
#
# Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
# Output: 22
#
#
# Example 4:
#
#
# Input: grid = [[1,1],[1,1]]
# Output: 4
#
#
#
# Constraints:
#
#
# rows == grid.length
# cols == grid[i].length
# 2 <= rows, cols <= 70
# 0 <= grid[i][j] <= 100 
#
#
#
from functools import cache
from typing import List

# @lc code=start
class Solution:
    # O(m*n*n), O(m*n*n). m, n = rows, cols
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        @cache
        def helper(row: int, col1: int, col2: int) -> int:
            if not (0 <= col1 < cols and 0 <= col2 < cols):
                return -float('inf')

            res = grid[row][col1]
            if col1 != col2:
                res += grid[row][col2]

            if row+1 < rows:
                res += max(helper(row+1, col1+i, col2+j)
                           for i in range(-1, 2)
                           for j in range(-1, 2))

            return res

        return helper(0, 0, cols-1)

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[[1,1],[1,1]]], 4),
            ([[[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]], 28),
            ([[[3,1,1],[2,5,1],[1,5,5],[2,1,1]]], 24),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
