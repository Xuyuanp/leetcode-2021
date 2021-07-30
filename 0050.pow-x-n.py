#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (31.32%)
# Likes:    2765
# Dislikes: 4086
# Total Accepted:    679.1K
# Total Submissions: 2.2M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
#
#
# Example 1:
#
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
#
# Example 2:
#
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
#
#
# Example 3:
#
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
#
#
#
# Constraints:
#
#
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= x^n <= 10^4
#
#
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if n < 0:
            return 1/self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n%2 == 1:
            return self.myPow(x, n-1)*x
        v = self.myPow(x, n//2)
        return v * v

# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([0, 2], 0),
            ([1, 2], 1),
            ([4, 2], 16),
            ([4, -2], 0.0625),
            ([2.0000, -2], 0.25),
            ([2.1, 3], 9.261),
        ]
        for args, want in cases:
            got = fn(*args)
            if abs(got-want) > 0.00001:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()
