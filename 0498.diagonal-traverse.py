#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (51.53%)
# Likes:    1543
# Dislikes: 442
# Total Accepted:    144.5K
# Total Submissions: 275.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix mat, return an array of all the elements of the array
# in a diagonal order.
#
#
# Example 1:
#
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
#
#
# Example 2:
#
#
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
#
#
#
# Constraints:
#
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# -10^5 <= mat[i][j] <= 10^5
#
#
#
from typing import List


# @lc code=start
class Solution:

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        m, n = len(mat), len(mat[0])
        directions = [
            ((-1, 1), (0, n - 1), (1, 0)),  # bottom-left -> top-right
            ((1, -1), (m - 1, 0), (0, 1)),  # top-right -> bottom-left
        ]
        curr = 0
        row = col = 0

        ROW, COL = 0, 1
        STEP, BOUND, CORNER_STEP = 0, 1, 2

        for _ in range(m * n):
            res.append(mat[row][col])

            row_end = row == directions[curr][BOUND][ROW]
            col_end = col == directions[curr][BOUND][COL]
            if row_end and col_end:
                row += directions[curr][CORNER_STEP][ROW]
                col += directions[curr][CORNER_STEP][COL]
                curr = (curr + 1) % 2
            elif row_end:
                col += 1
                curr = (curr + 1) % 2
            elif col_end:
                row += 1
                curr = (curr + 1) % 2
            else:
                row += directions[curr][STEP][ROW]
                col += directions[curr][STEP][COL]

        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[[1]]], [1]),
            ([[[1, 2, 3]]], [1, 2, 3]),
            ([[[1], [2], [3]]], [1, 2, 3]),
            ([[[1, 2], [3, 4]]], [1, 2, 3, 4]),
            ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
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
