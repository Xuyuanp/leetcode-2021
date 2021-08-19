#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (55.30%)
# Likes:    5229
# Dislikes: 195
# Total Accepted:    386.1K
# Total Submissions: 694K
# Testcase Example:  '3'
#
# Given an integer n, return the number of structurally unique BST's (binary
# search trees) which has exactly n nodes of unique values from 1 to n.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 5
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 19
#
#
#

# @lc code=start
from functools import lru_cache


class Solution:
    # O(n^2), O(n). memoization
    def numTrees(self, n: int) -> int:

        @lru_cache(None)
        def helper(m: int):
            if m < 2:
                return 1
            return sum(helper(i)*helper(m-i-1) for i in range(m))

        return helper(n)

    # O(n^2), O(n). DP
    def numTrees1(self, n: int) -> int:
        if n < 2:
            return n
        dp = [1] * (n+1)
        for i in range(2, n+1):
            dp[i] = sum(dp[j]*dp[i-j-1] for j in range(i))
        return dp[-1]

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([1], 1),
            ([2], 2),
            ([3], 5),
            ([4], 14),
            ([5], 42),
            ([10], 16796),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
