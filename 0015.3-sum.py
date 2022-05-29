#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (28.82%)
# Likes:    11666
# Dislikes: 1153
# Total Accepted:    1.4M
# Total Submissions: 4.8M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
#
#
# Constraints:
#
#
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(n*n), O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for i, x in enumerate(nums[:-2]):
            if x > 0:
                break
            if i > 0 and x == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                y, z = nums[j], nums[k]
                val = x + y + z
                if val == 0:
                    res.append([x, y, z])
                    while k > j and nums[k] == z:
                        k -= 1
                    while j < k and nums[j] == y:
                        j += 1
                elif val < 0:
                    j += 1
                else:
                    k -= 1

        return res


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([], []),
        ([0], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([1, -1, -1, 0], [[-1, 0, 1]]),
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ]
    for nums, want in cases:
        got = sol.threeSum(nums)
        if want != got:
            print(f"Failed => args: {nums}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
