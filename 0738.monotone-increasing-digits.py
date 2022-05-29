#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#
# https://leetcode.com/problems/monotone-increasing-digits/description/
#
# algorithms
# Medium (45.96%)
# Likes:    684
# Dislikes: 79
# Total Accepted:    31.5K
# Total Submissions: 68.4K
# Testcase Example:  '10'
#
# An integer has monotone increasing digits if and only if each pair of
# adjacent digits x and y satisfy x <= y.
#
# Given an integer n, return the largest number that is less than or equal to n
# with monotone increasing digits.
#
#
# Example 1:
#
#
# Input: n = 10
# Output: 9
#
#
# Example 2:
#
#
# Input: n = 1234
# Output: 1234
#
#
# Example 3:
#
#
# Input: n = 332
# Output: 299
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^9
#
#
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        res = 0
        power = 0
        while n > 0:
            high, low = divmod(n, 10)
            if high % 10 > low:
                res = 10 ** (power + 1) - 1
                high -= 1
            else:
                res += low * 10**power
            n = high
            power += 1
        return res


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([9], 9),
            ([10], 9),
            ([1234], 1234),
            ([332], 299),
            ([302], 299),
            ([1021], 999),
            ([12321], 12299),
            ([12221], 11999),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    main()
