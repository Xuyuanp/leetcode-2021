#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (40.48%)
# Likes:    4334
# Dislikes: 149
# Total Accepted:    386.7K
# Total Submissions: 949.5K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray [numsl, numsl+1, ...,
# numsr-1, numsr] of which the sum is greater than or equal to target. If there
# is no such subarray, return 0 instead.
#
#
# Example 1:
#
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem
# constraint.
#
#
# Example 2:
#
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
#
# Example 3:
#
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution of which the time complexity is O(n log(n)).
#
from typing import List

# @lc code=start
class Solution:
    # O(n), O(1). sliding window
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left = sum_ = 0
        for right, n in enumerate(nums):
            sum_ += n
            # when we got a subarray sum >= target, shrink the left bound
            while sum_ >= target:
                res = min(res, right-left+1)
                sum_ -= nums[left]
                left += 1

        return res if res != float('inf') else 0

    # O(n*log(n)), O(1)
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        def possible(length: int) -> bool:
            sum_ = sum(nums[:length])
            if sum_ >= target:
                return True
            for i in range(length, len(nums)):
                sum_ += nums[i] - nums[i-length]
                if sum_ >= target:
                    return True
            return False

        left, right = 1, len(nums)
        while left < right:
            mid = (left+right)//2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        return left if possible(left) else 0

# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([4, [1,4,4]], 1),
            ([7, [2,3,1,2,4,3]], 2),
            ([11, [1,1,1,1,1,1,1,1]], 0),
            ([15, [1,2,3,4,5]], 5),
            ([213, [12,28,83,4,25,26,25,2,25,25,25,12]], 8),
            ([1, [9,8,7,6,5,4,3,2,1]], 1),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()
