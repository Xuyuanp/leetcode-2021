#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
#
# algorithms
# Easy (45.73%)
# Likes:    771
# Dislikes: 860
# Total Accepted:    117.7K
# Total Submissions: 257K
# Testcase Example:  '["c","f","j"]\n"a"'
#
# Given a characters array letters that is sorted in non-decreasing order and a
# character target, return the smallest character in the array that is larger
# than target.
#
# Note that the letters wrap around.
#
#
# For example, if target == 'z' and letters == ['a', 'b'], the answer is
# 'a'.
#
#
#
# Example 1:
#
#
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
#
#
# Example 2:
#
#
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
#
#
# Example 3:
#
#
# Input: letters = ["c","f","j"], target = "d"
# Output: "f"
#
#
# Example 4:
#
#
# Input: letters = ["c","f","j"], target = "g"
# Output: "j"
#
#
# Example 5:
#
#
# Input: letters = ["c","f","j"], target = "j"
# Output: "c"
#
#
#
# Constraints:
#
#
# 2 <= letters.length <= 10^4
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.
#
#
#
from typing import List

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[0] if left == len(letters) else letters[left]


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([list("cfj"), "a"], "c"),
            ([list("cfj"), "c"], "f"),
            ([list("cfj"), "d"], "f"),
            ([list("cfj"), "f"], "j"),
            ([list("cfj"), "g"], "j"),
            ([list("cfj"), "j"], "c"),
            ([list("cfj"), "k"], "c"),
            ([list("abbc"), "b"], "c"),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()
