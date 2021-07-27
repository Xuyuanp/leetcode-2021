#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (35.69%)
# Likes:    7098
# Dislikes: 450
# Total Accepted:    682.7K
# Total Submissions: 1.9M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Determine if you are able to reach the last index.
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
#
#
#
from functools import lru_cache
from typing import List

# @lc code=start
class Solution:
    # O(n), O(1)
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= last:
                last = i
        return last == 0

    # O(n*max(nums)), O(n)
    # Time Limit Exceeded sometimes
    def canJump1(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(maxsize=None)
        def helper(start: int) -> bool:
            if n - start == 1 or nums[start] >= n - start:
                return True
            return any(helper(start+i) for i in range(nums[start], 0, -1))

        return helper(0)

# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([2,3,1,1,4], True),
        ([1], True),
        ([0], True),
        ([3,1,2], True),
        ([3,1,2,3], True),
        ([3, 2, 1, 0, 4], False),
    ]
    for nums, want in cases:
        got = sol.canJump(nums)
        if got != want:
            print(f"Failed => args: {nums}; want: {want}, but got: {got}")
            break
    else:
        print('All Passed')
