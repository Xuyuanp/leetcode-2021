#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (50.69%)
# Likes:    6547
# Dislikes: 546
# Total Accepted:    879.9K
# Total Submissions: 1.7M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
#
#
# Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# Example 2:
#
#
# Input: digits = ""
# Output: []
#
#
# Example 3:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
#
#

from typing import List


# @lc code=start
class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        table = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []

        def backtrack(digits: str, pat: List[str]):
            if not digits:
                res.append("".join(pat))
                return
            for c in table[digits[0]]:
                pat.append(c)
                backtrack(digits[1:], pat)
                pat.pop()

        backtrack(digits, [])

        return res


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ("", []),
        ("2", ["a", "b", "c"]),
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ]
    for args, want in cases:
        got = sol.letterCombinations(args)
        if want != got:
            print(f"Failed => args: {args}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
