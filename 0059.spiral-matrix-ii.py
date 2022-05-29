#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (59.03%)
# Likes:    1903
# Dislikes: 139
# Total Accepted:    265.6K
# Total Submissions: 446.8K
# Testcase Example:  '3'
#
# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n^2 in spiral order.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
#
#
#
from typing import List
from dataclasses import dataclass

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        loops = n // 2
        first = 1
        for i in range(loops):
            step = n - 1 - i * 2
            for j in range(i, n - i - 1):
                matrix[i][j] = first + step * 0
                matrix[j][n - i - 1] = first + step * 1
                matrix[n - i - 1][n - j - 1] = first + step * 2
                matrix[n - j - 1][i] = first + step * 3
                first += 1

            first += 3 * step

        if n % 2 == 1:
            matrix[loops][loops] = first
        return matrix

    def generateMatrix1(self, n: int) -> List[List[int]]:
        def generateMatrixMN(rows: int, cols: int) -> List[List[int]]:
            matrix = [[0] * cols for _ in range(rows)]

            STEP_ROW, STEP_COL, BOUND = 0, 1, 2
            directions = [
                [0, 1, cols - 1],  # left -> right
                [1, 0, rows - 1],  # top -> bottom
                [0, -1, 0],  # right -> left
                [-1, 0, 0],  # bottom -> top
            ]
            curr_dir = 0
            row = col = 0
            for val in range(rows * cols):
                matrix[row][col] = val + 1

                if [col, row][curr_dir % 2] == directions[curr_dir][BOUND]:
                    # when we reach the bound of the current direction,
                    # shrink the bound of the previous direction,
                    # and then turn to the next direction
                    pre_dir = (curr_dir - 1) % 4
                    directions[pre_dir][BOUND] -= directions[pre_dir][
                        [STEP_COL, STEP_ROW][pre_dir % 2]
                    ]
                    curr_dir = (curr_dir + 1) % 4

                row += directions[curr_dir][STEP_ROW]
                col += directions[curr_dir][STEP_COL]

            return matrix

        return generateMatrixMN(n, n)

    def generateMatrix2(self, n: int) -> List[List[int]]:
        def generateMatrixMN(rows: int, cols: int) -> List[List[int]]:
            matrix = [[0] * cols for _ in range(rows)]

            row = [0]
            col = [0]
            AXIS_REF, STEP, BOUND = 0, 1, 2
            DEREF = 0
            directions = [
                [col, 1, cols - 1],  # left -> right
                [row, 1, rows - 1],  # top -> bottom
                [col, -1, 0],  # right -> left
                [row, -1, 0],  # bottom -> top
            ]
            curr_dir = 0
            for val in range(rows * cols):
                matrix[row[DEREF]][col[DEREF]] = val + 1

                if directions[curr_dir][AXIS_REF][DEREF] == directions[curr_dir][BOUND]:
                    # when we reach the bound of the current direction,
                    # shrink the bound of the previous direction,
                    # and then turn to the next direction
                    pre_dir = (curr_dir - 1) % 4
                    directions[pre_dir][BOUND] -= directions[pre_dir][STEP]
                    curr_dir = (curr_dir + 1) % 4

                directions[curr_dir][AXIS_REF][DEREF] += directions[curr_dir][STEP]

            return matrix

        return generateMatrixMN(n, n)

    def generateMatrix3(self, n: int) -> List[List[int]]:
        def generateMatrixMN(rows: int, cols: int) -> List[List[int]]:
            DEREF = 0

            @dataclass
            class Direction:
                axis_ref: List[int]
                step: int
                bound: int

                def move(self):
                    self.axis_ref[DEREF] += self.step

                def shrink(self):
                    self.bound -= self.step

                def is_end(self):
                    return self.axis_ref[DEREF] == self.bound

            matrix = [[0] * cols for _ in range(rows)]

            row = [0]
            col = [0]

            directions = [
                Direction(col, 1, cols - 1),  # left -> right
                Direction(row, 1, rows - 1),  # top -> bottom
                Direction(col, -1, 0),  # right -> left
                Direction(row, -1, 0),  # bottom -> top
            ]
            curr_dir = 0
            for val in range(rows * cols):
                matrix[row[DEREF]][col[DEREF]] = val + 1

                if directions[curr_dir].is_end():
                    # when we reach the bound of the current direction,
                    # shrink the bound of the previous direction,
                    # and then turn to the next direction
                    pre_dir = (curr_dir + 3) % 4
                    directions[pre_dir].shrink()
                    curr_dir = (curr_dir + 1) % 4

                directions[curr_dir].move()

            return matrix

        return generateMatrixMN(n, n)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([1], [[1]]),
            ([2], [[1, 2], [4, 3]]),
            ([3], [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
            (
                [4],
                [
                    [1, 2, 3, 4],
                    [12, 13, 14, 5],
                    [11, 16, 15, 6],
                    [10, 9, 8, 7],
                ],
            ),
            (
                [5],
                [
                    [1, 2, 3, 4, 5],
                    [16, 17, 18, 19, 6],
                    [15, 24, 25, 20, 7],
                    [14, 23, 22, 21, 8],
                    [13, 12, 11, 10, 9],
                ],
            ),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
