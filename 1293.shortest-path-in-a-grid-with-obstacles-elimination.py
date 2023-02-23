#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
#
# algorithms
# Hard (43.29%)
# Likes:    1072
# Dislikes: 19
# Total Accepted:    38.6K
# Total Submissions: 89.2K
# Testcase Example:  '[[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]\n1'
#
# You are given an m x n integer matrix grid where each cell is either 0
# (empty) or 1 (obstacle). You can move up, down, left, or right from and to an
# empty cell in one step.
#
# Return the minimum number of steps to walk from the upper left corner (0, 0)
# to the lower right corner (m - 1, n - 1) given that you can eliminate at most
# k obstacles. If it is not possible to find such walk return -1.
#
#
# Example 1:
#
#
# Input:
# grid =
# [[0,0,0],
# [1,1,0],
# ⁠[0,0,0],
# [0,1,1],
# ⁠[0,0,0]],
# k = 1
# Output: 6
# Explanation:
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such
# path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
#
#
# Example 2:
#
#
# Input:
# grid =
# [[0,1,1],
# [1,1,1],
# [1,0,0]],
# k = 1
# Output: -1
# Explanation:
# We need to eliminate at least two obstacles to find such a walk.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 40
# 1 <= k <= m * n
# grid[i][j] == 0 or 1
# grid[0][0] == grid[m - 1][n - 1] == 0
#
#
#
import heapq
from collections import deque
from typing import List


# @lc code=start
class Solution:
    # O(m*n*k), O(m*n*k). TLE, Why?????
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        VISITED = "*"

        def dfs(i: int, j: int, k: int) -> int:
            if i == m - 1 and j == n - 1:
                return 0

            cell = grid[i][j]
            grid[i][j] = VISITED

            res = float("inf")
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] != VISITED:
                    if grid[x][y] == 0:
                        steps = dfs(x, y, k)
                        if steps >= 0:
                            res = min(res, steps + 1)
                    elif k > 0:
                        steps = dfs(x, y, k - 1)
                        if steps >= 0:
                            res = min(res, steps + 1)

            grid[i][j] = cell

            return -1 if res == float("inf") else res

        return dfs(0, 0, k)

    # O(m*n*k), O(m*n*k). AC
    def shortestPath1(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        if k >= (m - 1) + (n - 1) - 1:
            return m + n - 2

        queue = deque()
        queue.append((0, (0, 0, k)))
        visited = {(0, 0, k)}
        while queue:
            steps, (i, j, k) = queue.popleft()
            if i == m - 1 and j == n - 1:
                return steps
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    next_k = k - grid[x][y]
                    if next_k >= 0 and (x, y, next_k) not in visited:
                        visited.add((x, y, next_k))
                        queue.append((steps + 1, (x, y, next_k)))

        return -1

    # O(m*n*log(m*n*k))), O(m*n*k). A-star
    def shortestPath2(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        if k >= (m - 1) + (n - 1) - 1:
            return m + n - 2

        def manhatton_distance(i: int, j: int) -> int:
            return m - 1 - i + n - 1 - j

        visited = set()
        queue = [(manhatton_distance(0, 0), 0, (0, 0, k))]
        visited.add((0, 0, k))

        while queue:
            dist, steps, (i, j, k) = heapq.heappop(queue)
            if dist - steps <= k:
                return dist

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    next_k = k - grid[x][y]
                    next_state = (x, y, next_k)
                    if next_k >= 0 and next_state not in visited:
                        visited.add(next_state)
                        next_dist = manhatton_distance(x, y) + steps + 1
                        heapq.heappush(queue,
                                       (next_dist, steps + 1, next_state))

        return -1


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1], -1),
            ([[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1], 6),
            (
                [
                    [
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    ],
                    1,
                ],
                20,
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
