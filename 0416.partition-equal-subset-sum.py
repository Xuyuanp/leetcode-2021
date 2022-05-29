#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (45.25%)
# Likes:    5195
# Dislikes: 97
# Total Accepted:    322K
# Total Submissions: 707.9K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array nums containing only positive integers, find if the
# array can be partitioned into two subsets such that the sum of elements in
# both subsets is equal.
#
#
# Example 1:
#
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(n*sum), O(sum)
    def canPartition(self, nums: List[int]) -> bool:
        # sum(A) + sum(B) = sum(S)
        # sum(A) = sum(B)
        # sum(A) = sum(S)/2
        # => find A
        dp = {0}
        total = 0
        for x in nums:
            dp |= {x + y for y in dp}
            total += x
        return total % 2 == 0 and total // 2 in dp

    # O(n*sum), O(sum)
    def canPartition1(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        dp = [False] * (total + 1)
        dp[0] = True
        for x in nums:
            for i in range(total, -1, -1):
                if dp[i]:
                    dp[i + x] = True
        return dp[total // 2]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1]], False),
            ([[1, 1]], True),
            ([[1, 2, 3]], True),
            ([[1, 2, 5]], False),
            ([[1, 5, 11, 5]], True),
            ([[1, 2, 3, 5]], False),
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
