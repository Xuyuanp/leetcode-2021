#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
#
# algorithms
# Medium (47.65%)
# Likes:    1563
# Dislikes: 70
# Total Accepted:    83.2K
# Total Submissions: 174.7K
# Testcase Example:  '1\n6\n3'
#
# You have d dice and each die has f faces numbered 1, 2, ..., f. You are given
# three integers d, f, and target.
#
# Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7 to
# roll the dice so the sum of the face-up numbers equals target.
#
#
# Example 1:
#
#
# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation:
# You throw one die with 6 faces.  There is only one way to get a sum of 3.
#
#
# Example 2:
#
#
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation:
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
#
#
# Example 3:
#
#
# Input: d = 2, f = 5, target = 10
# Output: 1
# Explanation:
# You throw two dice, each with 5 faces.  There is only one way to get a sum of
# 10: 5+5.
#
#
# Example 4:
#
#
# Input: d = 1, f = 2, target = 3
# Output: 0
# Explanation:
# You throw one die with 2 faces.  There is no way to get a sum of 3.
#
#
# Example 5:
#
#
# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation:
# The answer must be returned modulo 10^9 + 7.
#
#
#
# Constraints:
#
#
# 1 <= d, f <= 30
# 1 <= target <= 1000
#
#
#

# @lc code=start
from collections import defaultdict
from functools import cache


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9 + 7

        @cache
        def helper(d: int, target: int) -> int:
            if target < d or target > d * f:
                return 0
            if d == 1 and target <= f:
                return 1

            return sum(helper(d - 1, target - x) for x in range(1, f + 1)) % mod

        return helper(d, target)

    def numRollsToTarget1(self, d: int, f: int, target: int) -> int:
        if not (d <= target <= d * f):
            return 0
        dp = defaultdict(int)
        dp[0] = 1
        for _ in range(d):
            next_dp = defaultdict(int)
            for i, cnt in dp.items():
                for x in range(1, f + 1):
                    next_dp[i + x] += cnt
            dp = next_dp
        return dp[target] % (10**9 + 7)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([1, 2, 3], 0),
            ([2, 5, 10], 1),
            ([2, 6, 7], 6),
            ([1, 6, 3], 1),
            ([30, 30, 500], 222616187),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
