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
    # O(min(m,n)*log(m*n))
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m > n:
            m, n = n, m

        def enough(x: int) -> bool:
            count = 0
            for i in range(m):
                count += min(x // (i + 1), n)
            return count >= k

        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            if not enough(mid):
                left = mid + 1
            else:
                right = mid
        return left

    # O(min(m,n)*log(m*n))
    def findKthNumber1(self, m: int, n: int, k: int) -> int:
        if m > n:
            m, n = n, m

        def n_less_than(x: int) -> int:
            count = 0
            for i in range(1, m + 1):
                count += min(x // i,
                             n)  # nums of vals less than x in each line
            return count

        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            if n_less_than(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [([3, 3, 5], 3), ([2, 3, 6], 6)]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
