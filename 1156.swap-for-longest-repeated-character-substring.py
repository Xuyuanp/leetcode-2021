#
# @lc app=leetcode id=1156 lang=python3
#
# [1156] Swap For Longest Repeated Character Substring
#
# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/description/
#
# algorithms
# Medium (47.09%)
# Likes:    575
# Dislikes: 52
# Total Accepted:    19.3K
# Total Submissions: 40.9K
# Testcase Example:  '"ababa"'
#
# Given a string text, we are allowed to swap two of the characters in the
# string. Find the length of the longest substring with repeated characters.
#
#
# Example 1:
#
#
# Input: text = "ababa"
# Output: 3
# Explanation: We can swap the first 'b' with the last 'a', or the last 'b'
# with the first 'a'. Then, the longest repeated character substring is "aaa",
# which its length is 3.
#
#
# Example 2:
#
#
# Input: text = "aaabaaa"
# Output: 6
# Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get
# longest repeated character substring "aaaaaa", which its length is 6.
#
#
# Example 3:
#
#
# Input: text = "aaabbaaa"
# Output: 4
#
#
# Example 4:
#
#
# Input: text = "aaaaa"
# Output: 5
# Explanation: No need to swap, longest repeated character substring is
# "aaaaa", length is 5.
#
#
# Example 5:
#
#
# Input: text = "abcdef"
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= text.length <= 20000
# text consist of lowercase English characters only.
#
#
#

# @lc code=start
from collections import defaultdict


class Solution:
    # O(n), O(1~n)
    def maxRepOpt1(self, text: str) -> int:
        mem = defaultdict(list)
        curr = text[0]
        start = 0
        for i, c in enumerate(text[1:], 1):
            if c != curr:
                mem[curr].append([start, i])
                curr = c
                start = i
        mem[curr].append([start, len(text)])

        START, END = 0, 1

        res = 1
        for segments in mem.values():
            length = len(segments)
            one_fix = 1 if length > 1 else 0
            two_fix = 1 if length > 2 else 0
            curr = segments[0]
            res = max(res, curr[END] - curr[START] + one_fix)
            for i in range(1, length):
                pre, curr = segments[i - 1], segments[i]
                res = max(res, curr[END] - curr[START] + one_fix)
                if curr[START] - pre[END] == 1:
                    res = max(res, curr[END] - pre[START] - 1 + two_fix)
        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (["abcdef"], 1),
            (["ababa"], 3),
            (["aaabaaa"], 6),
            (["aaabbaaa"], 4),
            (["aaaaa"], 5),
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
