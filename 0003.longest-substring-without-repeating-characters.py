#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (31.86%)
# Likes:    15734
# Dislikes: 778
# Total Accepted:    2.3M
# Total Submissions: 7.3M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
# Example 4:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#

# @lc code=start


class Solution:
    # O(n), O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        res = start = 0
        for i, c in enumerate(s):
            if c in last_seen and start <= last_seen[c]:
                start = last_seen[c] + 1
            else:
                res = max(res, i - start + 1)
            last_seen[c] = i
        return res


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ("", 0),
        ("a", 1),
        ("ab", 2),
        ("abc", 3),
        ("bbbbb", 1),
        ("pwwwkew", 3),
        ("abcabcbb", 3),
    ]
    for s, want in cases:
        got = sol.lengthOfLongestSubstring(s)
        if want != got:
            print(f"Failed => args: {s}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
