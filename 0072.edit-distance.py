#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (47.93%)
# Likes:    6162
# Dislikes: 73
# Total Accepted:    376.5K
# Total Submissions: 781.7K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
#
# Insert a character
# Delete a character
# Replace a character
#
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
#
# Constraints:
#
#
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
#
#
#
from functools import lru_cache

# @lc code=start
class Solution:
    # O(m*n), O(m*n)
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(maxsize=None)
        def helper(word1: str, word2: str) -> int:
            if not word1:
                return len(word2)
            if not word2:
                return len(word1)
            if word1[0] == word2[0]:
                return helper(word1[1:], word2[1:])

            return 1 + min(
                helper(word1[1:], word2),  # delete word1[0]
                helper(word1, word2[1:]),  # delete word2[0]
                helper(word1[1:], word2[1:]),  # replace either word1[0] or word2[0]
            )

        res = helper(word1, word2)
        return res

    # O(m*n), O(m*n)
    def minDistance1(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if 0 in (i, j):
                    dp[i][j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1],
                    )
        return dp[m][n]

    # O(m*n), O(min(m, n))
    def minDistance2(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)
        dp = [0] * (n + 1)
        for i in range(m + 1):
            next_dp = [0] * (n + 1)
            for j in range(n + 1):
                if i == 0 or j == 0:
                    next_dp[j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    next_dp[j] = dp[j - 1]
                else:
                    next_dp[j] = 1 + min(
                        dp[j],
                        next_dp[j - 1],
                        dp[j - 1],
                    )
            dp = next_dp
        return dp[n]

    # O(m*n), O(m*n)
    def minDistance3(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @lru_cache(maxsize=None)
        def helper(i: int, j: int) -> int:
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)

            return 1 + min(
                helper(i + 1, j),  # delete word1[i]
                helper(i, j + 1),  # delete word2[j]
                helper(i + 1, j + 1),  # replace either word1[i] or word2[j]
            )

        return helper(0, 0)

    def minDistance4(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if 0 in (i, j):
                return i + j
            if word1[i - 1] == word2[j - 1]:
                return dp(i - 1, j - 1)

            return 1 + min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1))

        return dp(m, n)


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            (("horse", "ros"), 3),
            (("intention", "execution"), 5),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()
