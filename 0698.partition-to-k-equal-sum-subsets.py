#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (45.04%)
# Likes:    3233
# Dislikes: 202
# Total Accepted:    134.3K
# Total Submissions: 298.3K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an integer array nums and an integer k, return true if it is possible
# to divide this array into k non-empty subsets whose sums are all equal.
#
#
# Example 1:
#
#
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4], k = 3
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 10^4
# The frequency of each element is in the range [1, 4].
#
#
#
from typing import List

# @lc code=start
class Solution:
    def canPartitionKSubsets1(self, nums: List[int],
                             k: int) -> bool:
        if k > len(nums):
            return False
        nums.sort(reverse=True)
        total = sum(nums)
        if total%k != 0:
            return False

        target = total//k
        bucket = [0]*k

        def backtrack(index: int) -> bool:
            if index == len(nums):
                return all(x == target for x in bucket)

            for i in range(0, k):
                if bucket[i] + nums[index] > target:
                    continue
                bucket[i] += nums[index]
                if backtrack(index+1):
                    return True
                bucket[i] -= nums[index]

            return False

        return backtrack(0)

    def canPartitionKSubsets(self, nums: List[int],
                              k: int) -> bool:
        if k > len(nums):
            return False
        total = sum(nums)
        if total%k != 0:
            return False
        used = [False]*len(nums)
        target = total//k

        def backtrack(kk: int, curr: int, start: int) -> bool:
            if kk == k-1:
                return True
            if curr == target:
                return backtrack(kk+1, 0, 0)

            for i in range(start, len(nums)):
                x = nums[i]
                if used[i] or curr + x > target:
                    continue
                used[i] = True
                if backtrack(kk, curr+x, i+1):
                    return True
                used[i] = False

            return False

        return backtrack(0, 0, 0)

# @lc code=end


if __name__ == '__main__':
    print(Solution().canPartitionKSubsets([815,625,3889,4471,60,494,944,1118,4623,497,771,679,1240,202,601,883], 3))
