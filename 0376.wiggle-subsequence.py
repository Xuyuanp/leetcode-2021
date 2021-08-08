#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#
# https://leetcode.com/problems/wiggle-subsequence/description/
#
# algorithms
# Medium (42.65%)
# Likes:    1966
# Dislikes: 82
# Total Accepted:    110.8K
# Total Submissions: 258.5K
# Testcase Example:  '[1,7,4,9,2,5]'
#
# A wiggle sequence is a sequence where the differences between successive
# numbers strictly alternate between positive and negative. The first
# difference (if one exists) may be either positive or negative. A sequence
# with one element and a sequence with two non-equal elements are trivially
# wiggle sequences.
#
#
# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences
# (6, -3, 5, -7, 3) alternate between positive and negative.
# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences.
# The first is not because its first two differences are positive, and the
# second is not because its last difference is zero.
#
#
# A subsequence is obtained by deleting some elements (possibly zero) from the
# original sequence, leaving the remaining elements in their original order.
#
# Given an integer array nums, return the length of the longest wiggle
# subsequence of nums.
#
#
# Example 1:
#
#
# Input: nums = [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence with differences (6,
# -3, 5, -7, 3).
#
#
# Example 2:
#
#
# Input: nums = [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length.
# One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,4,5,6,7,8,9]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
#
#
# Follow up: Could you solve this in O(n) time?
#
#
from typing import List

# @lc code=start
class Solution:
    # O(n), O(1)
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res = 1
        pre = 0
        for x, y in zip(nums, nums[1:]):
            if x == y:
                continue
            curr = y - x
            if curr * pre <= 0:
                res += 1
                pre = curr

        return res

# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[1,7,4,9,2,5]], 6),
            ([[1,2,3,4,5,6,7,8,9]], 2),
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
    main()
