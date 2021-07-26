#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (66.94%)
# Likes:    8632
# Dislikes: 354
# Total Accepted:    787.7K
# Total Submissions: 1.2M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
#
# 1 <= n <= 8
#
#
#

from typing import List

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(pat: str, left: int, right: int):
            if right >= left >= 0:
                if right == 0:
                    res.append(pat)
                    return
                backtrack(pat + '(', left-1, right)
                backtrack(pat + ')', left, right-1)


        backtrack('', n, n)

        return res

# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    cases = [
        (1, ['()']),
        (2, ['()()', '(())']),
        (3, ['()()()', '((()))', '(())()', '()(())', '(()())']),
    ]
    for n, want in cases:
        got = sol.generateParenthesis(n)
        if sorted(want) != sorted(got):
            print(f'Failed => args: {n}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
