#
# @lc app=leetcode id=960 lang=python3
#
# [960] Delete Columns to Make Sorted III
#
# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/description/
#
# algorithms
# Hard (55.60%)
# Likes:    351
# Dislikes: 9
# Total Accepted:    8.9K
# Total Submissions: 16K
# Testcase Example:  '["babca","bbazb"]'
#
# You are given an array of n strings strs, all of the same length.
#
# We may choose any deletion indices, and we delete all the characters in those
# indices for each string.
#
# For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0,
# 2, 3}, then the final array after deletions is ["bef", "vyz"].
#
# Suppose we chose a set of deletion indices answer such that after deletions,
# the final array has every string (row) in lexicographic order. (i.e.,
# (strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]), and
# (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]), and so on).
# Return the minimum possible value of answer.length.
#
#
# Example 1:
#
#
# Input: strs = ["babca","bbazb"]
# Output: 3
# Explanation: After deleting columns 0, 1, and 4, the final array is strs =
# ["bc", "az"].
# Both these rows are individually in lexicographic order (ie. strs[0][0] <=
# strs[0][1] and strs[1][0] <= strs[1][1]).
# Note that strs[0] > strs[1] - the array strs is not necessarily in
# lexicographic order.
#
# Example 2:
#
#
# Input: strs = ["edcba"]
# Output: 4
# Explanation: If we delete less than 4 columns, the only row will not be
# lexicographically sorted.
#
#
# Example 3:
#
#
# Input: strs = ["ghi","def","abc"]
# Output: 0
# Explanation: All rows are already lexicographically sorted.
#
#
#
# Constraints:
#
#
# n == strs.length
# 1 <= n <= 100
# 1 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#
#
#
#
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(m*n^2), O(n). m = len(strs), n = len(strs[0])
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])

        # dp[i] is the longest increasing sub sequence in strs[..][:i+1]
        dp = [1] * n
        max_len = 1
        for i in range(1, n):
            for j in range(i):
                if all(row[j] <= row[i] for row in strs):
                    dp[i] = max(dp[i], 1+dp[j])
            max_len = max(max_len, dp[i])
        return n - max_len

# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([['abc']], 0),
            ([['abc', 'def']], 0),
            ([['aaa', 'aaa', 'aaa']], 0),
            ([["babca","bbazb"]], 3),
            ([["edcba"]], 4),
            ([["ghi","def","abc"]], 0),
            ([["abbabb","babbaa","bbbbbb","babbaa"]], 3),
            ([["aaababa","ababbaa"]], 4),
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
    main()
