#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (44.78%)
# Likes:    2427
# Dislikes: 70
# Total Accepted:    157.2K
# Total Submissions: 347.7K
# Testcase Example:  '[[1,2],[2,3],[3,4],[1,3]]'
#
# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of
# the intervals non-overlapping.
#
#
# Example 1:
#
#
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are
# non-overlapping.
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals
# non-overlapping.
#
#
# Example 3:
#
#
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= starti < endi <= 5 * 10^4
#
#
#
from typing import List

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cnt, pre = 1, intervals[0]
        for curr in intervals[1:]:
            if curr[0] >= pre[1]:
                # pre:  |-----|
                # curr:         |----|
                # a valid increasing sequence
                cnt += 1
                pre = curr
            elif curr[1] <= pre[1]:
                # pre:  |------|
                # curr:   |---|
                # we can use the curr's endi replacing the prev's
                pre = curr
            # else:
            # pre:  |-----|
            # curr:   |-----|
            # the current interval has no contribute to new increasing sequence

        return len(intervals) - cnt

    def eraseOverlapIntervals1(self, intervals: List[List[int]]) -> int:
        """
        O(n*long(n)), O(n). greedy
        cnt is the length of the longest increasing subsequence
        """
        intervals.sort(key=lambda x: x[1])
        cnt, pre = 1, intervals[0]
        for curr in intervals[1:]:
            if curr[0] >= pre[1]:
                # pre:  |-----|
                # curr:           |----|
                # a valid increasing sequence
                cnt += 1
                pre = curr
            # else:
            # pre:  |-----|
            # curr:   |------|
            #   or |--------|
            # the current interval has no contribute to new increasing sequence

        return len(intervals) - cnt


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[[1, 2], [2, 3], [3, 4], [1, 3]]], 1),
            ([[[1, 2], [1, 2], [1, 2]]], 2),
            ([[[1, 2], [2, 3]]], 0),
            ([[[1, 100], [11, 22], [1, 11], [2, 12]]], 2),
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
