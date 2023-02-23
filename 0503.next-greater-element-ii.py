#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (59.46%)
# Likes:    2805
# Dislikes: 97
# Total Accepted:    149.3K
# Total Submissions: 251K
# Testcase Example:  '[1,2,1]'
#
# Given a circular integer array nums (i.e., the next element of
# nums[nums.length - 1] is nums[0]), return the next greater number for every
# element in nums.
#
# The next greater number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, return -1 for this
# number.
#
#
# Example 1:
#
#
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number.
# The second 1's next greater number needs to search circularly, which is also
# 2.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
from typing import List


# @lc code=start
class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        n = len(nums)

        for i in range(n * 2):
            v = nums[i % n]
            while stack and nums[stack[-1]] < v:
                res[stack.pop()] = v
            stack.append(i % n)

        return res


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([1], [-1]),
        ([1, 2], [2, -1]),
        ([2, 1], [-1, 2]),
        ([1, 2, 3], [2, 3, -1]),
        ([1, 2, 1], [2, -1, 2]),
        ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),
    ]
    for nums, want in cases:
        got = sol.nextGreaterElements(nums)
        if want != got:
            print(f"Failed => args: {nums}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
