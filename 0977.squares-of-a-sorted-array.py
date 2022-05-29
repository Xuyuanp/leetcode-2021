#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (71.55%)
# Likes:    2898
# Dislikes: 119
# Total Accepted:    562.7K
# Total Submissions: 788K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.
#
#
# Example 1:
#
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
#
# Example 2:
#
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.
#
#
#
# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach?
#
from typing import List

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        left, right = 0, n - 1
        index = n - 1
        while left <= right:
            if abs(nums[left]) > nums[right]:
                res[index] = nums[left] ** 2
                left += 1
            else:
                res[index] = nums[right] ** 2
                right -= 1
            index -= 1

        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1, 2, 3]], [1, 4, 9]),
            ([[-3, -2, -1]], [1, 4, 9]),
            ([[-4, -1, 0, 3, 10]], [0, 1, 9, 16, 100]),
            ([[-7, -3, 2, 3, 11]], [4, 9, 9, 49, 121]),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
