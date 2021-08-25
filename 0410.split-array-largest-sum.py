#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (47.35%)
# Likes:    3043
# Dislikes: 98
# Total Accepted:    132.6K
# Total Submissions: 278.4K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array nums which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
#
# Write an algorithm to minimize the largest sum among these m subarrays.
#
#
# Example 1:
#
#
# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
#
#
# Example 3:
#
#
# Input: nums = [1,4,4], m = 3
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 10^6
# 1 <= m <= min(50, nums.length)
#
#
#
from functools import cache
from typing import List

# @lc code=start
class Solution:
    # O(n*log(sum)), O(1)
    def splitArray(self, nums: List[int], m: int) -> int:
        def num_of_subarrays_sum_lt_val(val: int) -> int:
            cnt = 1
            total = 0
            for num in nums:
                if total + num > val:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right-left)//2
            if num_of_subarrays_sum_lt_val(mid) <= m:
                right = mid
            else:
                left = mid + 1
        return left

    # O(n*n*m), O(n*m)
    def splitArray1(self, nums: List[int], m: int) -> int:
        n = len(nums)

        @cache
        def helper(start: int, mm: int) -> int:
            if mm == 1:
                return sum(nums[start:])

            curr_sum = 0
            res = float('inf')

            for i in range(start, n-mm+1):
                curr_sum += nums[i]
                res = min(res, max(curr_sum, helper(i+1, mm-1)))

            return res

        return helper(0, m)

    # O(n*n*m), O(n*m)
    def splitArray1(self, nums: List[int], m: int) -> int:
        n = len(nums)

        @cache
        def helper(end: int, mm: int) -> int:
            if mm == 1:
                return sum(nums[:end])

            curr = 0
            res = float('inf')

            for i in range(end, mm-1, -1):
                curr+= nums[i-1]
                res = min(res, max(curr, helper(i-1, mm-1)))

            return res

        return helper(n, m)

    # O(n*n*m), O(n*m)
    def splitArray1(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[float('inf')]*(m+1) for _ in range(n+1)]
        dp[0][1] = 0

        for i in range(1, n+1):
            dp[i][1] = nums[i-1] + dp[i-1][1]
            for mm in range(2, min(i, m)+1):
                curr = 0
                for j in range(i, mm-1, -1):
                    curr += nums[j-1]
                    dp[i][mm] = min(dp[i][mm], max(curr, dp[j-1][mm-1]))

        return dp[n][m]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[7,2,5,10,8], 2], 18),
            ([[1,2,3,4,5], 2], 9),
            ([[1,4,4], 3], 4),
        ]
        for args, want in cases:
            got = func(*args)
            assert want == got, f'Failed => args: {args}; want: {want}, but got: {got}'
        print('  All Passed')
        print()


if __name__ == '__main__':
    test()
