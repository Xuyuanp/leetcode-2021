#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (50.83%)
# Likes:    6569
# Dislikes: 338
# Total Accepted:    757K
# Total Submissions: 1.5M
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array nums with n objects colored red, white, or blue, sort them
# in-place so that objects of the same color are adjacent, with the colors in
# the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and
# blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
#
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Example 3:
# Input: nums = [0]
# Output: [0]
# Example 4:
# Input: nums = [1]
# Output: [1]
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 300
# nums[i] is 0, 1, or 2.
#
#
#
# Follow up: Could you come up with a one-pass algorithm using only constant
# extra space?
#
#
from typing import List

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums)-1
        i = 0
        while left <= i <= right:
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                i = min(i, right)
            elif nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i = max(i, left)
            else:
                i += 1

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[0]], [0]),
            ([[1]], [1]),
            ([[2]], [2]),
            ([[0,0]], [0,0]),
            ([[1,1]], [1,1]),
            ([[2,2]], [2,2]),
            ([[2,0,1]], [0,1,2]),
            ([[2,0,2,1,1,0]], [0,0,1,1,2,2])
        ]
        for args, want in cases:
            func(*args)
            got = args[0]
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
