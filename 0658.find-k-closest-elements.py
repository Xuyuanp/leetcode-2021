#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (43.38%)
# Likes:    2964
# Dislikes: 351
# Total Accepted:    202.7K
# Total Submissions: 468.2K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# Given a sorted integer array arr, two integers k and x, return the k closest
# integers to x in the array. The result should also be sorted in ascending
# order.
#
# An integer a is closer to x than an integer b if:
#
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
#
#
#
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
#
#
# Constraints:
#
#
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# arr is sorted in ascending order.
# -10^4 <= arr[i], x <= 10^4
#
#
#
from typing import List

# @lc code=start
class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        if x <= nums[0]:
            return nums[:k]
        if x >= nums[-1]:
            return nums[-k:]

        left, right = 0, len(nums)-k
        # left ... mid ... mid+k ... right
        while left < right:
            mid = left + (right-left)//2
            if x - nums[mid] > nums[mid+k] - x:
                left = mid + 1
            else:
                right = mid

        return nums[left:left+k]

# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([[1], 1, 1], [1]),
            ([[1], 1, -1], [1]),
            ([[1, 2, 3, 4, 5], 4, 3], [1,2,3,4]),
            ([[1, 2, 3, 4, 5], 4, -1], [1,2,3,4]),
            ([[1, 2, 30, 31, 32], 3, 30], [30, 31, 32]),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()
