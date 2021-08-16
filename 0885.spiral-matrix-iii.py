#
# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#
# https://leetcode.com/problems/spiral-matrix-iii/description/
#
# algorithms
# Medium (71.32%)
# Likes:    369
# Dislikes: 437
# Total Accepted:    29.1K
# Total Submissions: 40.7K
# Testcase Example:  '1\n4\n0\n0'
#
# You start at the cell (rStart, cStart) of an rows x cols grid facing east.
# The northwest corner is at the first row and column in the grid, and the
# southeast corner is at the last row and column.
#
# You will walk in a clockwise spiral shape to visit every position in this
# grid. Whenever you move outside the grid's boundary, we continue our walk
# outside the grid (but may return to the grid boundary later.). Eventually, we
# reach all rows * cols spaces of the grid.
#
# Return an array of coordinates representing the positions of the grid in the
# order you visited them.
#
#
# Example 1:
#
#
# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
#
#
# Example 2:
#
#
# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output:
# [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
#
#
#
# Constraints:
#
#
# 1 <= rows, cols <= 100
# 0 <= rStart < rows
# 0 <= cStart < cols
#
#
#
from typing import List

# @lc code=start
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [None] * (rows * cols)

        EAST, SOUTH, WEST, NORTH = 0, 1, 2, 3
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        bounds = [cStart+1, rStart+1, cStart-1, rStart-1]

        ROW, COL = 0, 1

        dir = EAST

        index = 0
        row, col = rStart, cStart
        while index < rows*cols:
            if 0 <= row < rows and 0 <= col < cols:
                res[index] = [row, col]
                index += 1

            if dir == EAST and col == bounds[EAST]:
                bounds[EAST] = min(cols, bounds[EAST]+1)
                dir = SOUTH
            elif dir == SOUTH and row == bounds[SOUTH]:
                bounds[SOUTH] = min(rows, bounds[SOUTH]+1)
                dir = WEST
            elif dir == WEST and col == bounds[WEST]:
                bounds[WEST] = max(-1, bounds[WEST]-1)
                dir = NORTH
            elif dir == NORTH and row == bounds[NORTH]:
                bounds[NORTH] = max(-1, bounds[NORTH]-1)
                dir = EAST

            row += dirs[dir][ROW]
            col += dirs[dir][COL]

        return res

    def spiralMatrixIII2(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [None] * (rows * cols)

        # EAST, SOUTH, WEST, NORTH = 0, 1, 2, 3
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        bounds = [cStart+1, rStart+1, cStart-1, rStart-1]

        ROW, COL = 0, 1

        dir = 0

        index = 0
        row, col = rStart, cStart
        while index < rows*cols:
            if 0 <= row < rows and 0 <= col < cols:
                res[index] = [row, col]
                index += 1

            if [col, row][dir%2] == bounds[dir]:
                bounds[dir] += dirs[dir][[COL, ROW][dir%2]]
                dir = (dir+1)%len(dirs)

            row += dirs[dir][ROW]
            col += dirs[dir][COL]

        return res

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([1, 1, 0, 0], [[0,0]]),
            ([1, 4, 0, 0], [[0,0],[0,1],[0,2],[0,3]]),
            ([5,6,1,4], [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]])
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
