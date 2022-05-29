#
# @lc app=leetcode id=2014 lang=python3
#
# [2014] Longest Subsequence Repeated k Times
#
# https://leetcode.com/problems/longest-subsequence-repeated-k-times/description/
#
# algorithms
# Hard (51.63%)
# Likes:    95
# Dislikes: 42
# Total Accepted:    2.4K
# Total Submissions: 4.7K
# Testcase Example:  '"letsleetcode"\n2'
#
# You are given a string s of length n, and an integer k. You are tasked to
# find the longest subsequence repeated k times in string s.
#
# A subsequence is a string that can be derived from another string by deleting
# some or no characters without changing the order of the remaining
# characters.
#
# A subsequence seq is repeated k times in the string s if seq * k is a
# subsequence of s, where seq * k represents a string constructed by
# concatenating seq k times.
#
#
# For example, "bba" is repeated 2 times in the string "bababcba", because the
# string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence
# of the string "bababcba".
#
#
# Return the longest subsequence repeated k times in string s. If multiple such
# subsequences are found, return the lexicographically largest one. If there is
# no such subsequence, return an empty string.
#
#
# Example 1:
#
#
# Input: s = "letsleetcode", k = 2
# Output: "let"
# Explanation: There are two longest subsequences repeated 2 times: "let" and
# "ete".
# "let" is the lexicographically largest one.
#
#
# Example 2:
#
#
# Input: s = "bb", k = 2
# Output: "b"
# Explanation: The longest subsequence repeated 2 times is "b".
#
#
# Example 3:
#
#
# Input: s = "ab", k = 2
# Output: ""
# Explanation: There is no subsequence repeated 2 times. Empty string is
# returned.
#
#
# Example 4:
#
#
# Input: s = "bbabbabbbbabaababab", k = 3
# Output: "bbbb"
# Explanation: The longest subsequence "bbbb" is repeated 3 times in
# "bbabbabbbbabaababab".
#
#
#
# Constraints:
#
#
# n == s.length
# 2 <= n, k <= 2000
# 2 <= n < k * 8
# s consists of lowercase English letters.
#
#
#

# @lc code=start
from collections import deque


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = [0] * 26
        orda = ord("a")
        for c in s:
            freq[ord(c) - orda] += 1

        candidates = [chr(i + 97) for i, f in enumerate(freq) if f >= k]

        # O(n)
        def is_k_subseq(ss: str) -> bool:
            i = cnt = 0
            for c in s:
                if ss[i] != c:
                    continue
                i += 1
                if i != len(ss):
                    continue
                cnt += 1
                if cnt == k:
                    return True
                i = 0

            return False

        queue = deque()
        queue.append("")
        res = ""
        while queue:
            ss = queue.popleft()
            for c in candidates:
                new_ss = ss + c
                if is_k_subseq(new_ss):
                    res = new_ss
                    queue.append(new_ss)
        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (["ab", 2], ""),
            (["bb", 2], "b"),
            (["letsleetcode", 2], "let"),
            (["bbabbabbbbabaababab", 3], "bbbb"),
            (
                [
                    "exhmepeeeeeekeeetelqyeeeeudtdsjeeyeweeeeekqeizesieqnddzeaefqeyeeezesxfreveeeeyeeeseregoneiftemerujfveysezkeeiofsbeeerheueeehedkluoedeeemeweeekeefeqaleb",
                    65,
                ],
                "e",
            ),
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
