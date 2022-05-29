#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (58.79%)
# Likes:    3774
# Dislikes: 43
# Total Accepted:    238.4K
# Total Submissions: 405.2K
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
#
#
# For example, "ace" is a subsequence of "abcde".
#
#
# A common subsequence of two strings is a subsequence that is common to both
# strings.
#
#
# Example 1:
#
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
#
# Example 2:
#
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
#
# Example 3:
#
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
#
# Constraints:
#
#
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
#
#
#

# @lc code=start
from functools import cache


class Solution:
    # O(m*n), O(m*n). DP
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

    # O(m*n), O(m*n).
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        @cache
        def helper(i: int, j: int) -> int:
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + helper(i + 1, j + 1)
            return max(helper(i + 1, j), helper(i, j + 1))

        return helper(0, 0)

    # O(m*n), O(min(m, n)). DP
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            next_dp = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    next_dp[j] = dp[j - 1] + 1
                else:
                    next_dp[j] = max(dp[j], next_dp[j - 1])
            dp = next_dp
        return dp[n]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            (["a", "a"], 1),
            (["a", "b"], 0),
            (["a", "ab"], 1),
            (["ab", "a"], 1),
            (["abc", "def"], 0),
            (["abc", "abc"], 3),
            (["abcde", "ace"], 3),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
