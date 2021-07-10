#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (45.53%)
# Likes:    4579
# Dislikes: 182
# Total Accepted:    252.7K
# Total Submissions: 554.9K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# You are given an integer array nums and an integer target.
#
# You want to build an expression out of nums by adding one of the symbols '+'
# and '-' before each integer in nums and then concatenate all the
# integers.
#
#
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
# and concatenate them to build the expression "+2-1".
#
#
# Return the number of different expressions that you can build, which
# evaluates to target.
#
#
# Example 1:
#
#
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be
# target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#
#
# Example 2:
#
#
# Input: nums = [1], target = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000
#
#
#


from collections import defaultdict
from typing import List

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counter = defaultdict(int)
        counter[0] = 1
        for n in nums:
            next_counter = defaultdict(int)
            for i in counter:
                next_counter[i+n] += counter[i]
                next_counter[i-n] += counter[i]
            counter = next_counter
        return counter[target]

# @lc code=end


if __name__ == "__main__":
    print(Solution().findTargetSumWays([1,1,1,1,1], target = 3))
    print(Solution().findTargetSumWays([1], target = 1))
    print(Solution().findTargetSumWays([1], target = 3))
    print(Solution().findTargetSumWays([1, 0], target = 1))
    print(Solution().findTargetSumWays([0,38,42,31,13,10,11,12,44,16,38,17,22,28,9,27,20,35,34,39], target = 2))
