#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
#
# algorithms
# Hard (32.91%)
# Likes:    1522
# Dislikes: 53
# Total Accepted:    47.1K
# Total Submissions: 142.3K
# Testcase Example:  '[1,3,1]\n1'
#
# The distance of a pair of integers a and b is defined as the absolute
# difference between a and b.
#
# Given an integer array nums and an integer k, return the k^th smallest
# distance among all the pairs nums[i] and nums[j] where 0 <= i < j <
# nums.length.
#
#
# Example 1:
#
#
# Input: nums = [1,3,1], k = 1
# Output: 0
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1^st smallest distance pair is (1,1), and its distance is 0.
#
#
# Example 2:
#
#
# Input: nums = [1,1,1], k = 2
# Output: 0
#
#
# Example 3:
#
#
# Input: nums = [1,6,1], k = 3
# Output: 5
#
#
#
# Constraints:
#
#
# n == nums.length
# 2 <= n <= 10^4
# 0 <= nums[i] <= 10^6
# 1 <= k <= n * (n - 1) / 2
#
#
#
import heapq
from typing import List


# @lc code=start
class Solution:
    # O(n*log(n)+n*log(max(nums)-min(nums))), O(1)
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def possible(dist) -> bool:
            i = count = 0
            j = 1
            for i in range(n):
                while j < n and nums[j] - nums[i] <= dist:
                    j += 1
                count += j - i - 1

            return count >= k

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        return left

    # O(n^2*log(k)), O(k), TLE
    def smallestDistancePair1(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def gen_dists():
            for i in range(n - 1):
                for j in range(i + 1, n):
                    yield -abs(nums[i] - nums[j])

        dists = gen_dists()
        heap = []
        for _ in range(k):
            heapq.heappush(heap, next(dists))

        for dist in dists:
            if dist > heap[0]:
                heapq.heapreplace(heap, dist)

        return -heap[0]


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [([[1, 3, 1], 1], 0), ([[1, 1, 1], 2], 0), ([[1, 6, 1], 3], 5)]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()
