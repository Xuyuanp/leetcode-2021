#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (59.91%)
# Likes:    6196
# Dislikes: 382
# Total Accepted:    953.5K
# Total Submissions: 1.6M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
#
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
#
#
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
#
#
#
import heapq
from typing import List


# @lc code=start
class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [float("inf")] * k
        for n in nums[:k]:
            heapq.heappush(heap, n)
        for n in nums[k:]:
            if heap[0] < n:
                heapq.heapreplace(heap, n)
        return heap[0]

    def findKthLargest1(self, nums: List[int], k: int) -> int:

        def partition(start: int, end: int) -> int:
            pivot = nums[(start + end) // 2]
            i, j = start - 1, end + 1
            while True:
                i += 1
                j -= 1
                while nums[i] > pivot:
                    i += 1
                while nums[j] < pivot:
                    j -= 1

                if i >= j:
                    return j

                nums[i], nums[j] = nums[j], nums[i]

        def quick_sort(start: int, end: int):
            if end - start < 1:
                return

            p = partition(start, end)
            quick_sort(start, p)
            if p < k - 1:
                quick_sort(p + 1, end)

        quick_sort(0, len(nums) - 1)
        return nums[k - 1]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
            (([3, 2, 1, 5, 6, 4], 2), 5),
            (([1, 2, 3], 2), 2),
            (([1, 2, 3], 3), 1),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
