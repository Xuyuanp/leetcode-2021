#
# @lc app=leetcode id=1563 lang=python3
#
# [1563] Stone Game V
#
# https://leetcode.com/problems/stone-game-v/description/
#
# algorithms
# Hard (40.20%)
# Likes:    278
# Dislikes: 54
# Total Accepted:    10.5K
# Total Submissions: 26K
# Testcase Example:  '[6,2,3,4,5,5]'
#
# There are several stones arranged in a row, and each stone has an associated
# value which is an integer given in the array stoneValue.
#
# In each round of the game, Alice divides the row into two non-empty rows
# (i.e. left row and right row), then Bob calculates the value of each row
# which is the sum of the values of all the stones in this row. Bob throws away
# the row which has the maximum value, and Alice's score increases by the value
# of the remaining row. If the value of the two rows are equal, Bob lets Alice
# decide which row will be thrown away. The next round starts with the
# remaining row.
#
# The game ends when there is only one stone remaining. Alice's is initially
# zero.
#
# Return the maximum score that Alice can obtain.
#
#
# Example 1:
#
#
# Input: stoneValue = [6,2,3,4,5,5]
# Output: 18
# Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5].
# The left row has the value 11 and the right row has value 14. Bob throws away
# the right row and Alice's score is now 11.
# In the second round Alice divides the row to [6], [2,3]. This time Bob throws
# away the left row and Alice's score becomes 16 (11 + 5).
# The last round Alice has only one choice to divide the row which is [2], [3].
# Bob throws away the right row and Alice's score is now 18 (16 + 2). The game
# ends because only one stone is remaining in the row.
#
#
# Example 2:
#
#
# Input: stoneValue = [7,7,7,7,7,7,7]
# Output: 28
#
#
# Example 3:
#
#
# Input: stoneValue = [4]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= stoneValue.length <= 500
# 1 <= stoneValue[i] <= 10^6
#
#
#

# go: AC
#
# func max(x int, others ...int) int {
# 	res := x
# 	for _, y := range others {
# 		if y > res {
# 			res = y
# 		}
# 	}
# 	return res
# }
#
# func stoneGameV(stoneValues []int) int {
# 	n := len(stoneValues)
#
# 	dp := make([][]int, n+1)
# 	for i := 0; i < n+1; i++ {
# 		dp[i] = make([]int, n+1)
# 	}
#
# 	presum := make([]int, n+1)
# 	for i := 1; i < n+1; i++ {
# 		presum[i] = presum[i-1] + stoneValues[i-1]
# 	}
#
# 	var helper func(int, int) int
# 	helper = func(i int, j int) int {
# 		if i+1 == j {
# 			return 0
# 		}
# 		if dp[i][j] > 0 {
# 			return dp[i][j]
# 		}
# 		for k := i + 1; k < j; k++ {
# 			left := presum[k] - presum[i]
# 			right := presum[j] - presum[k]
# 			if left < right {
# 				dp[i][j] = max(dp[i][j], left+helper(i, k))
# 			} else if left > right {
# 				dp[i][j] = max(dp[i][j], right+helper(k, j))
# 			} else {
# 				dp[i][j] = max(dp[i][j], left+helper(i, k), right+helper(k, j))
# 			}
# 		}
# 		return dp[i][j]
# 	}
#
# 	return helper(0, n)
# }

from functools import cache
from typing import List

# @lc code=start
class Solution:
    # O(n^3), O(n^2). TLE (only python)
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] += presum[i] + stoneValue[i]

        # helper returns the answer of stoneValue[start:end]
        @cache
        def helper(start: int, end: int) -> int:
            if start + 1 == end:
                return 0
            res = 0
            for k in range(start + 1, end):  # split stones into [start:k] and [k:end]
                left = presum[k] - presum[start]  # sum(stoneValue[start:k])
                right = presum[end] - presum[k]  # sum(stoneValue[k:end])
                if left > right:
                    res = max(res, right + helper(k, end))
                elif left < right:
                    res = max(res, left + helper(start, k))
                else:
                    res = max(res, right + helper(k, end), left + helper(start, k))

            return res

        return helper(0, n)

    # O(n^3), O(n^2). TLE
    def stoneGameV1(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] += presum[i] + stoneValue[i]

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length
                for k in range(i + 1, j):
                    left = presum[k] - presum[i]
                    right = presum[j] - presum[k]
                    if left > right:
                        dp[i][j] = max(dp[i][j], right + dp[k][j])
                    elif left < right:
                        dp[i][j] = max(dp[i][j], left + dp[i][k])
                    else:
                        dp[i][j] = max(dp[i][j], left + dp[i][k], right + dp[k][j])

        return dp[0][n]

    # TODO: Optimize => O(n^2)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[4]], 0),
            ([[1, 2]], 1),
            ([[6, 2, 3, 4, 5, 5]], 18),
            ([[7, 7, 7, 7, 7, 7, 7]], 28),
            ([[98, 77, 24, 49, 6, 12, 2, 44, 51]], 259),
            ([[77, 24, 49, 6, 12, 2, 44, 51, 96]], 265),
            ([[98, 77, 24, 49, 6, 12, 2, 44, 51, 96]], 330),
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
