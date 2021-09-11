#
# @lc app=leetcode id=1147 lang=python3
#
# [1147] Longest Chunked Palindrome Decomposition
#
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/description/
#
# algorithms
# Hard (59.76%)
# Likes:    337
# Dislikes: 20
# Total Accepted:    14.2K
# Total Submissions: 23.6K
# Testcase Example:  '"ghiabcdefhelloadamhelloabcdefghi"'
#
# You are given a string text. You should split it to k substrings (subtext1,
# subtext2, ..., subtextk) such that:
#
#
# subtexti is a non-empty string.
# The concatenation of all the substrings is equal to text (i.e., subtext1 +
# subtext2 + ... + subtextk == text).
# subtexti == subtextk - i + 1 for all valid values of i (i.e., 1 <= i <= k).
#
#
# Return the largest possible value of k.
#
#
# Example 1:
#
#
# Input: text = "ghiabcdefhelloadamhelloabcdefghi"
# Output: 7
# Explanation: We can split the string on
# "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
#
#
# Example 2:
#
#
# Input: text = "merchant"
# Output: 1
# Explanation: We can split the string on "(merchant)".
#
#
# Example 3:
#
#
# Input: text = "antaprezatepzapreanta"
# Output: 11
# Explanation: We can split the string on
# "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
#
#
# Example 4:
#
#
# Input: text = "aaa"
# Output: 3
# Explanation: We can split the string on "(a)(a)(a)".
#
#
#
# Constraints:
#
#
# 1 <= text.length <= 1000
# text consists only of lowercase English characters.
#
#
#

# @lc code=start
class Solution:
    # O(n^2), O(1)
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        start = left = 0
        end = right = n-1
        res = 0
        while left < right:
            if text[start:left+1] == text[right:end+1]:
                res += 2
                start = left + 1
                end = right - 1
            left += 1
            right -= 1
        return res + (1 if start <= end else 0)

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            [["aba"], 3],
            [["aaa"], 3],
            [["elvtoelvto"], 2],
            [["ghiabcdefhelloadamhelloabcdefghi"], 7],
            [["merchant"], 1],
            [["antaprezatepzapreanta"], 11],
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
