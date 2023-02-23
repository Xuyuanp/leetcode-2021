#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.34%)
# Likes:    6803
# Dislikes: 315
# Total Accepted:    502.3K
# Total Submissions: 1.1M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#
from collections import Counter
from typing import List


# @lc code=start
class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ufs = {}

        def find(x):
            if x != ufs.setdefault(x, x):
                ufs[x] = find(ufs[x])
            return ufs[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                ufs[rx] = ry

        for x in nums:
            find(x)
            if x - 1 in ufs:
                union(x - 1, x)
            if x + 1 in ufs:
                union(x, x + 1)

        counter = Counter()
        for x in ufs:
            counter[find(x)] += 1
        return counter.most_common(1)[0][1]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[100, 4, 200, 1, 3, 2]], 4),
            ([[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], 9),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
