#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (33.31%)
# Likes:    5086
# Dislikes: 203
# Total Accepted:    397.9K
# Total Submissions: 1.2M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
#
#
#
from typing import List

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = n = 0
        while r < len(nums) -1:
            n += 1
            nxt = max(i + nums[i] for i in range(l, r+1))
            l, r = r+1, nxt

        return n

# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([1], 0),
        ([1, 2], 1),
        ([2, 2, 2], 1),
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2)
    ]
    for nums, want in cases:
        got = sol.jump(nums)
        if got != want:
            print(f"Failed => args: {nums}; want: {want}; but got: {got}")
            break
    else:
        print("All Passed")
