#
# @lc app=leetcode id=1262 lang=python3
#
# [1262] Greatest Sum Divisible by Three
#
# https://leetcode.com/problems/greatest-sum-divisible-by-three/description/
#
# algorithms
# Medium (50.28%)
# Likes:    890
# Dislikes: 27
# Total Accepted:    31.6K
# Total Submissions: 62.7K
# Testcase Example:  '[3,6,5,1,8]'
#
# Given an array nums of integers, we need to find the maximum possible sum of
# elements of the array such that it is divisible by three.
#
#
#
#
#
# Example 1:
#
#
# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum
# divisible by 3).
#
# Example 2:
#
#
# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum
# divisible by 3).
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0] * 3
        for x in nums:
            for curr in dp[:]:
                dp[(curr + x) % 3] = max(dp[(curr + x) % 3], curr + x)
        return dp[0]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[4]], 0),
            ([[9]], 9),
            ([[1, 2, 3, 4, 4]], 12),
            ([[3, 6, 5, 1, 8]], 18),
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
