#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (78.24%)
# Likes:    5157
# Dislikes: 209
# Total Accepted:    278K
# Total Submissions: 355.2K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# You are given a string s. We want to partition the string into as many parts
# as possible so that each letter appears in at most one part.
#
# Return a list of integers representing the size of these parts.
#
#
# Example 1:
#
#
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits s into less parts.
#
#
# Example 2:
#
#
# Input: s = "eccbbbbdec"
# Output: [10]
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.
#
#
#
from typing import List

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        seen = {c: i for i, c in enumerate(s)}
        left = right = 0
        for i, c in enumerate(s):
            right = max(right, seen[c])
            if i == right:
                res.append(right-left+1)
                left = i+1
        return res

# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            (['a'], [1]),
            (['eccbbbbdec'], [10]),
            (['ababcbacadefegdehijhklij'], [9,7,8]),
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
