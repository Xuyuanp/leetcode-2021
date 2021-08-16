#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (37.47%)
# Likes:    4592
# Dislikes: 698
# Total Accepted:    545.5K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(m*n), O(m*n)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        if m == 1:
            return matrix[0]
        if n == 1:
            return [row[0] for row in matrix]
        transm = list(zip(*matrix))
        res = []
        loops = min(m, n)//2
        for i in range(loops):
            res += matrix[i][i:n-i-1]
            res += transm[n-i-1][i:m-i-1]
            res += matrix[m-i-1][n-i-1:i:-1]
            res += transm[i][m-i-1:i:-1]

        if n > m and m%2 == 1:
            res += matrix[m//2][loops:n-loops]
        elif m > n and n%2 == 1:
            res += transm[n//2][loops:m-loops]
        elif m%2== n%2==1:
            res.append(matrix[m//2][n//2])
        return res

    # O(m*n), O(1)
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        if m == 1:
            return matrix[0]
        if n == 1:
            return [row[0] for row in matrix]

        res = [0]*m*n
        loops = min(m, n)//2
        index = 0
        for i in range(loops):
            for col in range(i, n-1-i):
                res[index] = matrix[i][col]
                index += 1
            for row in range(i, m-1-i):
                res[index] = matrix[row][n-1-i]
                index += 1
            for col in range(n-1-i, i, -1):
                res[index] = matrix[m-1-i][col]
                index += 1
            for row in range(m-1-i, i, -1):
                res[index] = matrix[row][i]
                index += 1

        if n > m and m%2 == 1:
            for col in range(loops, n-loops):
                res[index] = matrix[m//2][col]
                index += 1
        elif m > n and n%2 == 1:
            for row in range(loops, m-loops):
                res[index] = matrix[row][n//2]
                index += 1
        elif m%2 == n%2 == 1:
            res[index] = matrix[m//2][n//2]

        return res

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        if m == 1:
            return matrix[0]
        if n == 1:
            return [row[0] for row in matrix]

        return list(matrix[0]) + self.spiralOrder2(list(zip(*matrix[1:]))[::-1])


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([[[1]]], [1]), # 1x1
            ([[[1,2,3]]], [1,2,3]), # 1x3
            ([[[1],[2],[3]]], [1,2,3]), # 3x1
            ([[[1,2],[3,4]]], [1,2,4,3]), # 2x2
            ([[[1,2],
               [3,4],
               [5,6]]], [1,2,4,6,5,3]), # 3x2
            ([[[1,2,3],
               [4,5,6]]], [1,2,3,6,5,4]), # 2x3
            ([[[1,2,3],
               [4,5,6],
               [7,8,9]]], [1,2,3,6,9,8,7,4,5]),  # 3x3
            ([[[ 1, 2, 3, 4],
               [ 5, 6, 7, 8],
               [ 9,10,11,12]]], [1,2,3,4,8,12,11,10,9,5,6,7]), # 3x4
            ([[[ 1, 2, 3],
               [ 4, 5, 6],
               [ 7, 8, 9],
               [10,11,12]]], [1,2,3,6,9,12,11,10,7,4,5,8]), # 4x3
            ([[[ 1, 2, 3, 4],
               [ 5, 6, 7, 8],
               [ 9,10,11,12],
               [13,14,15,16]]], [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]), # 4*4
            ([[[ 1, 2, 3, 4, 5],
               [ 6, 7, 8, 9,10],
               [11,12,13,14,15],
               [16,17,18,19,20],
               [21,22,23,24,25]]], [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13]), # 5x5
            ([[[2,3,4],
               [5,6,7],
               [8,9,10],
               [11,12,13],
               [14,15,16]]], [2,3,4,7,10,13,16,15,14,11,8,5,6,9,12]), # 5x3
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
