#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#
# https://leetcode.com/problems/132-pattern/description/
#
# algorithms
# Medium (30.66%)
# Likes:    2512
# Dislikes: 151
# Total Accepted:    92.6K
# Total Submissions: 301.9K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array of n integers nums, a 132 pattern is a subsequence of three
# integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] <
# nums[k] < nums[j].
#
# Return true if there is a 132 pattern in nums, otherwise, return false.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
#
#
# Example 2:
#
#
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
#
#
# Example 3:
#
#
# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1,
# 3, 0] and [-1, 2, 0].
#
#
#
# Constraints:
#
#
# n == nums.length
# -10^9 <= nums[i] <= 10^9
# 1 <= n <= 2 * 10^5
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(n), O(n)
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        z = float("-inf")
        for x in nums[::-1]:
            if x < z:  # x is nums[i], stack[-1] is nums[j] and z is nums[k]
                return True
            while stack and stack[-1] < x:
                z = stack.pop()
            stack.append(x)
        return False

    # brute force O(n^3), O(1)
    def find132pattern1(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([1, 2, 3, 4], False),
        ([3, 1, 4, 2], True),
        ([-1, 3, 2, 0], True),
        ([4, 5, 6, 3, 2, 1], False),
    ]
    for nums, want in cases:
        got = sol.find132pattern(nums)
        if want != got:
            print(f"Failed => args: {nums}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
