#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.21%)
# Likes:    8090
# Dislikes: 332
# Total Accepted:    1.5M
# Total Submissions: 3.8M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
#
# Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: s = "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: s = "{[]}"
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#

# @lc code=start
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        parens = {"}": "{", "]": "[", ")": "("}

        stack = deque()
        for c in s:
            if c not in parens:
                stack.append(c)
                continue
            if not stack or stack[-1] != parens[c]:
                return False
            stack.pop()

        return len(stack) == 0


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ("]", False),
        ("[", False),
        ("()[]{}", True),
        ("(])", False),
        ("([{}])", True),
    ]
    for s, want in cases:
        got = sol.isValid(s)
        if want != got:
            print(f"Failed => args: {s}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
