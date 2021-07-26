#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (65.36%)
# Likes:    4640
# Dislikes: 135
# Total Accepted:    262K
# Total Submissions: 400.7K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the i^th day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
#
#
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
#
#
# Constraints:
#
#
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
#
#
#
from collections import deque
from typing import List

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = deque()

        for i, curr in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res

# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    cases = [
        ([30], [0]),
        ([30, 40], [1, 0]),
        ([50, 40, 30], [0, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
    ]
    for temperatures, want in cases:
        got = sol.dailyTemperatures(temperatures)
        if want != got:
            print(f'Failed => args: {temperatures}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
