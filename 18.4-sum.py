#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (35.75%)
# Likes:    3980
# Dislikes: 475
# Total Accepted:    458.2K
# Total Submissions: 1.3M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
#
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#
# Example 2:
#
#
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
#
#
#
from typing import List

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def two_sum(nums: List[int], target: int):
            lo, hi = 0, len(nums)-1
            while lo < hi:
                sum_ = nums[lo] + nums[hi]
                if sum_ < target or (lo > 0 and nums[lo] == nums[lo-1]):
                    lo += 1
                elif sum_ > target or (hi < len(nums)-1 and nums[hi] == nums[hi+1]):
                    hi -= 1
                else:
                    yield [nums[lo], nums[hi]]
                    lo += 1
                    hi -= 1

        def k_sum(nums: List[int], target: int, k: int):
            if not nums or len(nums) < k or nums[0] * k > target or nums[-1] * k < target:
                return
            if k == 2:
                yield from two_sum(nums, target)
                return
            for i, n in enumerate(nums[:1-k]):
                if i > 0 and n == nums[i-1]:
                    continue
                for vals in k_sum(nums[i+1:], target-n, k-1):
                    yield [n] + vals

        nums.sort()
        return list(k_sum(nums, target, 4))

# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
    (([-2,-1,-1,1,1,2,2], 0), [[-2, -1, 1, 2], [-1, -1, 1, 1]]),
    (([1,0,-1,0,-2,2], 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
    (([2,2,2,2,2], 8), [[2,2,2,2]]),
    (([0,0,0,0], 0), [[0,0,0,0]]),
    ]
    for (nums, target), want in cases:
        got = sol.fourSum(nums, target)
        if got != want:
            print(f'Failed => args: {nums}, {target}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
