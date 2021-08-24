#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/
#
# algorithms
# Hard (56.55%)
# Likes:    867
# Dislikes: 100
# Total Accepted:    47.9K
# Total Submissions: 84.4K
# Testcase Example:  '[6,5,4,3,2,1]\n2'
#
# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To
# work on the i-th job, you have to finish all the jobs j where 0 <= j < i).
#
# You have to finish at least one task every day. The difficulty of a job
# schedule is the sum of difficulties of each day of the d days. The difficulty
# of a day is the maximum difficulty of a job done in that day.
#
# Given an array of integers jobDifficulty and an integer d. The difficulty of
# the i-th job is jobDifficulty[i].
#
# Return the minimum difficulty of a job schedule. If you cannot find a
# schedule for the jobs return -1.
#
#
# Example 1:
#
#
# Input: jobDifficulty = [6,5,4,3,2,1], d = 2
# Output: 7
# Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
# Second day you can finish the last job, total difficulty = 1.
# The difficulty of the schedule = 6 + 1 = 7
#
#
# Example 2:
#
#
# Input: jobDifficulty = [9,9,9], d = 4
# Output: -1
# Explanation: If you finish a job per day you will still have a free day. you
# cannot find a schedule for the given jobs.
#
#
# Example 3:
#
#
# Input: jobDifficulty = [1,1,1], d = 3
# Output: 3
# Explanation: The schedule is one job per day. total difficulty will be 3.
#
#
# Example 4:
#
#
# Input: jobDifficulty = [7,1,7,1,7,1], d = 3
# Output: 15
#
#
# Example 5:
#
#
# Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
# Output: 843
#
#
#
# Constraints:
#
#
# 1 <= jobDifficulty.length <= 300
# 0 <= jobDifficulty[i] <= 1000
# 1 <= d <= 10
#
#
#
from functools import cache
from typing import List

# @lc code=start
class Solution:
    # O(n*n*d), O(n*d)
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        @cache
        def helper(start: int, dd: int) -> int:
            if dd == 1:
                return max(jobDifficulty[start:])
            res = float('inf')
            curr_max = -1
            for i in range(start, n-dd+1):
                curr_max = max(curr_max, jobDifficulty[i])
                res = min(res, curr_max+helper(i+1, dd-1))

            return res

        return helper(0, d)

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[6,5,4,3,2,1], 2], 7),
            ([[9,9,9], 4], -1),
            ([[1,1,1], 3], 3),
            ([[7,1,7,1,7,1], 3], 15),
            ([[11,111,22,222,33,333,44,444], 6], 843),
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
