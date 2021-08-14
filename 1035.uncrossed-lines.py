#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#
# https://leetcode.com/problems/uncrossed-lines/description/
#
# algorithms
# Medium (56.45%)
# Likes:    1302
# Dislikes: 24
# Total Accepted:    57.4K
# Total Submissions: 101.3K
# Testcase Example:  '[1,4,2]\n[1,2,4]'
#
# You are given two integer arrays nums1 and nums2. We write the integers of
# nums1 and nums2 (in the order they are given) on two separate horizontal
# lines.
#
# We may draw connecting lines: a straight line connecting two numbers nums1[i]
# and nums2[j] such that:
#
#
# nums1[i] == nums2[j], and
# the line we draw does not intersect any other connecting (non-horizontal)
# line.
#
#
# Note that a connecting line cannot intersect even at the endpoints (i.e.,
# each number can only belong to one connecting line).
#
# Return the maximum number of connecting lines we can draw in this way.
#
#
# Example 1:
#
#
# Input: nums1 = [1,4,2], nums2 = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to
# nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
#
#
# Example 2:
#
#
# Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
# Output: 3
#
#
# Example 3:
#
#
# Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 500
# 1 <= nums1[i], nums2[j] <= 2000
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(m*n), O(m*n). longest common subsequence. See also: 1143
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([[3],[3,3,2]], 1),
            ([[1,4,2], [1,2,4]], 2),
            ([[4,2], [2,4]], 1),
            ([[1,2], [3,4]], 0),
            ([[2,5,1,2,5], [10,5,2,1,5,2]], 3),
            ([[1,3,7,1,7,5], [1,9,2,5,1]], 2),
            ([[2,1], [1,2,1,3,3,2]], 2),
            ([[1,2,1,3,3,2], [2, 1]], 2),
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
