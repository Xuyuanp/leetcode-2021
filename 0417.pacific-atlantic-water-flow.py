#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (45.10%)
# Likes:    2575
# Dislikes: 633
# Total Accepted:    140.7K
# Total Submissions: 306.5K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# There is an m x n rectangular island that borders both the Pacific Ocean and
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given an m x n
# integer matrix heights where heights[r][c] represents the height above sea
# level of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring
# cells directly north, south, east, and west if the neighboring cell's height
# is less than or equal to the current cell's height. Water can flow from any
# cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and
# Atlantic oceans.
#
#
# Example 1:
#
#
# Input: heights =
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#
#
# Example 2:
#
#
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
#
#
#
# Constraints:
#
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10^5
#
#
#
from typing import List

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        p_visited = [[i == 0 or j == 0 for j in range(n)] for i in range(m)]
        a_visited = [[i == m-1 or j == n-1 for j in range(n)] for i in range(m)]

        def dfs(i: int, j: int, visited: List[List[bool]]):
            visited[i][j] = True
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = i+di, j+dj
                if 0 <= x < m and 0 <= y < n and \
                        heights[x][y] >= heights[i][j] and \
                        not visited[x][y]:
                    dfs(x, y, visited)

        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n-1, a_visited)

        for j in range(n):
            dfs(0, j, p_visited)
            dfs(m-1, j, a_visited)

        res = []

        for row in p_visited:
            print(row)
        print()
        for row in a_visited:
            print(row)

        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i, j])

        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[[2,1], [1,2]]], [[0,0],[0,1],[1,0],[1,1]]),
            ([[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]], [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])
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
