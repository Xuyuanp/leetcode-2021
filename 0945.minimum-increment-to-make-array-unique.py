#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/
#
# algorithms
# Medium (47.35%)
# Likes:    785
# Dislikes: 35
# Total Accepted:    42.7K
# Total Submissions: 89.5K
# Testcase Example:  '[1,2,2]'
#
# You are given an integer array nums. In one move, you can pick an index i
# where 0 <= i < nums.length and increment nums[i] by 1.
#
# Return the minimum number of moves to make every value in nums unique.
#
#
# Example 1:
#
#
# Input: nums = [1,2,2]
# Output: 1
# Explanation: After 1 move, the array could be [1, 2, 3].
#
#
# Example 2:
#
#
# Input: nums = [3,2,1,2,1,7]
# Output: 6
# Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to
# have all unique values.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
#
#
#
from typing import List

# @lc code=start
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        start = nums[0]
        for num in nums:
            res += max(0, start - num)
            start = max(start + 1, num + 1)
        return res

    def minIncrementForUnique1(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                gap = nums[i - 1] - nums[i] + 1
                res += gap
                nums[i] += gap

        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1]], 0),
            ([[1, 2, 2]], 1),
            ([[3, 2, 1, 2, 1, 7]], 6),
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
