#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Medium (33.64%)
# Likes:    2948
# Dislikes: 157
# Total Accepted:    223.8K
# Total Submissions: 661.4K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
# s1 and s2.
#
# An interleaving of two strings s and t is a configuration where they are
# divided into non-empty substrings such that:
#
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 +
# t3 + s3 + ...
#
#
# Note: a + b is the concatenation of strings a and b.
#
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
#
# Example 3:
#
#
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
#
#
#
# Constraints:
#
#
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
#
#
#
# Follow up: Could you solve it using only O(s2.length) additional memory
# space?
#
#

# @lc code=start
from functools import lru_cache


class Solution:
    # O(m*n), O(m*n)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m+n != len(s3):
            return False
        dp = [[False]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1]
                else:
                    dp[i][j] = \
                        dp[i-1][j] and s1[i-1] == s3[i+j-1] or \
                        dp[i][j-1] and s2[j-1] == s3[i+j-1]

        return dp[m][n]

    # O(m*n), O(min(m, n))
    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        m, n = len(s1), len(s2)
        if m+n != len(s3):
            return False

        dp = [False] * (n+1)

        for i in range(m+1):
            for j in range(n+1):
                if i == j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i-1] == s3[i-1]
                else:
                    dp[j] = \
                        dp[j] and s1[i-1] == s3[i+j-1] or \
                        dp[j-1] and s2[j-1] == s3[i+j-1]

        return dp[n]

    # O(m*n), O(min(m, n))
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        m, n = len(s1), len(s2)
        if m+n != len(s3):
            return False

        @lru_cache(None)
        def is_interleave(s1: str, s2: str, s3: str) -> bool:
            if len(s1) == 0:
                return s2 == s3
            if len(s2) == 0:
                return s1 == s3

            return s1[0] == s3[0] and is_interleave(s1[1:], s2, s3[1:]) or \
                s2[0] == s3[0] and is_interleave(s1, s2[1:], s3[1:])

        return is_interleave(s1, s2, s3)

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            (['', '', ''], True),
            (['aabcc', 'dbbca', 'aadbbcbcac'], True),
            (['aabcc', 'dbbca', 'aadbbbaccc'], False),
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