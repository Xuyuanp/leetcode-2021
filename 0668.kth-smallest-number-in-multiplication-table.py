#
# @lc app=leetcode id=668 lang=python3
#
# [668] Kth Smallest Number in Multiplication Table
#
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/
#
# algorithms
# Hard (48.34%)
# Likes:    789
# Dislikes: 25
# Total Accepted:    28.2K
# Total Submissions: 58.2K
# Testcase Example:  '3\n3\n5'
#
# Nearly everyone has used the Multiplication Table. The multiplication table
# of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).
#
# Given three integers m, n, and k, return the k^th smallest element in the m x
# n multiplication table.
#
#
# Example 1:
#
#
# Input: m = 3, n = 3, k = 5
# Output: 3
# Explanation: The 5^th smallest number is 3.
#
#
# Example 2:
#
#
# Input: m = 2, n = 3, k = 6
# Output: 6
# Explanation: The 6^th smallest number is 6.
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 3 * 10^4
# 1 <= k <= m * n
#
#
#

# @lc code=start
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(x: int) -> bool:
            count = 0
            for i in range(m):
                count += min(x//(i+1), n)
            return count >= k

        lo, hi = 1, m*n
        while lo < hi:
            mid = lo + (hi-lo)//2
            if not enough(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo


# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    cases = [
        ((3, 3, 5), 3),
        ((2, 3, 6), 6)
    ]
    for (m, n, k), want in cases:
        got = sol.findKthNumber(m, n, k)
        if want != got:
            print(f'Failed => args: {(m, n, k)}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
