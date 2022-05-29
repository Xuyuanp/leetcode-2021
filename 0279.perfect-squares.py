#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (49.80%)
# Likes:    4853
# Dislikes: 250
# Total Accepted:    421.6K
# Total Submissions: 843.3K
# Testcase Example:  '12'
#
# Given an integer n, return the least number of perfect square numbers that
# sum to n.
#
# A perfect square is an integer that is the square of an integer; in other
# words, it is the product of some integer with itself. For example, 1, 4, 9,
# and 16 are perfect squares while 3 and 11 are not.
#
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
#
#
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        while (m := len(dp)) <= n:
            square = float("inf")
            curr = 1
            while (val := curr**2) <= m:
                square = min(square, dp[m - val] + 1)
                curr += 1
            dp.append(square)

        return dp[n]

    # O(n*sqrt(n)), O(n)
    def numSquares1(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([1], 1),
            ([2], 2),
            ([3], 3),
            ([4], 1),
            ([5], 2),
            ([6], 3),
            ([7], 4),
            ([8], 2),
            ([9], 1),
            ([10], 2),
            ([11], 3),
            ([12], 3),
            ([13], 2),
            ([90], 2),
            ([100], 1),
            ([11100], 4),
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
