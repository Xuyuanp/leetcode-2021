#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (57.02%)
# Likes:    5658
# Dislikes: 250
# Total Accepted:    677.4K
# Total Submissions: 1.2M
# Testcase Example:  '3\n7'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# How many possible unique paths are there?
#
#
# Example 1:
#
#
# Input: m = 3, n = 7
# Output: 28
#
#
# Example 2:
#
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#
#
# Example 3:
#
#
# Input: m = 7, n = 3
# Output: 28
#
#
# Example 4:
#
#
# Input: m = 3, n = 3
# Output: 6
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10^9.
#
#
#

# @lc code=start
import itertools
from functools import cache


class Solution:
    # O(m*n), O(m*n)
    def uniquePaths1(self, m: int, n: int) -> int:
        mem = {}

        def helper(x: int, y: int) -> int:
            if x <= 0 or y <= 0:
                return 0
            if x == 1 or y == 1:
                return 1
            if (x, y) not in mem:
                mem[x, y] = helper(x - 1, y) + helper(x, y - 1)
            return mem[x, y]

        return helper(m, n)

    def uniquePaths2(self, m: int, n: int) -> int:

        @cache
        def helper(x: int, y: int) -> int:
            if x <= 0 or y <= 0:
                return 0
            return 1 if x == 1 or y == 1 else helper(x -
                                                     1, y) + helper(x, y - 1)

        return helper(m, n)

    # O(m*n), O(m*n)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, j in itertools.product(range(1, m + 1), range(1, n + 1)):
            dp[i][j] = 1 if i == j == 1 else dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([1, 1], 1),
            ([1, 3], 1),
            ([3, 1], 1),
            ([3, 3], 6),
            ([7, 3], 28),
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
