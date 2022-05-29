#
# @lc app=leetcode id=1278 lang=python3
#
# [1278] Palindrome Partitioning III
#
# https://leetcode.com/problems/palindrome-partitioning-iii/description/
#
# algorithms
# Hard (61.41%)
# Likes:    551
# Dislikes: 12
# Total Accepted:    15K
# Total Submissions: 24.6K
# Testcase Example:  '"abc"\n2'
#
# You are given a string s containing lowercase letters and an integer k. You
# need to :
#
#
# First, change some characters of s to other lowercase English letters.
# Then divide s into k non-empty disjoint substrings such that each substring
# is a palindrome.
#
#
# Return the minimal number of characters that you need to change to divide the
# string.
#
#
# Example 1:
#
#
# Input: s = "abc", k = 2
# Output: 1
# Explanation: You can split the string into "ab" and "c", and change 1
# character in "ab" to make it palindrome.
#
#
# Example 2:
#
#
# Input: s = "aabbc", k = 3
# Output: 0
# Explanation: You can split the string into "aa", "bb" and "c", all of them
# are palindrome.
#
# Example 3:
#
#
# Input: s = "leetcode", k = 8
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= k <= s.length <= 100.
# s only contains lowercase English letters.
#
#
#

# @lc code=start
from functools import cache


class Solution:
    # O(n*n*k), O(n*k)
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def make_palindrome(start: int, end: int) -> int:
            if start >= end:
                return 0
            return make_palindrome(start + 1, end - 1) + (
                0 if s[start] == s[end] else 1
            )

        @cache
        def helper(start: int, kk: int) -> int:
            if kk == 1:
                return make_palindrome(start, n - 1)

            res = float("inf")

            for i in range(start, n - kk + 1):
                curr = make_palindrome(start, i)
                res = min(res, curr + helper(i + 1, kk - 1))

            return res

        return helper(0, k)

    def palindromePartition1(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def make_palindrome(start: int, end: int) -> int:
            if start >= end:
                return 0
            return make_palindrome(start + 1, end - 1) + (
                0 if s[start] == s[end] else 1
            )

        @cache
        def helper(end: int, kk: int) -> int:
            if kk == 1:
                return make_palindrome(0, end - 1)

            res = float("inf")

            for i in range(end, kk - 1, -1):
                curr = make_palindrome(i - 1, end - 1)
                res = min(res, curr + helper(i - 1, kk - 1))

            return res

        return helper(n, k)

    def palindromePartition2(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[float("inf")] * (k + 1) for _ in range(n + 1)]

        @cache
        def make_palindrome(start: int, end: int) -> int:
            if start >= end:
                return 0
            return make_palindrome(start + 1, end - 1) + (
                0 if s[start] == s[end] else 1
            )

        for i in range(1, n + 1):
            dp[i][1] = make_palindrome(0, i - 1)
            for kk in range(2, min(i, k) + 1):
                for j in range(i, kk - 1, -1):
                    curr = make_palindrome(j - 1, i - 1)
                    dp[i][kk] = min(dp[i][kk], curr + dp[j - 1][kk - 1])

        return dp[n][k]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (["abc", 2], 1),
            (["aabbc", 3], 0),
            (["leetcode", 8], 0),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
