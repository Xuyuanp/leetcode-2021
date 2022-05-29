#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Medium (43.70%)
# Likes:    7708
# Dislikes: 203
# Total Accepted:    761.8K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(n), O(1)
    def rob(self, nums: List[int]) -> int:
        pre, curr = 0, nums[0]
        for money in nums[1:]:
            pre, curr = curr, max(pre + money, curr)
        return curr

    # O(n), O(n)
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[1, 2]], 2),
            ([[2, 1]], 2),
            ([[1, 2, 3, 1]], 4),
            ([[2, 7, 9, 3, 1]], 12),
            ([[2, 7, 9, 6, 1]], 13),
            ([[2, 1, 1, 2]], 4),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()
