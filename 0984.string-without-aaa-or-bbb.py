#
# @lc app=leetcode id=984 lang=python3
#
# [984] String Without AAA or BBB
#
# https://leetcode.com/problems/string-without-aaa-or-bbb/description/
#
# algorithms
# Medium (39.11%)
# Likes:    363
# Dislikes: 302
# Total Accepted:    25K
# Total Submissions: 63.3K
# Testcase Example:  '1\n2'
#
# Given two integers a and b, return any string s such that:
#
#
# s has length a + b and contains exactly a 'a' letters, and exactly b 'b'
# letters,
# The substring 'aaa' does not occur in s, and
# The substring 'bbb' does not occur in s.
#
#
#
# Example 1:
#
#
# Input: a = 1, b = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
#
#
# Example 2:
#
#
# Input: a = 4, b = 1
# Output: "aabaa"
#
#
#
# Constraints:
#
#
# 0 <= a, b <= 100
# It is guaranteed such an s exists for the given a and b.
#
#
#


# @lc code=start
class Solution:

    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []

        while a and b:
            if a > b:
                res.append("aab")
                a -= 2
                b -= 1
            elif a < b:
                res.append("bba")
                a -= 1
                b -= 2
            else:
                res.append("ab")
                a -= 1
                b -= 1

        while a > 0:
            res.append("a")
            a -= 1
        while b > 0:
            res.append("b")
            b -= 1

        return "".join(res)


# @lc code=end
def test():

    def no3a3b(s: str) -> bool:
        return len(s.split("aaa")) == 1 and len(s.split("bbb"))

    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([1, 2]),
            ([4, 1]),
            ([3, 3]),
            ([10, 20]),
        ]
        for args in cases:
            got = func(*args)
            if not no3a3b(got) or len(got) != sum(args):
                print(
                    f"  Failed => args: {args}; want no 3a3b, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
