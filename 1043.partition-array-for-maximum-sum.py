#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#
# https://leetcode.com/problems/partition-array-for-maximum-sum/description/
#
# algorithms
# Medium (68.28%)
# Likes:    1582
# Dislikes: 167
# Total Accepted:    37.9K
# Total Submissions: 55K
# Testcase Example:  '[1,15,7,9,2,5,10]\n3'
#
# Given an integer array arr, partition the array into (contiguous) subarrays
# of length at most k. After partitioning, each subarray has their values
# changed to become the maximum value of that subarray.
#
# Return the largest sum of the given array after partitioning. Test cases are
# generated so that the answer fits in a 32-bit integer.
#
#
# Example 1:
#
#
# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: arr becomes [15,15,15,9,10,10,10]
#
#
# Example 2:
#
#
# Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# Output: 83
#
#
# Example 3:
#
#
# Input: arr = [1], k = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 500
# 0 <= arr[i] <= 10^9
# 1 <= k <= arr.length
#
#
#
from functools import cache
from typing import List

# @lc code=start
class Solution:
    # O(n*k), O(n)
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        @cache
        def helper(start: int) -> int:
            if n - start < k:
                return (n - start) * max(arr[start:], default=0)

            curr_max = 0
            res = 0
            for i in range(1, k + 1):
                curr_max = max(curr_max, arr[start + i - 1])
                res = max(res, curr_max * i + helper(start + i))

            return res

        return helper(0)

    # O(n*k), O(n)
    def maxSumAfterPartitioning1(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        curr_max = -1
        for i in range(1, k + 1):
            curr_max = max(curr_max, arr[i - 1])
            dp[i] = curr_max * i

        for i in range(k + 1, n + 1):
            curr_max = -1
            for j in range(1, k + 1):
                curr_max = max(curr_max, arr[i - j])
                dp[i] = max(dp[i], curr_max * j + dp[i - j])

        return dp[n]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1], 1], 1),
            ([[1, 15, 7, 9, 2, 5, 10], 3], 84),
            ([[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4], 83),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
