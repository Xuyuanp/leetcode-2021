#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (42.49%)
# Likes:    7674
# Dislikes: 359
# Total Accepted:    834.5K
# Total Submissions: 2M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
#
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
#
#
from functools import lru_cache
from typing import List

# @lc code=start
class Solution:
    # O(n^2), O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)

        @lru_cache(None)
        def word_break(s: str) -> bool:
            if s in wd:
                return True
            for i in range(1, len(s)):
                if s[:i] in wd and word_break(s[i:]):
                    return True
            return False

        return word_break(s)

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)
        mem = {}

        def word_break(s: str) -> bool:
            if s in mem:
                return mem[s]
            if s in wd:
                mem[s] = True
                return True
            for i in range(1, len(s)):
                if s[:i] in wd and word_break(s[i:]):
                    mem[s] = True
                    return True
            mem[s] = False
            return False

        return word_break(s)

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)

        @lru_cache(None)
        def word_break(start: int) -> bool:
            print(start)
            if s[start:] in wd:
                return True
            for i in range(start + 1, len(s)):
                if s[start:i] in wd and word_break(i):
                    return True
            return False

        return word_break(0)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (["abc", ["ab", "bc"]], False),
            (["abcd", ["ab", "cd", "de"]], True),
            (["leetcode", ["leet", "code"]], True),
            (["applepenapple", ["apple", "pen"]], True),
            (["catsandog", ["cats", "dog", "sand", "and", "cat"]], False),
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
