#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#
# https://leetcode.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (52.26%)
# Likes:    2062
# Dislikes: 38
# Total Accepted:    89.9K
# Total Submissions: 170.2K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings word1 and word2, return the minimum number of steps
# required to make word1 and word2 the same.
#
# In one step, you can delete exactly one character in either string.
#
#
# Example 1:
#
#
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
#
#
# Example 2:
#
#
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= word1.length, word2.length <= 500
# word1 and word2 consist of only lowercase English letters.
#
#
#

# @lc code=start
class Solution:
    # O(m*n), O(m*n)
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [
            [0 if i > 0 and j > 0 else i + j for j in range(n + 1)]
            for i in range(m + 1)
        ]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[m][n]

    # O(m*n), O(min(m, n))
    def minDistance1(self, word1: str, word2: str) -> int:
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
                    next_dp[j] = min(dp[j], next_dp[j - 1]) + 1
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
            (["a", "b"], 2),
            (["a", "a"], 0),
            (["a", "ab"], 1),
            (["ab", "a"], 1),
            (["aaa", "a"], 2),
            (["sea", "eat"], 2),
            (["leetcode", "etco"], 4),
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
