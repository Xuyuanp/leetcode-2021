#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.48%)
# Likes:    8878
# Dislikes: 708
# Total Accepted:    1.1M
# Total Submissions: 2.9M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
#
# Prior to being passed to your function, nums is rotated at an unknown pivot
# index k (0 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
# example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
# [4,5,6,7,0,1,2].
#
# Given the array nums after the rotation and an integer target, return the
# index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
#
#
#
from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    def search1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        offset = low
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            real_mid = (mid + offset) % n
            if nums[real_mid] == target:
                return real_mid
            if nums[real_mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (([1], 0), -1),
            (([0, 1, 2, 3, 4, 5, 6], 0), 0),
            (([6, 0, 1, 2, 3, 4, 5], 0), 1),
            (([5, 6, 0, 1, 2, 3, 4], 0), 2),
            (([4, 5, 6, 0, 1, 2, 3], 0), 3),
            (([3, 4, 5, 6, 0, 1, 2], 0), 4),
            (([2, 3, 4, 5, 6, 0, 1], 0), 5),
            (([1, 2, 3, 4, 5, 6, 0], 0), 6),
            (([0, 1, 2, 3, 4, 5, 6], 2), 2),
            (([6, 0, 1, 2, 3, 4, 5], 2), 3),
            (([5, 6, 0, 1, 2, 3, 4], 2), 4),
            (([4, 5, 6, 0, 1, 2, 3], 2), 5),
            (([3, 4, 5, 6, 0, 1, 2], 2), 6),
            (([2, 3, 4, 5, 6, 0, 1], 2), 0),
            (([1, 2, 3, 4, 5, 6, 0], 2), 1),
            (([0, 1, 2, 3, 4, 5, 6], 3), 3),
            (([6, 0, 1, 2, 3, 4, 5], 3), 4),
            (([5, 6, 0, 1, 2, 3, 4], 3), 5),
            (([4, 5, 6, 0, 1, 2, 3], 3), 6),
            (([3, 4, 5, 6, 0, 1, 2], 3), 0),
            (([2, 3, 4, 5, 6, 0, 1], 3), 1),
            (([1, 2, 3, 4, 5, 6, 0], 3), 2),
            (([0, 1, 2, 3, 4, 5, 6], 4), 4),
            (([6, 0, 1, 2, 3, 4, 5], 4), 5),
            (([5, 6, 0, 1, 2, 3, 4], 4), 6),
            (([4, 5, 6, 0, 1, 2, 3], 4), 0),
            (([3, 4, 5, 6, 0, 1, 2], 4), 1),
            (([2, 3, 4, 5, 6, 0, 1], 4), 2),
            (([1, 2, 3, 4, 5, 6, 0], 4), 3),
            (([0, 1, 2, 3, 4, 5, 6], 6), 6),
            (([6, 0, 1, 2, 3, 4, 5], 6), 0),
            (([5, 6, 0, 1, 2, 3, 4], 6), 1),
            (([4, 5, 6, 0, 1, 2, 3], 6), 2),
            (([3, 4, 5, 6, 0, 1, 2], 6), 3),
            (([2, 3, 4, 5, 6, 0, 1], 6), 4),
            (([1, 2, 3, 4, 5, 6, 0], 6), 5),
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
