#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (57.99%)
# Likes:    2936
# Dislikes: 88
# Total Accepted:    205K
# Total Submissions: 353.2K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# Find this single element that appears only once.
#
# Follow up: Your solution should run in O(log n) time and O(1) space.
#
#
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
#
#
#
from typing import List

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == nums[mid + 1]:
                if mid % 2 == 1:
                    # [1,2,2,3,3,4,4]
                    # [1,2,2]
                    right = mid - 1
                else:
                    # [1,1,2,2,3]
                    # [1,1,2,2,3,3,4,4,5]
                    left = mid + 2
            elif nums[mid - 1] == nums[mid]:
                if mid % 2 == 1:
                    # [1,1,2]
                    # [1,1,2,2,3,4,4]
                    left = mid + 1
                else:
                    # [1,2,2,3,3]
                    # [1,1,2,3,3,4,4,5,5]
                    right = mid - 2
            else:
                # [1,1,2,3,3]
                return nums[mid]
        return nums[left]


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[1, 2, 2]], 1),
            ([[1, 1, 2]], 2),
            ([[1, 2, 2, 3, 3]], 1),
            ([[1, 1, 2, 3, 3]], 2),
            ([[1, 1, 2, 2, 3]], 3),
            ([[3, 3, 7, 7, 10, 11, 11]], 10),
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
