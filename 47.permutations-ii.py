#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (50.68%)
# Likes:    3257
# Dislikes: 81
# Total Accepted:    473.7K
# Total Submissions: 934.6K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
#
#
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
#
#
# Example 2:
#
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
#
#

from typing import List
from collections import Counter

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = Counter(nums)

        def backtrack(pat: List[int]):
            if len(pat) == len(nums):
                res.append(list(pat))
                return

            for n in counter:
                if counter[n] > 0:
                    pat.append(n)
                    counter[n] -= 1
                    backtrack(pat)
                    counter[n] += 1
                    pat.pop()

        backtrack([])

        return res

# @lc code=end

