#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (26.77%)
# Likes:    1452
# Dislikes: 1601
# Total Accepted:    220K
# Total Submissions: 813.9K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string s and an array of strings words of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of
# each word in words exactly once, in any order, and without any intervening
# characters.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
#
#
# Example 2:
#
#
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
#
#
# Example 3:
#
#
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of lower-case English letters.
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] consists of lower-case English letters.
#
#
#
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    # O(n*m), O(m)
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, m, k = len(s), len(words), len(words[0])
        counter = Counter(words)
        res = []
        for start in range(n - m * k + 1):
            if s[start:start + k] not in counter:
                continue
            window = Counter(counter)
            required = len(counter)
            for i in range(start, start + m * k, k):
                curr = s[i:i + k]
                if not window[curr]:
                    break
                window[curr] -= 1
                if window[curr] == 0:
                    required -= 1
                if required == 0:
                    res.append(start)
                    break

        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (["barfoothefoobarman", ["foo", "bar"]], [0, 9]),
            (["wordgoodgoodgoodbestword", ["word", "good", "best",
                                           "word"]], []),
            (["barfoofoobarthefoobarman", ["bar", "foo", "the"]], [6, 9, 12]),
        ]
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
