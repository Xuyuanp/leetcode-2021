#
# @lc app=leetcode id=750 lang=python3
#
# [750] Count of Corner Rectangles
#
# https://leetcode-cn.com/problems/number-of-corner-rectangles/   [locked]
#
# algorithms
# Medium (32.05%)
# Likes:    11500
# Dislikes: 1618
# Total Accepted:    1M
# Total Submissions: 3.2M
#
# Given an m x n integer matrix grid where each entry is only 0 or 1,
# return the number of corner rectangles.
#
# A corner rectangle is four distinct 1's on the grid that forms an
# axis-aligned rectangle. Note that only the corners need to
# have the value 1. Also, all four 1's used must be distinct.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]
# Output: 1
# Explanation: There is only one corner rectangle,
#  with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
# Example 2:
#
#
# Input: grid = [[1,1,1],[1,1,1],[1,1,1]]
# Output: 9
# Explanation: There are four 2x2 rectangles,
#  four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
# Example 3:
#
#
# Input: grid = [[1,1,1,1]]
# Output: 0
# Explanation: Rectangles must have four distinct corners.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j] is either 0 or 1.
# The number of 1's in the grid is in the range [1, 6000].
#

from collections import Counter
from typing import List

# @lc code=start


class Solution:
    # O(m*n*n), O(n*n)
    def countOfCornerRectanges(self, grid: List[List[int]]) -> int:
        counter = Counter()
        n = len(grid[0])
        for row in grid:
            for i in range(n - 1):
                if row[i] == 0:
                    continue
                for j in range(i + 1, n):
                    if row[j] == 1:
                        counter[i, j] += 1
        return sum(c * (c - 1) // 2 for c in counter.values())


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[[1, 1, 1, 1]]], 0),
            ([[[1, 1, 1], [1, 1, 1], [1, 1, 1]]], 9),
            ([[[1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 0, 1]]], 1),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
