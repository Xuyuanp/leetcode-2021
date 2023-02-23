#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (48.18%)
# Likes:    13031
# Dislikes: 620
# Total Accepted:    1.5M
# Total Submissions: 3.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
#
# Example 1:
#
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: 1
#
#
# Example 3:
#
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -10^5 <= nums[i] <= 10^5
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
from typing import List


# @lc code=start
class Solution:
    # O(n), O(n). dp
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)

    # O(n), O(n).
    def maxSubArray1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, n):
            # dp[i] only need dp[i-1] => reduce dim
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            res = max(res, dp[i])
        return res

    # O(n), O(1).
    def maxSubArray2(self, nums: List[int]) -> int:
        n = len(nums)
        dp_i_1 = nums[0]
        res = dp_i_1
        for i in range(1, n):
            dp_i = max(nums[i], dp_i_1 + nums[i])
            res = max(res, dp_i)
            dp_i_1 = dp_i
        return res

    # O(n), O(1)
    def maxSubArray3(self, nums: List[int]) -> int:
        res = curr = nums[0]
        for x in nums[1:]:
            curr = max(x, curr + x)
            res = max(res, curr)
        return res

    def maxSubArray4(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            res = max(nums[i], res)
        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[-2, 1]], 1),
            ([[-2, -1]], -1),
            ([[-2, 1, -3, 4, -1, 2, 1, -5, 4]], 6),
            ([[5, 4, -1, 7, 8]], 23),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
