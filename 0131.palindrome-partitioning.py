#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (53.91%)
# Likes:    4190
# Dislikes: 130
# Total Accepted:    342.4K
# Total Submissions: 626.3K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
#
# A palindrome string is a string that reads the same backward as forward.
#
#
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
#
#
# Constraints:
#
#
# 1 <= s.length <= 16
# s contains only lowercase English letters.
#
#
#
from functools import lru_cache
from typing import List

# @lc code=start
class Solution:
    # O(n*2^n), O(n^2)
    def partition1(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        @lru_cache(None)
        def is_palindrome(i: int, j: int) -> bool:
            if i >= j:
                return True
            return s[i] == s[j] and is_palindrome(i+1, j-1)

        def backtrack(i: int, pat: List[str]):
            if i == n:
                res.append(list(pat))
                return
            for j in range(i, n):
                if is_palindrome(i, j):
                    pat.append(s[i:j+1])
                    backtrack(j+1, pat)
                    pat.pop(-1)

        backtrack(0, [])
        return res

    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        dp = [[i==j for i in range(n)] for j in range(n)]

        @lru_cache(None)
        def fill_dp(i: int, j: int):
            if 0 <= i <= j < n and s[i] == s[j]:
                dp[i][j] = True
                fill_dp(i-1, j+1)

        def backtrack(i: int, pat: List[str]):
            if i == n:
                res.append(list(pat))
                return
            fill_dp(i, i)
            fill_dp(i, i+1)
            for j in range(i, n):
                if dp[i][j]:
                    pat.append(s[i:j+1])
                    backtrack(j+1, pat)
                    pat.pop(-1)

        backtrack(0, [])
        return res

# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            (['a'], [['a']]),
            (['aab'], [['a','a','b'], ['aa','b']]),
            (['aba'], [['a','b','a'], ['aba']]),
            (['aabc'], [['a','a','b', 'c'], ['aa','b', 'c']]),
            (['aaa'], [['a','a','a'], ['aa','a'], ['a', 'aa'], ['aaa']]),
        ]
        for args, want in cases:
            got = fn(*args)
            if sorted(want) != sorted(got):
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    main()
