#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (58.25%)
# Likes:    2591
# Dislikes: 140
# Total Accepted:    133.3K
# Total Submissions: 226.3K
# Testcase Example:  '"2-1-1"'
#
# Given a string expression of numbers and operators, return all possible
# results from computing all the different possible ways to group numbers and
# operators. You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
#
# Example 2:
#
#
# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
#
#
#
# Constraints:
#
#
# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.
#
#
#
from typing import List

# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)

        def parse_tokens(i: int):
            j = i
            while j < n and str.isdigit(expression[j]):
                j += 1
            yield int(expression[i:j])
            if j < n:
                yield expression[j]
                yield from parse_tokens(j + 1)

        tokens = list(parse_tokens(0))

        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }

        def helper(i: int, j: int) -> List[int]:
            if j - i == 0:
                return [tokens[i]]
            res = []
            for k in range(i + 1, j, 2):
                left = helper(i, k - 1)
                op = ops[tokens[k]]
                right = helper(k + 1, j)
                for x in left:
                    for y in right:
                        res.append(op(x, y))
            return res

        return helper(0, len(tokens) - 1)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (["2-1-1"], [0, 2]),
            (["2*3-4*5"], [-34, -14, -10, -10, 10]),
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
