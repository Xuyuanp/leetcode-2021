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

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        loops = n//2
        first = 1
        for i in range(loops):
            step = n-1-i*2
            for j in range(i, n-i-1):
                matrix[    i][    j] = first + step * 0
                matrix[    j][n-i-1] = first + step * 1
                matrix[n-i-1][n-j-1] = first + step * 2
                matrix[n-j-1][    i] = first + step * 3
                first += 1

            first += 3*step

        if n%2 == 1:
            matrix[loops][loops] = first
        return matrix

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([1], [[1]]),
            ([2], [[1,2],
                   [4,3]]),
            ([3], [[1,2,3],
                   [8,9,4],
                   [7,6,5]]),
            ([4], [[ 1, 2, 3, 4],
                   [12,13,14, 5],
                   [11,16,15, 6],
                   [10, 9, 8, 7],]),
            ([5], [[ 1, 2, 3, 4, 5],
                   [16,17,18,19, 6],
                   [15,24,25,20, 7],
                   [14,23,22,21, 8],
                   [13,12,11,10, 9]])
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
