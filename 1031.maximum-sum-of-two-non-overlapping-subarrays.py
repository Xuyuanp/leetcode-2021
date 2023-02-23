#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
#
# algorithms
# Medium (59.04%)
# Likes:    1218
# Dislikes: 57
# Total Accepted:    40.3K
# Total Submissions: 68.2K
# Testcase Example:  '[0,6,5,2,2,5,1,9,4]\n1\n2'
#
# Given an integer array nums and two integers firstLen and secondLen, return
# the maximum sum of elements in two non-overlapping subarrays with lengths
# firstLen and secondLen.
#
# The array with length firstLen could occur before or after the array with
# length secondLen, but they have to be non-overlapping.
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
#
#
# Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with
# length 2.
#
#
# Example 2:
#
#
# Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with
# length 2.
#
#
# Example 3:
#
#
# Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8]
# with length 3.
#
#
#
# Constraints:
#
#
# 1 <= firstLen, secondLen <= 1000
# 2 <= firstLen + secondLen <= 1000
# firstLen + secondLen <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
#
#
from typing import List


# @lc code=start
class Solution:
    # O(n), O(n)
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int,
                           secondLen: int) -> int:
        n = len(nums)
        MAX_LEFT_FST, MAX_RIGHT_FST, MAX_LEFT_SND, MAX_RIGHT_SND = 0, 1, 2, 3
        # dp[i] saved the MAX_[LEFT|RIGHT]_[FST|SND] at [0, i) and [i, n)
        dp = [[0, 0, 0, 0] for _ in range(n)]
        for i in range(1, n):
            nums[i] += nums[i - 1]

        dp[firstLen][MAX_LEFT_FST] = nums[firstLen - 1]
        dp[secondLen][MAX_LEFT_SND] = nums[secondLen - 1]
        for i in range(1, n):
            if i > firstLen:
                dp[i][MAX_LEFT_FST] = max(dp[i - 1][MAX_LEFT_FST],
                                          nums[i - 1] - nums[i - firstLen - 1])
            if i > secondLen:
                dp[i][MAX_LEFT_SND] = max(
                    dp[i - 1][MAX_LEFT_SND],
                    nums[i - 1] - nums[i - secondLen - 1])

        dp[n - firstLen][MAX_RIGHT_FST] = nums[-1] - nums[n - firstLen - 1]
        dp[n - secondLen][MAX_RIGHT_SND] = nums[-1] - nums[n - secondLen - 1]
        for i in range(n - 1, 0, -1):
            if n - i > firstLen:
                dp[i][MAX_RIGHT_FST] = max(
                    dp[i + 1][MAX_RIGHT_FST],
                    nums[i + firstLen - 1] - nums[i - 1])
            if n - i > secondLen:
                dp[i][MAX_RIGHT_SND] = max(
                    dp[i + 1][MAX_RIGHT_SND],
                    nums[i + secondLen - 1] - nums[i - 1])

        return max(
            max(
                dp[i][MAX_LEFT_FST] + dp[i][MAX_RIGHT_SND],
                dp[i][MAX_LEFT_SND] + dp[i][MAX_RIGHT_FST],
            ) for i in range(n))


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1, 1], 1, 1], 2),
            ([[1, 2, 3], 1, 1], 5),
            ([[0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2], 20),
            ([[3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2], 29),
            ([[2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3], 31),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    main()
