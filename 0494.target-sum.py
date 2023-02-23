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

from collections import Counter, defaultdict
from functools import lru_cache
from typing import List


# @lc code=start
class Solution:

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        mem = {}

        def helper(index: int, curr: int) -> int:
            if (index, curr) not in mem:
                if index == len(nums):
                    mem[index, curr] = 1 if curr == target else 0
                else:
                    positive = helper(index + 1, curr + nums[index])
                    negative = helper(index + 1, curr - nums[index])
                    mem[index, curr] = positive + negative
            return mem[index, curr]

        return helper(0, 0)

    def findTargetSumWays1(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def helper(index: int, curr: int) -> int:
            if index == len(nums):
                return 1 if curr == target else 0

            positive = helper(index + 1, curr + nums[index])
            negative = helper(index + 1, curr - nums[index])
            return positive + negative

        return helper(0, 0)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counter = defaultdict(int)
        counter[0] = 1
        for x in nums:
            next_counter = defaultdict(int)
            for i in counter:
                next_counter[i + x] += counter[i]
                next_counter[i - x] += counter[i]
            counter = next_counter
        return counter[target]

    # O(n*sum), O(sum)
    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        # sum(A) + sum(B) = sum(S)
        # sum(A) - sum(B) = target
        # sum(A) = (sum(S) + target)/2
        # => find A
        total = 0
        counter = Counter([0])
        for x in nums:
            total += x
            next_counter = Counter(counter)
            for i in counter:
                next_counter[i + x] += counter[i]
            counter = next_counter
        if (total + target) % 2 == 1:
            return 0
        return counter[(total + target) // 2]


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1], 1], 1),
            ([[1], 3], 0),
            ([[1, 0], 1], 2),
            ([[1, 1, 1, 1, 1], 3], 5),
            (
                [
                    [
                        0,
                        38,
                        42,
                        31,
                        13,
                        10,
                        11,
                        12,
                        44,
                        16,
                        38,
                        17,
                        22,
                        28,
                        9,
                        27,
                        20,
                        35,
                        34,
                        39,
                    ],
                    2,
                ],
                6666,
            ),
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
