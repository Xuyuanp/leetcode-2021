#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (37.85%)
# Likes:    6815
# Dislikes: 266
# Total Accepted:    749.9K
# Total Submissions: 2M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
#
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#
from typing import List

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        VISITED = '*'
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True

            board[i][j] = VISITED
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n:
                    if dfs(x, y, k+1):
                        return True
            board[i][j] = word[k]

            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB'], False),
            ([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'SEE'], True),
            ([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED'], True),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
