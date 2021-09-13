#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (63.75%)
# Likes:    1272
# Dislikes: 436
# Total Accepted:    185.2K
# Total Submissions: 292.8K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order.
#
#
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
#
#
#
from datetime import datetime
import random
from typing import List

# @lc code=start
class Solution:
    def sortArrayBubble(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for j in range(n-1, 0, -1):
            for i in range(j):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums

    def sortArraySelect(self, nums: List[int]) -> List[int]:
        n = len(nums)
        curr_min = 0
        for i in range(n):
            curr_min = i
            for j in range(i+1, n):
                if nums[j] < nums[curr_min]:
                    curr_min = j
            nums[i], nums[curr_min] = nums[curr_min], nums[i]

        return nums

    def sortArrayInsert(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for j in range(1, n):
            tmp = nums[j]
            i = j - 1
            while i >= 0 and nums[i] > tmp:
                nums[i+1] = nums[i]
                i -= 1
            nums[i+1] = tmp
        return nums

    def sortArrayMerge(self, nums: List[int]) -> List[int]:
        def merge(left: List[int], right: List[int]) -> List[int]:
            i = j = k = 0
            m, n = len(left), len(right)
            res = [0]*(m+n)
            while i < m and j < n:
                if left[i] <= right[j]:
                    res[k] = left[i]
                    i += 1
                else:
                    res[k] = right[j]
                    j += 1
                k += 1

            while i < m:
                res[k] = left[i]
                i += 1
                k += 1
            while j < n:
                res[k] = right[j]
                j += 1
                k += 1
            return res

        def merge_sort(nums: List[int]) -> List[int]:
            if len(nums) < 2:
                return nums
            mid = len(nums)//2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            return merge(left, right)

        return merge_sort(nums)

    def sortArrayQuick(self, nums: List[int]) -> List[int]:

        def partition(start: int, end: int) -> int:
            pivot = nums[(start+end)//2]
            i, j = start-1, end+1
            while True:
                i += 1
                j -= 1
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1

                if i >= j:
                    return j

                nums[i], nums[j] = nums[j], nums[i]

        def quick_sort(start: int, end: int):
            if end - start < 1:
                return

            p = partition(start, end)
            quick_sort(start, p)
            quick_sort(p+1, end)

        quick_sort(0, len(nums)-1)

        return nums

    def sortArrayHeap(self, nums: List[int]) -> List[int]:
        def sift_down(start: int, end: int):
            root = start
            while True:
                child1 = 2*root + 1
                child2 = child1 + 1
                if child1 >= end:
                    break
                if child2 < end and nums[child1] < nums[child2]:
                    child1 = child2
                if nums[root] >= nums[child1]:
                    break
                nums[root], nums[child1] = nums[child1], nums[root]
                root = child1

        n = len(nums)
        # heapify(nums) -> maxheap
        for i in range((n-1)//2, -1, -1):
            sift_down(i, n)

        for i in range(n-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            sift_down(0, i)

        return nums

    def sortArrayShell(self, nums: List[int]) -> List[int]:
        n = len(nums)
        gap = n//2
        while gap > 0:
            for i in range(gap, n):
                tmp = nums[i]
                j = i
                while j >= gap and tmp < nums[j-gap]:
                    nums[j] = nums[j-gap]
                    j = j - gap
                nums[j] = tmp
            gap = gap//2
        return nums

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[1]], [1]),
            ([[2, 1]], [1, 2]),
            ([[5,2,3,1]], [1, 2, 3, 5]),
            ([[5,2,3, 2,1]], [1, 2, 2, 3, 5]),
            ([[3,2,3,1,2,4,5,5,6]], [1, 2, 2, 3, 3, 4, 5, 5, 6]),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


def benchmark(n: int):
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        func = getattr(sol, method)
        nums = list(range(n))
        random.shuffle(nums)

        start = datetime.now()
        res = func(nums)
        assert sorted(res) == res, f'{method}: {res}'
        duration = datetime.now() - start
        print(f"{method:15s}: {duration.total_seconds()}s")


if __name__ == '__main__':
    test()

    print('Benchmark:')
    for n in range(1, 5):
        print(f'N = {10**n}')
        benchmark(10**n)
