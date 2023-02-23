#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
#
# algorithms
# Medium (50.17%)
# Likes:    1995
# Dislikes: 73
# Total Accepted:    123.1K
# Total Submissions: 244.5K
# Testcase Example:  '[[10,16],[2,8],[1,6],[7,12]]'
#
# There are some spherical balloons spread in two-dimensional space. For each
# balloon, provided input is the start and end coordinates of the horizontal
# diameter. Since it's horizontal, y-coordinates don't matter, and hence the
# x-coordinates of start and end of the diameter suffice. The start is always
# smaller than the end.
#
# An arrow can be shot up exactly vertically from different points along the
# x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart
# ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An
# arrow once shot keeps traveling up infinitely.
#
# Given an array points where points[i] = [xstart, xend], return the minimum
# number of arrows that must be shot to burst all balloons.
#
#
# Example 1:
#
#
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: One way is to shoot one arrow for example at x = 6 (bursting the
# balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two
# balloons).
#
#
# Example 2:
#
#
# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
#
#
# Example 3:
#
#
# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= points.length <= 10^4
# points[i].length == 2
# -2^31 <= xstart < xend <= 2^31 - 1
#
#
#
from typing import List


# @lc code=start
class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        O(n*log(n)), O(n). greedy. longest-increasing-subsequence
        |----|
         |-----|
              |----|
                 |------|
        """
        points.sort(key=lambda p: p[1])
        cnt = 1
        pre = points[0]
        for curr in points[1:]:
            if curr[0] > pre[1]:
                cnt += 1
                pre = curr
        return cnt


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[[1, 2]]], 1),
            ([[[1, 2], [2, 3]]], 1),
            ([[[1, 2], [3, 4]]], 2),
            ([[[10, 16], [2, 8], [1, 6], [7, 12]]], 2),
            ([[[1, 2], [3, 4], [5, 6], [7, 8]]], 4),
            ([[[1, 2], [2, 3], [3, 4], [4, 5]]], 2),
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
