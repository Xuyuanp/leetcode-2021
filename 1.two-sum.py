#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (47.21%)
# Likes:    22467
# Dislikes: 761
# Total Accepted:    4.5M
# Total Submissions: 9.6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#
from typing import List

# @lc code=start
class Solution:
    # O(n), O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if n in seen:
                return [seen[n], i]
            seen[target-n] = i
        return []

# @lc code=end


if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], target = 9))
    print(Solution().twoSum([3,2,4], target = 6))
    print(Solution().twoSum([3,3], target = 6))
