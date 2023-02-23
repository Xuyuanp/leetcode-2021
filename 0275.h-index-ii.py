#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#
# https://leetcode.com/problems/h-index-ii/description/
#
# algorithms
# Medium (36.50%)
# Likes:    579
# Dislikes: 907
# Total Accepted:    146.3K
# Total Submissions: 400.3K
# Testcase Example:  '[0,1,3,5,6]'
#
# Given an array of integers citations where citations[i] is the number of
# citations a researcher received for their i^th paper and citations is sorted
# in an ascending order, return compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: A scientist has an index
# h if h of their n papers have at least h citations each, and the other n − h
# papers have no more than h citations each.
#
# If there are several possible values for h, the maximum one is taken as the
# h-index.
#
# You must write an algorithm that runs in logarithmic time.
#
#
# Example 1:
#
#
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each
# of them had received 0, 1, 3, 5, 6 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining two with no more than 3 citations each, their h-index is 3.
#
#
# Example 2:
#
#
# Input: citations = [1,2,100]
# Output: 2
#
#
#
# Constraints:
#
#
# n == citations.length
# 1 <= n <= 10^5
# 0 <= citations[i] <= 1000
# citations is sorted in ascending order.
#
#
#
from typing import List


# @lc code=start
class Solution:

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] == n - mid:
                return citations[mid]
            if citations[mid] > n - mid:
                right = mid - 1
            else:
                left = mid + 1

        return n - left


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[0]], 0),
            ([[1]], 1),
            ([[100]], 1),
            ([[1, 100]], 1),
            ([[2, 2]], 2),
            ([[1, 2, 100]], 2),
            ([[1, 3, 100]], 2),
            ([[0, 1, 3, 5, 6]], 3),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    main()
