#
# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#
# https://leetcode.com/problems/largest-sum-of-averages/description/
#
# algorithms
# Medium (51.60%)
# Likes:    1345
# Dislikes: 66
# Total Accepted:    35.1K
# Total Submissions: 67.8K
# Testcase Example:  '[9,1,2,3,9]\n3'
#
# You are given an integer array nums and an integer k. You can partition the
# array into at most k non-empty adjacent subarrays. The score of a partition
# is the sum of the averages of each subarray.
#
# Note that the partition must use every integer in nums, and that the score is
# not necessarily an integer.
#
# Return the maximum score you can achieve of all the possible partitions.
# Answers within 10^-6 of the actual answer will be accepted.
#
#
# Example 1:
#
#
# Input: nums = [9,1,2,3,9], k = 3
# Output: 20.00000
# Explanation:
# The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is
# 9 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4,5,6,7], k = 4
# Output: 20.50000
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#
from functools import cache
import math
from typing import List

# @lc code=start
class Solution:
    # O(n*k), O(n*k)
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)

        @cache
        def helper(start: int, kk: int) -> float:
            if kk == 1:
                return sum(nums[start:])/(n-start)
            total = 0
            res = 0
            for i in range(start, n-kk+1):
                total += nums[i]
                res = max(res, total/(i-start+1) + helper(i+1, kk-1))
            return res

        return helper(0, k)

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[9,1,2,3,9], 3], 20),
            ([[1,2,3,4,5,6,7], 4], 20.5),
            ([[4,1,7,5,6,2,3], 4], 18.1667),
        ]
        for args, want in cases:
            got = func(*args)
            if not math.isclose(want, got, rel_tol=1e-3):
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
