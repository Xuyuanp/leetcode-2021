#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Easy (49.78%)
# Likes:    2969
# Dislikes: 251
# Total Accepted:    331.1K
# Total Submissions: 664.4K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# Given two strings s and t, return true if s is a subsequence of t, or false
# otherwise.
#
# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (i.e., "ace" is a
# subsequence of "abcde" while "aec" is not).
#
#
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
#
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# s and t consist only of lowercase English letters.
#
#
#
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k
# >= 10^9, and you want to check one by one to see if t has its subsequence. In
# this scenario, how would you change your code?
#

# @lc code=start
from functools import cache


class Solution:
    # O(m*n), O(m*n)
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return False

        @cache
        def helper(i: int, j: int) -> bool:
            if i == m:
                return True
            if j == n:
                return False
            return s[i] == t[j] and helper(i + 1, j + 1) or helper(i, j + 1)

        return helper(0, 0)

    # O(n), O(1)
    def isSubsequence2(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return False

        i = j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == m


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (["", "ab"], True),
            (["a", "ab"], True),
            (["a", "ba"], True),
            (["abc", "ahbgdc"], True),
            (["axc", "ahbgdc"], False),
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
