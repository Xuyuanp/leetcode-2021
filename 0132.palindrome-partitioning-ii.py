#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (31.59%)
# Likes:    2461
# Dislikes: 68
# Total Accepted:    180.4K
# Total Submissions: 552.5K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
#
# Example 1:
#
#
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
#
#
# Example 2:
#
#
# Input: s = "a"
# Output: 0
#
#
# Example 3:
#
#
# Input: s = "ab"
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2000
# s consists of lower-case English letters only.
#
#
#

# @lc code=start
from functools import lru_cache


class Solution:

    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [n - x for x in range(n + 1)]

        def check(i: int, j: int):
            while i >= 0 and j < n and s[i] == s[j]:
                dp[i] = min(dp[i], dp[j + 1] + 1)
                i -= 1
                j += 1

        for k in range(n - 1, -1, -1):
            check(k, k)
            check(k, k + 1)

        return dp[0] - 1

    def minCut2(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def is_palindrome(i: int, j: int) -> bool:
            return True if i >= j else s[i] == s[j] and is_palindrome(
                i + 1, j - 1)

        dp = [n - x for x in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if not is_palindrome(i, j):
                    continue
                dp[i] = min(dp[i], dp[j + 1] + 1)

        return dp[0] - 1

    def minCut1(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def is_palindrome(i: int, j: int) -> bool:
            if i >= j:
                return True
            return False if s[i] != s[j] else is_palindrome(i + 1, j - 1)

        @lru_cache(None)
        def dp(i: int) -> int:
            if i == n:
                return 0
            res = float("inf")
            for j in range(i, n):
                if is_palindrome(i, j):
                    res = min(res, dp(j + 1) + 1)
            return res

        return dp(0) - 1


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            (["aab"], 1),
            (["a"], 0),
            (["ab"], 1),
            (["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"], 0),
            (["abacbc"], 1),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    main()
