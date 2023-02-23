#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (30.94%)
# Likes:    11853
# Dislikes: 735
# Total Accepted:    1.4M
# Total Submissions: 4.4M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
# Example 3:
#
#
# Input: s = "a"
# Output: "a"
#
#
# Example 4:
#
#
# Input: s = "ac"
# Output: "a"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),
#
#
#
from typing import Tuple


# @lc code=start
class Solution:

    def longestPalindrome(self, s: str) -> str:
        # time: O(n^2), space: O(1)
        n = len(s)
        if n <= 1:
            return s

        def helper(left: int, right: int) -> Tuple[int, int]:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return (left + 1, right - 1)

        start = end = 0

        for i in range(n):
            (l1, r1) = helper(i, i)
            (l2, r2) = helper(i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]

    def longestPalindrome1(self, s: str) -> str:
        # dp: dp[i][j] presents if the substring s[i:j+1] is a palindrome
        # time: O(n^2), space: O(n^2)
        n = len(s)
        if n <= 1:
            return s
        dp = [[i == j for j in range(n)] for i in range(n)]
        res = s[0]
        for j in range(n):
            for k in range(j):
                i = j - k - 1
                if s[i] == s[j]:
                    dp[i][j] = j - i == 1 or dp[i + 1][j - 1]
                    if dp[i][j] and j - i + 1 > len(res):
                        res = s[i:j + 1]

        return res


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ("cbbcd", "cbbc"),
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("aacabdkacaa", "aca"),
    ]
    for s, want in cases:
        got = sol.longestPalindrome1(s)
        if want != got:
            print(f"Failed => args: {s}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
