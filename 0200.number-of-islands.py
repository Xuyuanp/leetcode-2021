#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (50.51%)
# Likes:    9143
# Dislikes: 253
# Total Accepted:    1.1M
# Total Submissions: 2.2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
#
# Example 1:
#
#
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
#
#
from typing import List


# @lc code=start
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])

        def bfs(row: int, col: int):
            if 0 <= row < m and 0 <= col < n and grid[row][col] == "1":
                grid[row][col] = "0"
                bfs(row - 1, col)
                bfs(row + 1, col)
                bfs(row, col - 1)
                bfs(row, col + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    bfs(i, j)

        return res

    def numIslands1(self, grid: List[List[str]]) -> int:
        res = [0]

        ufs = {}

        def find(point):
            if point not in ufs:
                ufs[point] = point
                res[0] += 1
            elif ufs[point] != point:
                ufs[point] = find(ufs[point])
            return ufs[point]

        def union(p1, p2):
            r1, r2 = find(p1), find(p2)
            if r1 == r2:
                return
            res[0] -= 1
            ufs[r1] = r2

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                index = i * n + j
                find(index)
                if i > 0 and grid[i - 1][j] == "1" and index - n in ufs:
                    union(index - n, index)
                if j > 0 and grid[i][j - 1] == "1" and index - 1 in ufs:
                    union(index - 1, index)

        return res[0]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (
                [[
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ]],
                3,
            ),
            (
                [[
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ]],
                1,
            ),
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
