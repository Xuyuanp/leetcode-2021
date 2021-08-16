#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (36.72%)
# Likes:    7604
# Dislikes: 477
# Total Accepted:    585.8K
# Total Submissions: 1.6M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
#
# The testcases will be generated such that the answer is unique.
#
# A substring is a contiguous sequence of characters within the string.
#
#
# Example 1:
#
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
#
#
# Example 2:
#
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
#
# Example 3:
#
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
#
# Constraints:
#
#
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
#
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    # O(m+n), O(max number of letters). sliding window
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        win_counter = defaultdict(int)
        matched, required = 0, len(counter)
        res = ''
        left = right = 0
        for right, c in enumerate(s):
            if c not in counter:
                continue

            win_counter[c] += 1
            if counter[c] == win_counter[c]:
                matched+=1

            while matched == required and left <= right:
                c = s[left]
                if c in counter:
                    if not res or right-left+1 < len(res):
                        res = s[left:right+1]

                    win_counter[c]-=1
                    if win_counter[c] < counter[c]:
                        matched-=1

                left += 1

        return res

    # O(m+n), O(number of unique letters in t). sliding window
    def minWindow1(self, s: str, t: str) -> str:
        counter = Counter(t)
        required = len(counter)
        res = ''
        left = 0
        for right, char in enumerate(s, 1):
            if char not in counter:
                continue

            counter[char] -= 1
            if counter[char] == 0:
                required -= 1

            while required == 0 and left < right:
                # when required == 0, counter[<any letter>] <= 0
                char = s[left]
                if char in counter:
                    if not res or right-left < len(res):
                        res = s[left:right]

                    counter[char] += 1
                    if counter[char] == 1:
                        required += 1

                left += 1

        return res

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            (['a', 'aa'], ''),
            (['a', 'a'], 'a'),
            (['ADOBECODEBANC', 'ABC'], 'BANC'),
            (['aABCDEFGz', 'az'], 'aABCDEFGz'),
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
