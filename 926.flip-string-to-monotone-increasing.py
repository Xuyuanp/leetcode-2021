#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#
# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
#
# algorithms
# Medium (53.78%)
# Likes:    831
# Dislikes: 26
# Total Accepted:    28.9K
# Total Submissions: 53.6K
# Testcase Example:  '"00110"'
#
# A string of '0's and '1's is monotone increasing if it consists of some
# number of '0's (possibly 0), followed by some number of '1's (also possibly
# 0.)
#
# We are given a string s of '0's and '1's, and we may flip any '0' to a '1' or
# a '1' to a '0'.
#
# Return the minimum number of flips to make s monotone increasing.
#
#
#
#
# Example 1:
#
#
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
#
#
#
# Example 2:
#
#
# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
#
#
#
# Example 3:
#
#
# Input: s = "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
#
#
#
#
# Note:
#
#
# 1 <= s.length <= 20000
# s only consists of '0' and '1' characters.
#
#
#
#
#
#

# @lc code=start
class Solution:
    # O(n), O(1)
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = flips = 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                flips += 1
            flips = min(ones, flips)
        return flips

    # O(n), O(n)
    def minFlipsMonoIncr2(self, s: str) -> int:
        n = len(s)
        ones = [0] * (n+1) # ones[i]: nums of '1' in [0, i)
        for i in range(n):
            ones[i+1] = ones[i] + int(s[i])

        ans = min(
            ones[i] +                                      # nums of '1' at left
            n - i - (ones[-1] - ones[i]) -1 + int(s[i])    # nums of '0' at right
            for i in range(n))

        return ans


    # O(n), O(n)
    def minFlipsMonoIncr1(self, s: str) -> int:
        l = [0] * len(s) # l[i]: nums of '1' at the left  of s[i]
        r = [0] * len(s) # r[i]: nums of '0' at the right of s[i]
        # l[i] + r[i] is the total flips at s[i]
        n = len(s)
        for i in range(1, n):
            l[i] = l[i-1] + (1 if s[i-1] == '1' else 0)
            r[n-i-1] = r[n-i] + (1 if s[n-i] == '0' else 0)

        return min(l[i] + r[i] for i in range(n))

# @lc code=end

if __name__ == "__main__":
    print(Solution().minFlipsMonoIncr('00011000'))
    print(Solution().minFlipsMonoIncr('00110'))
    print(Solution().minFlipsMonoIncr('010110'))
    print(Solution().minFlipsMonoIncr('11011'))
