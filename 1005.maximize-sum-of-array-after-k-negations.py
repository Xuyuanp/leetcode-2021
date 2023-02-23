#
# @lc app=leetcode id=1005 lang=python3
#
# [1005] Maximize Sum Of Array After K Negations
#
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/
#
# algorithms
# Easy (52.30%)
# Likes:    680
# Dislikes: 64
# Total Accepted:    42.7K
# Total Submissions: 81.8K
# Testcase Example:  '[4,2,3]\n1'
#
# Given an integer array nums and an integer k, modify the array in the
# following way:
#
#
# choose an index i and replace nums[i] with -nums[i].
#
#
# You should apply this process exactly k times. You may choose the same index
# i multiple times.
#
# Return the largest possible sum of the array after modifying it in this
# way.
#
#
# Example 1:
#
#
# Input: nums = [4,2,3], k = 1
# Output: 5
# Explanation: Choose index 1 and nums becomes [4,-2,3].
#
#
# Example 2:
#
#
# Input: nums = [3,-1,0,2], k = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
#
#
# Example 3:
#
#
# Input: nums = [2,-3,-1,5,-4], k = 2
# Output: 13
# Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -100 <= nums[i] <= 100
# 1 <= k <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: -abs(x))
        for i in range(len(nums)):
            if k == 0:
                break
            if nums[i] < 0:
                nums[i] *= -1
                k -= 1
        else:
            nums[-1] *= (-1)**(k % 2)

        return sum(nums)


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1], 1], -1),
            ([[1], 2], 1),
            ([[1, -2], 1], 3),
            ([[1, -2], 2], 1),
            ([[4, 2, 3], 1], 5),
            ([[3, -1, 0, 2], 3], 6),
            ([[2, -3, -1, 5, -4], 2], 13),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    main()
