#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (46.51%)
# Likes:    1329
# Dislikes: 150
# Total Accepted:    160.6K
# Total Submissions: 342.5K
# Testcase Example:  '[1,3,5,4,7]'
#
# Given an unsorted array of integers nums, return the length of the longest
# continuous increasing subsequence (i.e. subarray). The subsequence must be
# strictly increasing.
#
# A continuous increasing subsequence is defined by two indices l and r (l < r)
# such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for
# each l <= i < r, nums[i] < nums[i + 1].
#
#
# Example 1:
#
#
# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5] with
# length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as
# elements 5 and 7 are separated by element
# 4.
#
#
# Example 2:
#
#
# Input: nums = [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2] with length
# 1. Note that it must be strictly
# increasing.
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
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = curr = 1
        for x, y in zip(nums, nums[1:]):
            if y > x:
                curr += 1
                res = max(res, curr)
            else:
                curr = 1
        return res

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([[1,3,5,4,7]], 3),
            ([[2,2,2,2,2]], 1)
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
