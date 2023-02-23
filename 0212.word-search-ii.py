#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (37.83%)
# Likes:    4419
# Dislikes: 153
# Total Accepted:    339.8K
# Total Submissions: 895K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#  '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
#
#
# Example 1:
#
#
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
#
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
#
#
#
from collections import defaultdict
from typing import List


# @lc code=start
class TrieNode:

    def __init__(self):
        self.word = ""
        self.valid = False
        self.children = defaultdict(TrieNode)

    def add(self, word: str):
        node = self
        for char in word:
            node = node.children[char]
        node.valid = True
        node.word = word


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.add(word)

        m, n = len(board), len(board[0])
        VISITED = "*"
        res = set()

        def dfs(i: int, j: int, node: TrieNode):
            if node.valid:
                res.add(node.word)

            char = board[i][j]
            board[i][j] = VISITED
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] in node.children:
                    dfs(x, y, node.children[board[x][y]])
            board[i][j] = char

        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char in root.children:
                    dfs(i, j, root.children[char])

        return list(res)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[["a", "a"]], ["aaa"]], []),
            (
                [
                    [
                        ["o", "a", "a", "n"],
                        ["e", "t", "a", "e"],
                        ["i", "h", "k", "r"],
                        ["i", "f", "l", "v"],
                    ],
                    ["oath", "pea", "eat", "rain", "hklf", "hf"],
                ],
                ["oath", "eat", "hklf", "hf"],
            ),
            ([[["a"]], ["a"]], ["a"]),
            ([[["a", "b"], ["c", "d"]], ["abcb"]], []),
            (
                [
                    [
                        ["o", "a", "a", "n"],
                        ["e", "t", "a", "e"],
                        ["i", "h", "k", "r"],
                        ["i", "f", "l", "v"],
                    ],
                    ["oath", "pea", "eat", "rain"],
                ],
                ["eat", "oath"],
            ),
        ]
        for args, want in cases:
            got = func(*args)
            if sorted(want) != sorted(got):
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
