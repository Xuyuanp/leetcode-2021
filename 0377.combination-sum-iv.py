#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (47.33%)
# Likes:    2684
# Dislikes: 303
# Total Accepted:    195K
# Total Submissions: 408.4K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an array of distinct integers nums and a target integer target, return
# the number of possible combinations that add up to target.
#
# The answer is guaranteed to fit in a 32-bit integer.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
#
#
# Example 2:
#
#
# Input: nums = [9], target = 3
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
#
#
#
# Follow up: What if negative numbers are allowed in the given array? How does
# it change the problem? What limitation we need to add to the question to
# allow negative numbers?
#
#
from collections import Counter
from functools import cache
from typing import List

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = Counter()
        dp[0] = 1

        for i in range(1, target + 1):
            for x in nums:
                if x <= i:
                    dp[i] += dp[i - x]

        return dp[target]

    def combinationSum41(self, nums: List[int], target: int) -> int:
        @cache
        def helper(target: int) -> int:
            if target == 0:
                return 1
            res = 0
            for x in nums:
                if x <= target:
                    res += helper(target - x)
            return res

        return helper(target)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1, 2, 3], 4], 7),
            ([[9], 3], 0),
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
