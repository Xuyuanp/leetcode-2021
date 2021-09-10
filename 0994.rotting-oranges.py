#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (49.85%)
# Likes:    4284
# Dislikes: 230
# Total Accepted:    250.5K
# Total Submissions: 499K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
#
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
#
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
# Example 2:
#
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
#
#
# Example 3:
#
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(m*n), O(m*n). BFS
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshes = 0
        rottens = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshes += 1
                elif grid[i][j] == 2:
                    grid[i][j] = 0
                    rottens.append((i, j))
        if freshes == 0:
            return 0

        steps = 0
        while rottens:
            steps += 1
            next_rottens = []
            for i, j in rottens:
                for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                    x, y = i+di, j+dj
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 0
                        next_rottens.append((x, y))
                        freshes -= 1
                        if freshes <= 0:
                            return steps
            rottens = next_rottens
        return -1


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[[0,2]]], 0),
            ([[[2,1,1],[0,1,1],[1,0,1]]], -1),
            ([[[2,1,1],[1,1,0],[0,1,1]]], 4),
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
