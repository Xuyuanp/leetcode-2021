#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (42.01%)
# Likes:    4456
# Dislikes: 135
# Total Accepted:    199.1K
# Total Submissions: 473.6K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
#
# Example 1:
#
#
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
#
# Example 2:
#
#
# Input: nums = [-1]
# Output: [0]
#
#
# Example 3:
#
#
# Input: nums = [-1,-1]
# Output: [0,0]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
from typing import List, Tuple

# @lc code=start
class Solution:
    # O(n*log(n)), O(n)
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        INDEX, VALUE = 0, 1

        def merge_sort(nums: List[Tuple[int, int]]) -> List[int]:
            if len(nums) < 2:
                return nums
            mid = len(nums)//2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            new_nums = [0] * (len(left)+len(right))
            i = j = k = 0
            while i < len(left) or j < len(right):
                while j < len(right) and (i == len(left) or left[i][VALUE] > right[j][VALUE]):
                    new_nums[k] = right[j]
                    j += 1
                    k += 1
                while i < len(left) and (j == len(right) or left[i][VALUE] <= right[j][VALUE]):
                    new_nums[k] = left[i]
                    res[left[i][INDEX]] += j
                    i += 1
                    k += 1

            return new_nums

        merge_sort(list(enumerate(nums)))

        return res

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[-1,-1]], [0,0]),
            ([[-1]], [0]),
            ([[5,2,6,1]], [2,1,1,0]),
            ([[1,2,3,4]], [0,0,0,0]),
            ([[4,3,2,1]], [3,2,1,0]),
            ([[26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]],
             [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]),
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
