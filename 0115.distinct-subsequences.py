#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (40.42%)
# Likes:    2374
# Dislikes: 100
# Total Accepted:    176.7K
# Total Submissions: 434.7K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given two strings s and t, return the number of distinct subsequences of s
# which equals t.
#
# A string's subsequence is a new string formed from the original string by
# deleting some (can be none) of the characters without disturbing the
# remaining characters' relative positions. (i.e., "ACE" is a subsequence of
# "ABCDE" while "AEC" is not).
#
# It is guaranteed the answer fits on a 32-bit signed integer.
#
#
# Example 1:
#
#
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# rabbbit
# rabbbit
# rabbbit
#
#
# Example 2:
#
#
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.
#
#
#

# @lc code=start
import itertools
from functools import lru_cache


class Solution:
    # O(m*n), O(m*n)
    def numDistinct(self, s: str, t: str) -> int:

        @lru_cache(None)
        def helper(s: str, t: str) -> int:
            if len(s) < len(t):
                return 0
            if len(t) == 1:
                return 1 + helper(s[1:], t) if s[0] == t[0] else helper(
                    s[1:], t)
            res = 0
            for i in range(len(s) - len(t) + 1):
                if s[i] == t[0]:
                    res += helper(s[i + 1:], t[1:])
            return res

        return helper(s, t)

    def numDistinct1(self, s: str, t: str) -> int:

        @lru_cache(None)
        def helper(len_s: int, len_t: int) -> int:
            if len_s < len_t:
                return 0
            if len_t == 1:
                if s[len_s - 1] == t[len_t - 1]:
                    return 1 + helper(len_s - 1, len_t)
                return helper(len_s - 1, len_t)

            res = 0
            for i in range(len_s - len_t + 1):
                if s[len_s - i - 1] == t[len_t - 1]:
                    res += helper(len_s - i - 1, len_t - 1)
            return res

        return helper(len(s), len(t))

    def numDistinct2(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        @lru_cache(None)
        def helper(si: int, ti: int) -> int:
            if ti == n:
                return 1
            if m - si < n - ti:
                return 0
            res = helper(si + 1, ti)
            if s[si] == t[ti]:
                res += helper(si + 1, ti + 1)
            return res

        return helper(0, 0)

    def numDistinct3(self, s: str, t: str) -> int:

        @lru_cache(None)
        def helper(s: str, t: str) -> int:
            if not t:
                return 1
            if len(s) < len(t):
                return 0

            res = helper(s[1:], t)
            if s[0] == t[0]:
                res += helper(s[1:], t[1:])
            return res

        return helper(s, t)

    def numDistinct4(self, s: str, t: str) -> int:
        """
            _ r a b b i t
            0 1 2 3 4 5 6
        _ 0 1 0 0 0 0 0 0
        r 1 1 1 0 0 0 0 0
        a 2 1 1 1 0 0 0 0
        b 3 1 1 1 1 0 0 0
        b 4 1 1 1 2 1 0 0
        b 5 1 1 1 3 3 0 0
        i 6 1 1 1 3 3 3 0
        t 7 1 1 1 3 3 3 3
        """
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [[1 if j == 0 else 0 for j in range(n + 1)] for _ in range(m + 1)]

        for i, j in itertools.product(range(1, m + 1), range(1, n + 1)):
            if i < j:
                continue
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
        return dp[m][n]

    def numDistinct5(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            next_dp = [0] * (n + 1)
            next_dp[0] = 1
            for j in range(1, n + 1):
                if i < j:
                    continue
                next_dp[j] = dp[j]
                if s[i - 1] == t[j - 1]:
                    next_dp[j] += dp[j - 1]
            dp = next_dp
        return dp[n]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (["a", "a"], 1),
            (["a", "b"], 0),
            (["rabbbit", "rabbit"], 3),
            (["babgbag", "bag"], 5),
            (["bakjsdfgakbsjdfhasgdfasdfbag", "bag"], 14),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
