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
from typing import List
import heapq

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
                continue
            if heap[0] < n:
                heapq.heapreplace(heap, n)
        return heap[0]

# @lc code=end

if __name__ == "__main__":
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))
    print(Solution().findKthLargest([1,2,3], 2))
