#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#
# https://leetcode.com/problems/count-of-range-sum/description/
#
# algorithms
# Hard (36.25%)
# Likes:    1255
# Dislikes: 137
# Total Accepted:    53.7K
# Total Submissions: 148.5K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# Given an integer array nums and two integers lower and upper, return the
# number of range sums that lie in [lower, upper] inclusive.
#
# Range sum S(i, j) is defined as the sum of the elements in nums between
# indices i and j inclusive, where i <= j.
#
#
# Example 1:
#
#
# Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their
# respective sums are: -2, -1, 2.
#
#
# Example 2:
#
#
# Input: nums = [0], lower = 0, upper = 0
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# -10^5 <= lower <= upper <= 10^5
# The answer is guaranteed to fit in a 32-bit integer.
#
#
#
import bisect
from collections import Counter
from typing import List

# @lc code=start
class Solution:
    # O(n+L*n), O(n). L = upper-lower+1. TLE
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        res = 0
        mem = Counter()
        for csum in presum:
            for target in range(lower, upper+1):
                res += mem[csum-target]
            mem[csum] += 1
        return res

    # TODO: WTF
    def countRangeSum1(self, nums: List[int], lower: int, upper: int) -> int:
        # for i < j
        # lower <= sum(nums[i:j]) <= upper
        # lower <= presum[j] - presum[i] <= upper
        # lower + presum[i] <= presum[j] <= upper + presum[i]
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        res = 0
        temp = []
        for csum in presum:
            left = bisect.bisect_left(temp, csum+lower)
            right = bisect.bisect_right(temp, csum+upper)
            res += right-left
            bisect.insort(temp, csum)
        return res

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[0], 0, 0], 1),
            ([[-2,5,-1], -2, 2], 3),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
