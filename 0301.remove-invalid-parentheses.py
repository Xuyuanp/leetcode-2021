#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (45.31%)
# Likes:    3817
# Dislikes: 181
# Total Accepted:    290.3K
# Total Submissions: 636.8K
# Testcase Example:  '"()())()"'
#
# Given a string s that contains parentheses and letters, remove the minimum
# number of invalid parentheses to make the input string valid.
#
# Return all the possible results. You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: s = "()())()"
# Output: ["(())()","()()()"]
#
#
# Example 2:
#
#
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
#
#
# Example 3:
#
#
# Input: s = ")("
# Output: [""]
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 25
# s consists of lowercase English letters and parentheses '(' and ')'.
# There will be at most 20 parentheses in s.
#
#
#
from typing import List

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1

        res = set()

        def helper(
            curr: str, i: int, left: int, right: int, left_rem: int, right_rem: int
        ):
            if i == len(s):
                if left == right and left_rem == right_rem == 0:
                    res.add(curr)
                return

            if s[i] == "(":
                if left_rem > 0:
                    helper(curr, i + 1, left, right, left_rem - 1, right_rem)

                helper(curr + "(", i + 1, left + 1, right, left_rem, right_rem)

            elif s[i] == ")":
                if right_rem > 0:
                    helper(curr, i + 1, left, right, left_rem, right_rem - 1)
                if left > right:
                    helper(curr + ")", i + 1, left, right + 1, left_rem, right_rem)
            else:
                helper(curr + s[i], i + 1, left, right, left_rem, right_rem)

        helper("", 0, 0, 0, left, right)
        return list(res)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([")("], [""]),
            (["()())()"], ["(())()", "()()()"]),
            (["(a)())()"], ["(a())()", "(a)()()"]),
            (["((((((((((((((((((((aaaaa"], ["aaaaa"]),
        ]
        for args, want in cases:
            got = func(*args)
            if sorted(want) != sorted(got):
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
