#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (32.05%)
# Likes:    11500
# Dislikes: 1618
# Total Accepted:    1M
# Total Submissions: 3.2M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
# Example 3:
#
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#
#
# Example 4:
#
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#
#
# Example 5:
#
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#
from typing import List

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        mid = (m + n + 1) // 2
        left, right = 0, m
        while left < right:
            mid1 = left + (right - left) // 2
            mid2 = mid - mid1
            if nums1[mid1] < nums2[mid2 - 1]:
                left = mid1 + 1
            else:
                right = mid1
        mid1 = left
        mid2 = mid - mid1
        c1 = max(
            float("-inf") if mid1 < 1 else nums1[mid1 - 1],
            float("-inf") if mid2 < 1 else nums2[mid2 - 1],
        )
        if (m + n) % 2 == 1:
            return c1
        c2 = min(
            float("inf") if mid1 >= m else nums1[mid1],
            float("inf") if mid2 >= n else nums2[mid2],
        )
        return (c1 + c2) / 2


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[], [2]], 2),
            ([[1], [1]], 1),
            ([[1, 2], [3, 4]], 2.5),
            ([[3, 4], [1, 2]], 2.5),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()
