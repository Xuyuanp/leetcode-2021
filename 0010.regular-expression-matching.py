#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (27.68%)
# Likes:    6473
# Dislikes: 920
# Total Accepted:    577K
# Total Submissions: 2.1M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string s and a pattern p, implement regular expression
# matching with support for '.' and '*' where:
#
#
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
#
# Example 1:
#
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Example 4:
#
#
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore,
# it matches "aab".
#
#
# Example 5:
#
#
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 20
# 1 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
#
#
#

# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def match_single(c: str, cp: str) -> bool:
            return cp == "." or c == cp

        def is_match(i: int, j: int) -> bool:
            if j == n:
                return i == m

            cp = p[j]
            if j + 1 < n and p[j + 1] == "*":
                while i < m:
                    if is_match(i, j + 2):
                        return True
                    if not match_single(s[i], cp):
                        return False
                    i += 1
                return is_match(i, j + 2)

            if i < m and match_single(s[i], cp):
                return is_match(i + 1, j + 1)

            return False

        return is_match(0, 0)

    # O(m*n), O(m*n)
    def isMatch1(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = i < m and (s[i] == p[j] or p[j] == ".")
                if j + 1 < n and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]

    def isMatch2(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def match_single(c: str, cp: str) -> bool:
            return cp == "." or c == cp

        def is_match(i: int, j: int) -> bool:
            if j < 0:
                return i < 0

            if p[j] == "*":
                return is_match(i, j - 1)

            if j + 1 < n and p[j + 1] == "*":
                if is_match(i, j - 1):
                    return True
                if i < 0 or not match_single(s[i], p[j]):
                    return False
                return is_match(i - 1, j)

            if i >= 0 and match_single(s[i], p[j]):
                return is_match(i - 1, j - 1)

            return False

        return is_match(m - 1, n - 1)

    # O(m*n), O(m*n)
    def isMatch3(self, s: str, p: str) -> bool:
        def match_single(c: str, cp: str) -> bool:
            return cp == "." or c == cp

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(2, n + 1):
            dp[0][j] = p[j - 1] == "*" and dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = (
                        dp[i][j - 2]
                        or match_single(s[i - 1], p[j - 2])
                        and dp[i - 1][j]
                    )
                else:
                    dp[i][j] = dp[i - 1][j - 1] and match_single(s[i - 1], p[j - 1])

        return dp[m][n]

    # O(m*n), O(n)
    def isMatch4(self, s: str, p: str) -> bool:
        def match_single(c: str, cp: str) -> bool:
            return cp == "." or c == cp

        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(2, n + 1):
            dp[j] = p[j - 1] == "*" and dp[j - 2]

        for i in range(1, m + 1):
            next_dp = [False] * (n + 1)
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    next_dp[j] = (
                        next_dp[j - 2] or match_single(s[i - 1], p[j - 2]) and dp[j]
                    )
                else:
                    next_dp[j] = dp[j - 1] and match_single(s[i - 1], p[j - 1])
            dp = next_dp

        return dp[n]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (["a", ".*..a*"], False),
            (["a", "ab*"], True),
            (["aa", "a"], False),
            (["aa", "a*"], True),
            (["ab", ".*"], True),
            (["ab", ".*c"], False),
            (["abc", ".*c"], True),
            (["aaa", "a*a"], True),
            (["aaa", "aaaa"], False),
            (["aab", "c*a*b"], True),
            (["bbbba", ".*a*a"], True),
            (["mississippi", "mis*is*p*"], False),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
