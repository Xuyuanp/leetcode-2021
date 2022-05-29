#
# @lc app=leetcode id=440 lang=python3
#
# [440] K-th Smallest in Lexicographical Order
#
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/
#
# algorithms
# Hard (30.00%)
# Likes:    446
# Dislikes: 65
# Total Accepted:    15.7K
# Total Submissions: 52.3K
# Testcase Example:  '13\n2'
#
# Given two integers n and k, return the k^th lexicographically smallest
# integer in the range [1, n].
#
#
# Example 1:
#
#
# Input: n = 13, k = 2
# Output: 10
# Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6,
# 7, 8, 9], so the second smallest number is 10.
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= k <= n <= 10^9
#
#
#

# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        res = 1
        k -= 1
        while k > 0:
            count = 0
            interval = [res, res + 1]
            while interval[0] <= n:
                count += min(n + 1, interval[1]) - interval[0]
                interval = [interval[0] * 10, interval[1] * 10]
            if k >= count:
                res += 1
                k -= count
            else:
                res *= 10
                k -= 1
        return res


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([13, 2], 10),
        ([1, 1], 1),
        ([13, 10], 6),
        ([100, 50], 53),
        ([100, 100], 100),
    ]
    for (n, k), want in cases:
        got = sol.findKthNumber(n, k)
        if want != got:
            print(f"Failed => args: {(n, k)}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
