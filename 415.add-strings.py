#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (49.29%)
# Likes:    1988
# Dislikes: 408
# Total Accepted:    319.4K
# Total Submissions: 646.8K
# Testcase Example:  '"11"\n"123"'
#
# Given two non-negative integers, num1 and num2 represented as string, return
# the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling
# large integers (such as BigInteger). You must also not convert the inputs to
# integers directly.
#
#
# Example 1:
#
#
# Input: num1 = "11", num2 = "123"
# Output: "134"
#
#
# Example 2:
#
#
# Input: num1 = "456", num2 = "77"
# Output: "533"
#
#
# Example 3:
#
#
# Input: num1 = "0", num2 = "0"
# Output: "0"
#
#
#
# Constraints:
#
#
# 1 <= num1.length, num2.length <= 10^4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.
#
#
#
from itertools import zip_longest

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ascii_zero = ord('0')
        x = 0
        res = []
        for c1, c2 in zip_longest(reversed(num1), reversed(num2), fillvalue='0'):
            n1, n2 = ord(c1) - ascii_zero, ord(c2) - ascii_zero
            sum_ = n1 + n2 + x
            res.append(chr(sum_ % 10 + ascii_zero))
            x = sum_ // 10
        if x > 0:
            res.append('1')

        return ''.join(reversed(res))


# @lc code=end

if __name__ == "__main__":
    print(Solution().addStrings("11", "123"))
    print(Solution().addStrings("1", "9"))
    print(Solution().addStrings("91", "9"))
    print(Solution().addStrings("0", "9"))
    print(Solution().addStrings("999991", "9"))
