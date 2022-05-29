#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (42.10%)
# Likes:    8755
# Dislikes: 415
# Total Accepted:    998.2K
# Total Submissions: 2.4M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
#
#
#
from typing import List

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        STARTI, ENDI = 0, 1
        pre = intervals[0]
        for curr in intervals[1:]:
            # pre:   |-------|
            # case1:   |---|               <-- merge
            # case2:   |--------|          <-- merge and update endi
            # case3:           |---|       <-- yield pre
            if curr[STARTI] <= pre[ENDI]:
                pre[ENDI] = max(pre[ENDI], curr[ENDI])
            else:
                res.append(pre)
                pre = curr
        res.append(pre)
        return res


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[[1, 3], [2, 6], [8, 10], [15, 18]]], [[1, 6], [8, 10], [15, 18]]),
            ([[[1, 4], [4, 5]]], [[1, 5]]),
            ([[[4, 5], [1, 4]]], [[1, 5]]),
            ([[[1, 3], [2, 3]]], [[1, 3]]),
            ([[[2, 3], [1, 3]]], [[1, 3]]),
            ([[[2, 3], [1, 4]]], [[1, 4]]),
            ([[[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]], [[1, 10]]),
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
