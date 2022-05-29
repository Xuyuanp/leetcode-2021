#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#
# https://leetcode.com/problems/longest-string-chain/description/
#
# algorithms
# Medium (56.31%)
# Likes:    2329
# Dislikes: 120
# Total Accepted:    135.2K
# Total Submissions: 239.6K
# Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
#
# You are given an array of words where each word consists of lowercase English
# letters.
#
# wordA is a predecessor of wordB if and only if we can insert exactly one
# letter anywhere in wordA without changing the order of the other characters
# to make it equal to wordB.
#
#
# For example, "abc" is a predecessor of "abac", while "cba" is not a
# predecessor of "bcad".
#
#
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1,
# where word1 is a predecessor of word2, word2 is a predecessor of word3, and
# so on. A single word is trivially a word chain with k == 1.
#
# Return the length of the longest possible word chain with words chosen from
# the given list of words.
#
#
# Example 1:
#
#
# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
#
#
# Example 2:
#
#
# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
# Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc",
# "pcxbc", "pcxbcf"].
#
#
# Example 3:
#
#
# Input: words = ["abcd","dbqca"]
# Output: 1
# Explanation: The trivial word chain ["abcd"] is one of the longest word
# chains.
# ["abcd","dbqca"] is not a valid word chain because the ordering of the
# letters is changed.
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of lowercase English letters.
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(l*n^2), O(n). l = max of len(word)) in words
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=lambda w: len(w))

        def is_pred(w1: str, w2: str) -> bool:
            if len(w1) + 1 != len(w2):
                return False
            i = j = 0
            count = 0
            while i < len(w1) and j < len(w2):
                if w1[i] == w2[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    count += 1

            return count <= 1

        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if is_pred(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # O(n*l^2), O(n)
    def longestStrChain1(self, words: List[str]) -> int:
        words.sort(key=lambda w: len(w))

        dp = {w: 1 for w in words}

        for word in words:
            for i in range(len(word)):
                pre = word[:i] + word[i + 1 :]
                if pre in dp:
                    dp[word] = max(dp[word], dp[pre] + 1)

        return max(dp.values())


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([["a", "b", "ba", "bca", "bda", "bdca"]], 4),
            ([["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]], 5),
            ([["abcd", "dbqca"]], 1),
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
