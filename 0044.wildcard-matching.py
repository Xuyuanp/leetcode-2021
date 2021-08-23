#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (25.80%)
# Likes:    3524
# Dislikes: 162
# Total Accepted:    326.5K
# Total Submissions: 1.3M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*' where:
#
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
#
# The matching should cover the entire input string (not partial).
#
#
# Example 1:
#
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#
#
# Example 3:
#
#
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
#
#
# Example 4:
#
#
# Input: s = "adceb", p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
#
#
# Example 5:
#
#
# Input: s = "acdcb", p = "a*c?b"
# Output: false
#
#
#
# Constraints:
#
#
# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.
#
#
#

# @lc code=start
class Solution:
    # O(m*n), O(m*n) => O(n)
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and p[j-1] == '*'

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
        return dp[m][n]

    # O(m*n), O(n)
    def isMatch1(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [False] * (n+1)
        dp[0] = True

        for j in range(1, n+1):
            dp[j] = dp[j-1] and p[j-1] == '*'

        for i in range(1, m+1):
            next_dp = [False] * (n+1)
            for j in range(1, n+1):
                if p[j-1] == '*':
                    next_dp[j] = next_dp[j-1] or dp[j]
                else:
                    next_dp[j] = dp[j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
            dp = next_dp
        return dp[n]

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            (['aa', 'a'], False),
            (['aa', '*'], True),
            (['cb', '?a'], False),
            (['adceb', '*a*b'], True),
            (['acdcb', 'a*c?b'], False),
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
