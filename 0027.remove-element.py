#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
# https://leetcode.com/problems/remove-element/description/
#
# algorithms
# Easy (49.89%)
# Likes:    2361
# Dislikes: 3794
# Total Accepted:    918.7K
# Total Submissions: 1.8M
# Testcase Example:  '[3,2,2,3]\n3'
#
# Given an integer array nums and an integer val, remove all occurrences of val
# in nums in-place. The relative order of the elements may be changed.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array
# nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result. It does not
# matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.
#
# Custom Judge:
#
# The judge will test your solution with the following code:
#
#
# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
# ⁠                           // It is sorted with no values equaling val.
#
# int k = removeElement(nums, val); // Calls your implementation
#
# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
# ⁠   assert nums[i] == expectedNums[i];
# }
#
#
# If all assertions pass, then your solution will be accepted.
#
#
# Example 1:
#
#
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements
# of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
#
#
# Example 2:
#
#
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements
# of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100
#
#
#
from typing import List

# @lc code=start
class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                cnt += 1
            else:
                nums[i], nums[i-cnt] = nums[i-cnt], nums[i]
        return len(nums) - cnt

    def removeElement(self, nums: List[int], val: int) -> int:
        total = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[total] = nums[i]
                total += 1
        return total

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
                (([1], 1), []),
                (([1, 1], 1), []),
                (([1, 2], 1), [2]),
                (([1, 2], 2), [1]),
                (([1, 2], 3), [1, 2]),
                (([1,2,3,2,4], 2), [1,3,4]),
                ]
        for args, want in cases:
            got = fn(*args)
            if want != args[0][:got]:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
