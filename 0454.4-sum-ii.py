#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
# https://leetcode.com/problems/4sum-ii/description/
#
# algorithms
# Medium (54.99%)
# Likes:    2194
# Dislikes: 85
# Total Accepted:    175.5K
# Total Submissions: 318.6K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
# return the number of tuples (i, j, k, l) such that:
#
#
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
#
#
#
# Example 1:
#
#
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) +
# (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) +
# (-1) + 0 = 0
#
#
# Example 2:
#
#
# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1
#
#
#
# Constraints:
#
#
# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
#
#
#
from collections import defaultdict
from typing import List

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dp = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                dp[n1+n2] += 1
        total = 0
        for n3 in nums3:
            for n4 in nums4:
                if -n3-n4 in dp:
                    total += dp[-n3-n4]
        return total


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        (([1,2], [-2,-1], [-1,2], [0,2]), 2)
        (([1,2], [-2,-1], [-1,2], [0,2]), 2)
    ]
    for (nums1, nums2, nums3, nums4), want in cases:
        got = sol.fourSumCount(nums1, nums2, nums3, nums4)
        if got != want:
            print(f'Failed: args: {nums1}, {nums2}, {nums3}, {nums4}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
