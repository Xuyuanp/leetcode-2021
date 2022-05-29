#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (45.45%)
# Likes:    8369
# Dislikes: 181
# Total Accepted:    620.2K
# Total Submissions: 1.3M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting
# some or no elements without changing the order of the remaining elements. For
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#
#
# Example 1:
#
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
#
# Example 3:
#
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
#
#
from typing import List

# @lc code=start
from bisect import bisect_left


class Solution:
    # O(n^2), O(n)
    def lengthOfLIS2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

    # O(n*log(n)), O(n)
    def lengthOfLIS1(self, nums: List[int]) -> int:
        lis = []

        def binary_search(x: int) -> int:
            left, right = 0, len(lis)
            while left < right:
                mid = (left + right) // 2
                if lis[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left

        for x in nums:
            pos = binary_search(x)
            if pos == len(lis):
                lis.append(x)
            else:
                lis[pos] = x
        return len(lis)

    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for x in nums:
            pos = bisect_left(lis, x)
            if pos == len(lis):
                lis.append(x)
            else:
                lis[pos] = x
        return len(lis)


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[10, 9, 2, 5, 3, 7, 101, 18]], 4),
            ([[0, 1, 0, 3, 2, 3]], 4),
            ([[7, 7, 7, 7, 7, 7]], 1),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    main()
