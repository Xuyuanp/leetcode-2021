#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (33.31%)
# Likes:    5086
# Dislikes: 203
# Total Accepted:    397.9K
# Total Submissions: 1.2M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
#
#
#
from typing import List


# @lc code=start
class Solution:

    def jump3(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] is the min jumps to reach the index i from the first index
        dp = [float("inf")] * n
        dp[0] = 0
        for i in range(n):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]

    def jump2(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] is the min jumps to reach the last index from the index i
        dp = [float("inf")] * n
        dp[-1] = 0
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= n - 1:
                dp[i] = 1
            elif nums[i] > 0:
                dp[i] = min(dp[i + 1:i + nums[i] + 1]) + 1
        return dp[0]

    def jump(self, nums: List[int]) -> int:
        left = right = steps = 0
        while right < len(nums) - 1:
            steps += 1
            nxt = max(i + nums[i] for i in range(left, right + 1))
            left, right = right + 1, nxt

        return steps


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1]], 0),
            ([[1, 2]], 1),
            ([[2, 2, 2]], 1),
            ([[2, 3, 0, 1, 4]], 2),
            ([[2, 3, 1, 1, 4]], 2),
            ([[5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]], 3),
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
