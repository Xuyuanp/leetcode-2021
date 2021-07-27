#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (30.20%)
# Likes:    5657
# Dislikes: 198
# Total Accepted:    395.2K
# Total Submissions: 1.3M
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
#
# Example 1:
#
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#
#
# Example 2:
#
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#
#
# Example 3:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.
#
#
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = deque([0])
        for c in s:
            if c == '(':
                stack.append(0)
            elif len(stack) > 1:
                val = stack.pop()
                stack[-1] += val + 2
                res = max(res, stack[-1])
            else:
                stack = deque([0])
        return res

    def longestValidParentheses2(self, s: str) -> int:
        res = 0
        dp = [0] * len(s)

        for i in range(1, len(s)):
            if s[i] != ')':
                continue
            if s[i-1] == '(':
                dp[i] = 2 + dp[i-2]  # we don't need to check if i-2 >= 0, because dp[-1] == 0
            else:
                mirror = i - dp[i-1] - 1
                if mirror >= 0 and s[mirror] == '(':
                    dp[i] = dp[i-1] + 2 + dp[mirror-1] # the same as above
            res = max(res, dp[i])

        return res

    def longestValidParentheses1(self, s: str) -> int:
        res = 0
        dp = defaultdict(int)

        for i in range(1, len(s)):
            if s[i] != ')':
                continue
            if s[i-1] == '(':
                dp[i] = dp[i-2] + 2
            else:
                mirror = i - dp[i-1] - 1
                if mirror >= 0 and s[mirror] == '(':
                    dp[i] = dp[i-1] + dp[mirror-1] + 2
            res = max(res, dp[i])

        return res

# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ('', 0),
        ('(()', 2),
        (')()())', 4),
        ('(()))())(', 4),
        ('((()))', 6),
    ]
    for s, want in cases:
        got = sol.longestValidParentheses(s)
        if got != want:
            print(f'Failed => args: {s}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
