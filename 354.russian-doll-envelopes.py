#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (38.39%)
# Likes:    2322
# Dislikes: 63
# Total Accepted:    112.8K
# Total Submissions: 292.4K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
# represents the width and the height of an envelope.
#
# One envelope can fit into another if and only if both the width and height of
# one envelope are greater than the other envelope's width and height.
#
# Return the maximum number of envelopes you can Russian doll (i.e., put one
# inside the other).
#
# Note: You cannot rotate an envelope.
#
#
# Example 1:
#
#
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
#
#
# Example 2:
#
#
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= envelopes.length <= 5000
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^4
#
#
#
from typing import List

# @lc code=start
from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda env: (env[0], -env[1]))
        sub = []

        for _, h in envelopes:
            pos = bisect_left(sub, h)
            if pos == len(sub):
                sub.append(h)
            else:
                sub[pos] = h

        return len(sub)

# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    cases = [
        ([[5,4],[6,4],[6,7],[2,3]], 3),
        ([[1,1],[1,1],[1,1]], 1),
        ([[1,1],[2,1],[1,1]], 1),
    ]
    for envelopes, want in cases:
        got = sol.maxEnvelopes(envelopes)
        if want != got:
            print(f'Failed => args: {envelopes}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
