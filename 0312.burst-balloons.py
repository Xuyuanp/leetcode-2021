#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (54.24%)
# Likes:    4133
# Dislikes: 119
# Total Accepted:    145.2K
# Total Submissions: 266K
# Testcase Example:  '[3,1,5,8]'
#
# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted
# with a number on it represented by an array nums. You are asked to burst all
# the balloons.
#
# If you burst the i^th balloon, you will get nums[i - 1] * nums[i] * nums[i +
# 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as
# if there is a balloon with a 1 painted on it.
#
# Return the maximum coins you can collect by bursting the balloons wisely.
#
#
# Example 1:
#
#
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
# Example 2:
#
#
# Input: nums = [1,5]
# Output: 10
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 500
# 0 <= nums[i] <= 100
#
#
#
from functools import cache
from typing import List


# @lc code=start
class Solution:
    # O(n^3), O(n^2)
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        # dp[i][j] = answer of nums[i:j+1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for x in range(1, n + 1):
            for i in range(1, n - x + 2):
                j = i + x - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] +
                        dp[k + 1][j],
                    )

        return dp[1][n]

    # O(n^3), O(n^2)
    def maxCoins1(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        @cache
        def helper(i: int, j: int) -> int:
            res = 0
            for k in range(i, j + 1):
                res = max(
                    res,
                    helper(i, k - 1) + nums[i - 1] * nums[k] * nums[j + 1] +
                    helper(k + 1, j),
                )
            return res

        return helper(1, n)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1, 5]], 10),
            ([[3, 1, 5, 8]], 167),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
