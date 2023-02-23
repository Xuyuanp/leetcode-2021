#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (38.18%)
# Likes:    6516
# Dislikes: 219
# Total Accepted:    776.3K
# Total Submissions: 2M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
#
#
#
from typing import List


# @lc code=start
class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def search_left():
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left if nums[left] == target else -1

        def search_right():
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2 + 1
                if nums[mid] == target:
                    left = mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            return left if nums[left] == target else -1

        left_bound = search_left()
        if left_bound < 0:
            return [-1, -1]

        right_bound = search_right()
        return [left_bound, right_bound]


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[], 1], [-1, -1]),
            ([[1], 1], [0, 0]),
            ([[1, 1], 1], [0, 1]),
            ([[1, 1, 2, 3, 4], 1], [0, 1]),
            ([[1, 2, 3, 4, 4, 4], 4], [3, 5]),
            ([[5, 7, 7, 8, 8, 10], 8], [3, 4]),
            ([[5, 7, 7, 8, 8, 10], 9], [-1, -1]),
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
