#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (42.25%)
# Likes:    1770
# Dislikes: 286
# Total Accepted:    259.3K
# Total Submissions: 613.1K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,4,4,5,6,7] might
# become:
#
#
# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
#
#
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums that may contain duplicates, return the
# minimum element of this array.
#
# You must decrease the overall operation steps as much as possible.
#
#
# Example 1:
# Input: nums = [1,3,5]
# Output: 1
# Example 2:
# Input: nums = [2,2,2,0,1]
# Output: 0
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.
#
#
#
# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array,
# but nums may contain duplicates. Would this affect the runtime complexity?
# How and why?
#
#
#
#
from typing import List


# @lc code=start
class Solution:

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                right -= 1
            else:
                right = mid

        return nums[left]


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[1, 1]], 1),
            ([[1, 1, 2]], 1),
            ([[2, 1, 1]], 1),
            ([[2, 1, 2]], 1),
            ([[2, 1, 2, 2, 2, 2]], 1),
            ([[2, 2, 2, 0, 1]], 0),
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
