#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (68.17%)
# Likes:    6615
# Dislikes: 139
# Total Accepted:    852.9K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
#
#
#

from typing import List

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def backtrack(pat: List[int]):
            if len(pat) == len(nums):
                res.append(pat.copy())
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                x = nums[i]

                pat.append(x)
                used.add(i)
                backtrack(pat)
                pat.pop(-1)
                used.remove(i)

        backtrack([])

        return res

# @lc code=end

if __name__ == "__main__":
    print(Solution().permute([1,2]))
