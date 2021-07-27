#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Hard (40.13%)
# Likes:    2571
# Dislikes: 374
# Total Accepted:    234.9K
# Total Submissions: 583K
# Testcase Example:  '3\n3'
#
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
#
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
# Given n and k, return the k^th permutation sequence.
#
#
# Example 1:
# Input: n = 3, k = 3
# Output: "213"
# Example 2:
# Input: n = 4, k = 9
# Output: "2314"
# Example 3:
# Input: n = 3, k = 1
# Output: "123"
#
#
# Constraints:
#
#
# 1 <= n <= 9
# 1 <= k <= n!
#
#
#

# @lc code=start
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ''

        nums = [i for i in range(1, n+1)]
        k-=1
        for _ in range(n):
            j, k = divmod(k, math.factorial(len(nums)-1))
            res += str(nums[j])
            nums.remove(nums[j])

        return res

# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    cases = [
        ((3, 3), '213'),
        ((4, 9), '2314'),
        ((3, 1), '123'),
        ((8, 100), '12384675'),
    ]
    for (n, k), want in cases:
        got = sol.getPermutation(n, k)
        if want != got:
            print(f'Failed => args: {(n, k)}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
