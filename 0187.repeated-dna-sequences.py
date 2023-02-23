#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (42.13%)
# Likes:    1398
# Dislikes: 358
# Total Accepted:    223.2K
# Total Submissions: 524.1K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A',
# 'C', 'G', and 'T'.
#
#
# For example, "ACGAATTCCG" is a DNA sequence.
#
#
# When studying DNA, it is useful to identify repeated sequences within the
# DNA.
#
# Given a string s that represents a DNA sequence, return all the
# 10-letter-long sequences (substrings) that occur more than once in a DNA
# molecule. You may return the answer in any order.
#
#
# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is either 'A', 'C', 'G', or 'T'.
#
#
#
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    # O(n), O(n)
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        bitmap = {
            "A": 0,
            "C": 1,
            "G": 2,
            "T": 3,
        }
        n = len(s)
        res = []
        counter = Counter()
        for i in range(n - 9):
            seq = 0
            for j in range(10):
                seq = seq << 2
                seq |= bitmap[s[i + j]]
            counter[seq] += 1
            if counter[seq] == 2:
                res.append(s[i:i + 10])

        return res

    # O(n), O(n)
    def findRepeatedDnaSequences1(self, s: str) -> List[str]:
        n = len(s)
        res = []
        counter = Counter()
        for i in range(n - 9):
            curr = s[i:i + 10]
            counter[curr] += 1
            if counter[curr] == 2:
                res.append(curr)

        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (["AAAAAAAAAAAAA"], ["AAAAAAAAAA"]),
            (["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"],
             ["AAAAACCCCC", "CCCCCAAAAA"]),
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
