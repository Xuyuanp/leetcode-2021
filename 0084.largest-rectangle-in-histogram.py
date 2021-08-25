#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (38.09%)
# Likes:    6440
# Dislikes: 111
# Total Accepted:    379.3K
# Total Submissions: 994.9K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in
# the histogram.
#
#
# Example 1:
#
#
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10
# units.
#
#
# Example 2:
#
#
# Input: heights = [2,4]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4
#
#
#
from typing import List

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        stack = [-1]
        heights.append(0)

        for i, h in enumerate(heights):
            while heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[2]], 2),
            ([[2, 4]], 4),
            ([[2, 1, 2]], 3),
            ([[1, 2, 3]], 4),
            ([[3, 2, 1, 2, 3]], 5),
            ([[2, 1, 5, 6, 2, 3]], 10),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
