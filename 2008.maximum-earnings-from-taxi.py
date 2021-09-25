#
# @lc app=leetcode id=2008 lang=python3
#
# [2008] Maximum Earnings From Taxi
#
# https://leetcode.com/problems/maximum-earnings-from-taxi/description/
#
# algorithms
# Medium (40.79%)
# Likes:    196
# Dislikes: 5
# Total Accepted:    4.3K
# Total Submissions: 10.5K
# Testcase Example:  '5\n[[2,5,4],[1,5,1]]'
#
# There are n points on a road you are driving your taxi on. The n points on
# the road are labeled from 1 to n in the direction you are going, and you want
# to drive from point 1 to point n to make money by picking up passengers. You
# cannot change the direction of the taxi.
#
# The passengers are represented by a 0-indexed 2D integer array rides, where
# rides[i] = [starti, endi, tipi] denotes the i^th passenger requesting a ride
# from point starti to point endi who is willing to give a tipi dollar tip.
#
# For each passenger i you pick up, you earn endi - starti + tipi dollars. You
# may only drive at most one passenger at a time.
#
# Given n and rides, return the maximum number of dollars you can earn by
# picking up the passengers optimally.
#
# Note: You may drop off a passenger and pick up a different passenger at the
# same point.
#
#
# Example 1:
#
#
# Input: n = 5, rides = [[2,5,4],[1,5,1]]
# Output: 7
# Explanation: We can pick up passenger 0 to earn 5 - 2 + 4 = 7 dollars.
#
#
# Example 2:
#
#
# Input: n = 20, rides =
# [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
# Output: 20
# Explanation: We will pick up the following passengers:
# - Drive passenger 1 from point 3 to point 10 for a profit of 10 - 3 + 2 = 9
# dollars.
# - Drive passenger 2 from point 10 to point 12 for a profit of 12 - 10 + 3 = 5
# dollars.
# - Drive passenger 5 from point 13 to point 18 for a profit of 18 - 13 + 1 = 6
# dollars.
# We earn 9 + 5 + 6 = 20 dollars in total.
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
# 1 <= rides.length <= 3 * 10^4
# rides[i].length == 3
# 1 <= starti < endi <= n
# 1 <= tipi <= 10^5
#
#
#
from collections import defaultdict
from typing import List

# @lc code=start
class Solution:
    # O(m*log(m)) + O(n+m), O(m+n)
    #
    # dp[i] = max(dp[i-1], dp[startj] + (profit of rides[j] for all endj == i))
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        START, END, TIP = 0, 1, 2

        rides.sort(key=lambda x: (x[END], x[START], -x[TIP]))
        curr = 0
        dp = [0]*(n+1)

        for i in range(1, n+1):
            dp[i] = dp[i-1]
            while curr < len(rides) and i == rides[curr][END]:
                ride = rides[curr]
                dp[i] = max(dp[i], dp[ride[START]] + ride[END]-ride[START]+ride[TIP])
                curr += 1

        return dp[n]

    # O(m) + O(m+n), O(m+n)
    def maxTaxiEarnings1(self, n: int, rides: List[List[int]]) -> int:
        ends = defaultdict(list)
        for start, end, tip in rides:
            ends[end].append((start, tip))

        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1]
            if i not in ends:
                continue
            for start, tip in ends[i]:
                dp[i] = max(dp[i], dp[start] + i-start+tip)

        return dp[n]

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([5, [[2,5,4],[1,5,1]]], 7),
            ([20, [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]], 20),
            ([10, [[9,10,2],[4,5,6],[6,8,1],[1,5,5],[4,9,5],[1,6,5],[4,8,3],[4,7,10],[1,9,8],[2,3,5]]], 22),
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
