#
# @lc app=leetcode id=2009 lang=python3
#
# [2009] Minimum Number of Operations to Make Array Continuous
#
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/
#
# algorithms
# Hard (44.59%)
# Likes:    138
# Dislikes: 2
# Total Accepted:    2.7K
# Total Submissions: 6K
# Testcase Example:  '[4,2,5,3]'
#
# You are given an integer array nums. In one operation, you can replace any
# element in nums with any integer.
#
# nums is considered continuous if both of the following conditions are
# fulfilled:
#
#
# All elements in nums are unique.
# The difference between the maximum element and the minimum element in nums
# equals nums.length - 1.
#
#
# For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is
# not continuous.
#
# Return the minimum number of operations to make nums continuous.
#
#
# Example 1:
#
#
# Input: nums = [4,2,5,3]
# Output: 0
# Explanation: nums is already continuous.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,5,6]
# Output: 1
# Explanation: One possible solution is to change the last element to 4.
# The resulting array is [1,2,3,5,4], which is continuous.
#
#
# Example 3:
#
#
# Input: nums = [1,10,100,1000]
# Output: 3
# Explanation: One possible solution is to:
# - Change the second element to 2.
# - Change the third element to 3.
# - Change the fourth element to 4.
# The resulting array is [1,2,3,4], which is continuous.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
#
#
#
from typing import List


# @lc code=start
class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        m = len(nums)

        right = 1
        curr = 0
        for left in range(m):
            while right < m and nums[right] - nums[left] <= n - 1:
                right += 1
            curr = max(curr, right - left)

        return n - curr


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[8, 5, 9, 9, 8, 4]], 2),
            ([[4, 2, 5, 3]], 0),
            ([[1, 2, 3, 5, 6]], 1),
            ([[1, 10, 100, 1000]], 3),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
            print("--")
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
