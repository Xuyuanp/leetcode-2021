#
# @lc app=leetcode id=940 lang=python3
#
# [940] Distinct Subsequences II
#
# https://leetcode.com/problems/distinct-subsequences-ii/description/
#
# algorithms
# Hard (41.33%)
# Likes:    771
# Dislikes: 23
# Total Accepted:    18.4K
# Total Submissions: 43.7K
# Testcase Example:  '"abc"'
#
# Given a string s, return the number of distinct non-empty subsequences of s.
# Since the answer may be very large, return it modulo 10^9 + 7.
# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (i.e., "ace" is a
# subsequence of "abcde" while "aec" is not.)
#
# Example 1:
#
#
# Input: s = "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc",
# and "abc".
#
#
# Example 2:
#
#
# Input: s = "aba"
# Output: 6
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and
# "aba".
#
#
# Example 3:
#
#
# Input: s = "aaa"
# Output: 3
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2000
# s consists of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    # O(n), O(n)
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        # dp[i] is the number of distinct non-empty subsequences of s[:i] (include '')
        # if use s[i-1], dp[i] = dp[i-1]
        # if skip s[i-1], dp[i] = dp[i-1]
        # so dp[i] = dp[i-1]*2
        # duplicated: dp[last index of s[i-1]-1]
        # res = dp[n]-1
        dp[0] = 1
        last = {}
        for i, c in enumerate(s, 1):
            dp[i] = dp[i - 1] * 2
            if c in last:
                dp[i] -= dp[last[c] - 1]
            last[c] = i
        return (dp[n] - 1) % (10**9 + 7)

    # O(n), O(1)
    def distinctSubseqII1(self, s: str) -> int:
        ends = [0] * 26
        # ends[ord(c)-ord('a')] is the number of distinct subsequences end with c
        orda = ord("a")
        for c in s:
            ends[ord(c) - orda] = sum(ends) + 1
        return sum(ends) % (10**9 + 7)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [(["aaa"], 3), (["aba"], 6), (["abc"], 7)]
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
