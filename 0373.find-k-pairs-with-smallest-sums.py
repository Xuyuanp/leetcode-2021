#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (38.80%)
# Likes:    2355
# Dislikes: 147
# Total Accepted:    143.4K
# Total Submissions: 368.3K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# You are given two integer arrays nums1 and nums2 sorted in ascending order
# and an integer k.
#
# Define a pair (u, v) which consists of one element from the first array and
# one element from the second array.
#
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest
# sums.
#
#
# Example 1:
#
#
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#
#
# Example 2:
#
#
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#
#
# Example 3:
#
#
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [[1,3],[2,3]]
# Explanation: All possible pairs are returned from the sequence:
# [1,3],[2,3]
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 10^5
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1 and nums2 both are sorted in ascending order.
# 1 <= k <= 1000
#
#
#
from collections import deque
import heapq
from typing import List

# @lc code=start
class Solution:
    # O(m*n*log(m*n)). TLE
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        for _, x, y in sorted((x+y, x, y) for x in nums1 for y in nums2):
            res.append([x, y])
            k -= 1
            if k == 0:
                break
        return res

    # O(m*n*log(k)). TLE
    def kSmallestPairs1(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for x in nums1:
            for y in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-x-y, x, y))
                else:
                    if x+y < -heap[0][0]:
                        heapq.heapreplace(heap, (-x-y, x, y))
        res = deque()
        while heap and k > 0:
            _, x, y = heapq.heappop(heap)
            res.appendleft([x, y])
            k -= 1

        return list(res)

    # O(k*log(k)), O(k)
    def kSmallestPairs2(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        m, n = len(nums1), len(nums2)

        # m*n matrix, searching from topleft corner(BFS)

        visited = set()

        heap = [(nums1[0]+nums2[0], 0, 0)]
        # k loops at most
        # in each loop, pop 1 and push 2, so heap size is k at most
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i+1 < m and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
                visited.add((i+1, j))
            if j+1 < n and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i, j+1))

        return res

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[1,1,2],[1,2,3], 2], [[1,1],[1,1]]),
            ([[1,1,2],[1,2,3], 4], [[1,1],[1,1],[1,2],[1,2]]),
            ([[1,2],[3], 3], [[1,3],[2,3]]),
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
