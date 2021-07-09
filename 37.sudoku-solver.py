#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (48.53%)
# Likes:    3127
# Dislikes: 114
# Total Accepted:    252.3K
# Total Submissions: 519.3K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes
# of the grid.
#
#
# The '.' character indicates empty cells.
#
#
# Example 1:
#
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output:
# [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is
# shown below:
#
#
#
#
#
# Constraints:
#
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.
#
#
#

# @lc code=start
from typing import List, Tuple, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]):
        digits = set(str(i) for i in range(1, 10))
        filled = set()

        def is_empty(row: int, col: int):
            return board[row][col] == '.'

        def get_candidates(row: int, col: int) -> Set[str]:
            filled.clear()
            anchor_row = (row//3)*3
            anchor_col = (col//3)*3

            for i in range(9):
                if not is_empty(row, i):
                    filled.add(board[row][i])
                if not is_empty(i, col):
                    filled.add(board[i][col])
                sub_row = anchor_row + i // 3
                sub_col = anchor_col + i % 3
                if not is_empty(sub_row, sub_col):
                    filled.add(board[sub_row][sub_col])

            return digits - filled

        def next_cell(row: int, col: int) -> Tuple[int, int]:
            row += (col + 1) // 9
            col = (col + 1) % 9
            return (row, col)

        def put_cell(row: int, col: int, x: str):
            board[row][col] = x

        def clear_cell(row: int, col: int):
            board[row][col] = '.'

        def backtrack(row: int, col: int) -> bool:
            if row == 9:
                return True
            (next_row, next_col) = next_cell(row, col)
            if not is_empty(row, col):
                return backtrack(next_row, next_col)

            for x in get_candidates(row, col):
                put_cell(row, col, x)

                if backtrack(next_row, next_col):
                    return True

                clear_cell(row, col)

            return False

        backtrack(0, 0)

# @lc code=end
