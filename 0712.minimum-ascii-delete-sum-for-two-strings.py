#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (60.01%)
# Likes:    1557
# Dislikes: 58
# Total Accepted:    51.7K
# Total Submissions: 85.7K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings s1 and s2, return the lowest ASCII sum of deleted
# characters to make two strings equal.
#
#
# Example 1:
#
#
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
#
#
# Example 2:
#
#
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is
# 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers
# of 433 or 417, which are higher.
#
#
#
# Constraints:
#
#
# 1 <= s1.length, s2.length <= 1000
# s1 and s2 consist of lowercase English letters.
#
#
#

# @lc code=start
from functools import cache


class Solution:
    # O(m*n), O(m*n)=>O(min(m, n))
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == j == 0:
                    pass
                elif i == 0:
                    dp[i][j] = ord(s2[j-1]) + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = ord(s1[i-1]) + dp[i-1][j]
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        ord(s1[i-1])+dp[i-1][j],
                        ord(s2[j-1]) + dp[i][j-1]
                    )

        return dp[m][n]

    # O(m*n), O(min(m, n))
    def minimumDeleteSum1(self, s1: str, s2: str) -> int:
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        m, n = len(s1), len(s2)
        dp = [0] * (n+1)

        for i in range(m+1):
            next_dp = [0]*(n+1)
            for j in range(n+1):
                if i == j == 0:
                    pass
                elif i == 0:
                    next_dp[j] = ord(s2[j-1]) + next_dp[j-1]
                elif j == 0:
                    next_dp[j] = ord(s1[i-1]) + dp[j]
                elif s1[i-1] == s2[j-1]:
                    next_dp[j] = dp[j-1]
                else:
                    next_dp[j] = min(
                        ord(s1[i-1]) + dp[j],
                        ord(s2[j-1])+next_dp[j-1],
                    )
            dp = next_dp

        return dp[n]

    # O(m*n), O(m*n)
    def minimumDeleteSum2(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        @cache
        def helper(i: int, j: int) -> int:
            if i == m and j == n:
                return 0
            if i == m:
                return ord(s2[j]) + helper(i, j+1)
            if j == n:
                return ord(s1[i]) + helper(i+1, j)
            if s1[i] == s2[j]:
                return helper(i+1, j+1)
            return min(
                ord(s1[i]) + helper(i+1, j),
                ord(s2[j]) + helper(i, j+1)
            )

        return helper(0, 0)

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            (['a', 'b'], ord('a')+ord('b')),
            (['sea', 'eat'], 231),
            (['delete', 'leet'], 403)
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
