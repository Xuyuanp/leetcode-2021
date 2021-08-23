#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence
#
# https://leetcode.com/problems/shortest-common-supersequence/description/
#
# algorithms
# Hard (54.05%)
# Likes:    1413
# Dislikes: 32
# Total Accepted:    30.9K
# Total Submissions: 56.6K
# Testcase Example:  '"abac"\n"cab"'
#
# Given two strings str1 and str2, return the shortest string that has both
# str1 and str2 as subsequences. If there are multiple valid strings, return
# any of them.
#
# A string s is a subsequence of string t if deleting some number of characters
# from t (possibly 0) results in the string s.
#
#
# Example 1:
#
#
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation:
# str1 = "abac" is a subsequence of "cabac" because we can delete the first
# "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these
# properties.
#
#
# Example 2:
#
#
# Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
# Output: "aaaaaaaa"
#
#
#
# Constraints:
#
#
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.
#
#
#

# @lc code=start
from collections import deque


class Solution:
    # O(m*n), O(m*n). find the longest common subsequence and fill the extra chars
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        res = deque()
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                i -= 1
                j -= 1
                res.appendleft(str1[i])
            elif dp[i-1][j] == dp[i][j]:
                i -= 1
                res.appendleft(str1[i])
            elif dp[i][j-1] == dp[i][j]:
                j -= 1
                res.appendleft(str2[j])

        while i > 0:
            i -= 1
            res.appendleft(str1[i])
        while j > 0:
            j -= 1
            res.appendleft(str2[j])

        return ''.join(res)

# @lc code=end

def is_shortest_common_supersequence(scs: str, str1: str, str2: str) -> bool:
    m, n = len(str1), len(str2)
    i = j = 0
    for c in scs:
        if i < m and j < n and c == str1[i] == str2[j]:
            i += 1
            j += 1
        elif i < m and c == str1[i]:
            i += 1
        elif j < n and c == str2[j]:
            j += 1
        else:
            return False
    return i == m and j == n

def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            (['a', 'b']),
            (['abac', 'cab']),
            (['aaaaaaaa', 'aaaaaaaa']),
            (['bbbaaaba', 'bbababbb']),
            (['atdznrqfwlfbcqkezrltzyeqvqemikzgghxkzenhtapwrmrovwtpzzsyiwongllq',
              'xjtuwbmvsdeogmnzorndhmjoqnqjnhmfueifqwleggctttilmfokpgotfykyzdhf']),
        ]
        for args in cases:
            got = func(*args)
            str1, str2 = args
            if not is_shortest_common_supersequence(got, str1, str2):
                print(f"  Failed => args: {args}; got: '{got}' not the shortest common supersequence")
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
