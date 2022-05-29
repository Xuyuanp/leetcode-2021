#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (51.63%)
# Likes:    1911
# Dislikes: 283
# Total Accepted:    146.3K
# Total Submissions: 282.1K
# Testcase Example:  '2'
#
# Given an integer n, break it into the sum of k positive integers, where k >=
# 2, and maximize the product of those integers.
#
# Return the maximum product you can get.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
#
#
# Example 2:
#
#
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
#
#
#
# Constraints:
#
#
# 2 <= n <= 58
#
#
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(2, i):
                dp[i] = max(dp[i], j * max(i - j, dp[i - j]))
        return dp[n]

    def integerBreak1(self, n: int) -> int:
        if n < 4:
            return n - 1
        dp = [0] * (n + 1)
        # max(i, dp[i]) return i iff i < 4, so we init the first 3 elememts as themself
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            for j in range(2, i - 1):
                dp[i] = max(dp[i], j * dp[i - j])
        return dp[n]

    # O(log(k)), O(1). k is number of 3 in n
    # for all N > 4 => 3*(n-3) > n
    def integerBreak2(self, n: int) -> int:
        if n < 4:
            return n - 1
        three, rest = divmod(n, 3)
        if rest < 2:
            rest += 3
            three -= 1
        return rest * (3**three)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([2], 1),
            ([3], 2),
            ([4], 4),
            ([5], 6),
            ([6], 9),
            ([7], 12),
            ([8], 18),
            ([9], 27),
            ([10], 36),
            ([11], 54),
            ([12], 81),
            ([57], 1162261467),
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
    test()
