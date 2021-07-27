#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
from typing import List

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(x1: int, y1: int, x2: int, y2: int) -> bool:
            if x1 == x2 or y1 == y2:
                return False
            if x2 - x1 == y2 - y1 == 1:
                return target == matrix[x1][y1]
            px = (x1 + x2)//2
            py = (y1 + y2)//2
            val = matrix[px][py]

            if target == val:
                return True

            if target < val:
                return search(x1, y1, px, py) or \
                    search(px, y1, x2, py) or \
                    search(x1, py, px, y2)
            if target > val:
                return search(px, py, x2, y2) or \
                    search(px, y1, x2, py) or \
                    search(x1, py, px, y2)

            return False

        return search(0, 0, len(matrix), len(matrix[0]))

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        row = m-1
        col = 0

        while 0 <= row < m and 0 <= col < n:
            val = matrix[row][col]
            if val == target:
                return True
            if val < target:
                col += 1
            else:
                row -= 1
        return False


# @lc code=end


if __name__ == "__main__":
    print(Solution().searchMatrix([
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
    ], target=15))
