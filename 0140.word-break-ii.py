#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (36.93%)
# Likes:    3740
# Dislikes: 453
# Total Accepted:    362.7K
# Total Submissions: 950.4K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a string s and a dictionary of strings wordDict, add spaces in s to
# construct a sentence where each word is a valid dictionary word. Return all
# such possible sentences in any order.
#
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
#
#
# Example 1:
#
#
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
#
#
# Example 2:
#
#
# Input: s = "pineapplepenapple", wordDict =
# ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
#
#
from functools import cache
from typing import List

# @lc code=start
class Solution:
    # O(n^2), O(n^2)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)

        def dfs(curr: str, sentence: List[str]):
            if curr == '':
                res.append(' '.join(sentence))

            for i in range(1, len(curr)+1):
                if curr[:i] in wordDict:
                    sentence.append(curr[:i])
                    dfs(curr[i:], sentence)
                    sentence.pop(-1)

        dfs(s, [])

        return res

    def wordBreak2(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def dfs(curr: str, sentence: List[str]):
            if curr == '':
                res.append(' '.join(sentence))

            for word in wordDict:
                if curr.startswith(word):
                    sentence.append(word)
                    dfs(curr[len(word):], sentence)
                    sentence.pop(-1)

        dfs(s, [])

        return res

    def wordBreak3(self, s: str, wordDict: List[str]) -> List[str]:
        @cache
        def dfs(curr: str) -> List[str]:
            res = []
            if curr == '':
                return ['']
            for word in wordDict:
                if curr.startswith(word):
                    for suffix in dfs(curr[len(word):]):
                        if suffix:
                            res.append(word+' '+suffix)
                        else:
                            res.append(word)
            return res

        return dfs(s)

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            (['catsanddog', ["cat","cats","and","sand","dog"]], ["cats and dog","cat sand dog"]),
            (['pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple']], ["pine apple pen apple","pineapple pen apple","pine applepen apple"]),
            (['catsandog', ['cats', 'dog', 'sand', 'and', 'cat']], []),
        ]
        for args, want in cases:
            got = func(*args)
            if sorted(want) != sorted(got):
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
