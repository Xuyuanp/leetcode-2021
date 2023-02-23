#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#
# https://leetcode.com/problems/assign-cookies/description/
#
# algorithms
# Easy (50.44%)
# Likes:    978
# Dislikes: 135
# Total Accepted:    132.5K
# Total Submissions: 262.8K
# Testcase Example:  '[1,2,3]\n[1,1]'
#
# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
#
# Each child i has a greed factor g[i], which is the minimum size of a cookie
# that the child will be content with; and each cookie j has a size s[j]. If
# s[j] >= g[i], we can assign the cookie j to the child i, and the child i will
# be content. Your goal is to maximize the number of your content children and
# output the maximum number.
#
#
# Example 1:
#
#
# Input: g = [1,2,3], s = [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3
# children are 1, 2, 3.
# And even though you have 2 cookies, since their size is both 1, you could
# only make the child whose greed factor is 1 content.
# You need to output 1.
#
#
# Example 2:
#
#
# Input: g = [1,2], s = [1,2,3]
# Output: 2
# Explanation: You have 2 children and 3 cookies. The greed factors of 2
# children are 1, 2.
# You have 3 cookies and their sizes are big enough to gratify all of the
# children,
# You need to output 2.
#
#
#
# Constraints:
#
#
# 1 <= g.length <= 3 * 10^4
# 0 <= s.length <= 3 * 10^4
# 1 <= g[i], s[j] <= 2^31 - 1
#
#
#
from typing import List


# @lc code=start
class Solution:
    # O(m*log(m)+n*log(n)+min(m,n)), O(m+n). Greedy
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi, si = len(g) - 1, len(s) - 1
        res = 0
        while gi >= 0 and si >= 0:
            if g[gi] <= s[si]:
                res += 1
                si -= 1
            gi -= 1
        return res


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1], []], 0),
            ([[1, 2], [1, 2, 3]], 2),
            ([[1, 2, 3], [1, 1]], 1),
            ([[2, 3], [1, 1]], 0),
            ([[1, 2], [1]], 1),
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
