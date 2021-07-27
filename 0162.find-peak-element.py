#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (44.30%)
# Likes:    3616
# Dislikes: 2902
# Total Accepted:    559.4K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is strictly greater than its neighbors.
#
# Given an integer array nums, find a peak element, and return its index. If
# the array contains multiple peaks, return the index to any of the peaks.
#
# You may imagine that nums[-1] = nums[n] = -∞. <-- IMPORTANT!!!
#
# You must write an algorithm that runs in O(log n) time.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
#
# Example 2:
#
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i. <-- IMPORTANT!!!
#
#
#
from typing import List

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1

        return left

# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    cases = [
        ([1,2,3,1], {2}),
        ([1,2,1,3,5,6,7], {5, 6}),
        ([1,2,3], {2}),
        ([3,2,1], {0}),
        ([1,3,2], {1}),
        ([1,2,3,-1,4,-2], {2, 4}),
    ]
    for nums, wants in cases:
        got = sol.findPeakElement(nums)
        if got not in wants:
            print(f'Failed => args: {nums}; wants: {wants}, but got: {got}')
            break
    else:
        print('All Passed')
