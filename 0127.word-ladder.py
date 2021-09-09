#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Hard (32.82%)
# Likes:    5890
# Dislikes: 1493
# Total Accepted:    632.7K
# Total Submissions: 1.9M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:
#
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
# be in wordList.
# sk == endWord
#
#
# Given two words, beginWord and endWord, and a dictionary wordList, return the
# number of words in the shortest transformation sequence from beginWord to
# endWord, or 0 if no such sequence exists.
#
#
# Example 1:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot"
# -> "dog" -> cog", which is 5 words long.
#
#
# Example 2:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# valid transformation sequence.
#
#
#
# Constraints:
#
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
#
#
#
import string
from collections import deque
from typing import List

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord, 1)])

        candidates = set(wordList)
        while queue:
            curr, length = queue.popleft()
            if curr == endWord:
                return length
            for i in range(len(curr)):
                for c in string.ascii_lowercase:
                    if curr[i] == c:
                        continue
                    next_word = curr[:i] + c + curr[i+1:]
                    if next_word in candidates:
                        queue.append((next_word, length+1))
                        candidates.remove(next_word)

        return 0


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            (['a', 'c', ['a', 'b', 'c']], 2),
            (['hit', 'cog', ["hot","dot","dog","lot","log","cog"]], 5),
            (['hit', 'cog', ["hot","dot","dog","lot","log"]], 0),
            (["hot", "dog", ["hot","dog","dot"]], 3),
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
