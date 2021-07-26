#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (49.06%)
# Likes:    7230
# Dislikes: 223
# Total Accepted:    1M
# Total Submissions: 2.1M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#
# Constraints:
#
#
# 1 <= n <= 45
#
#
#

# @lc code=start
class Solution:
    # O(n), O(1)
    def climbStairs(self, n: int) -> int:
        x, y = 1, 1
        for _ in range(2, n+1):
            y, x = x+y, y
        return y

    # O(n), O(n)
    def climbStairs3(self, n: int) -> int:
        if n < 2:
            return 1
        def helper(n: int, x: int, y: int):
            if n == 0:
                return y
            return helper(n-1, y, x+y)
        return helper(n-1, 1, 1)

    # O(n), O(n)
    def climbStairs2(self, n: int) -> int:
        dp = {0: 1, 1: 1}
        def helper(n: int) -> int:
            if n not in dp:
                dp[n] = helper(n-1) + helper(n-2)
            return dp[n]
        return helper(n)

    # O(n), O(n)
    def climbStairs1(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n];

    # O(2^n) O(n)
    def climbStairs0(self, n: int) -> int:
        def helper(n: int) -> int:
            if n < 2:
                return 1
            return helper(n-1) + helper(n-2)
        return helper(n)


# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    cases = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
    ]
    for n, want in cases:
        got = sol.climbStairs(n)
        if want != got:
            print(f'Failed => args: {n}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
