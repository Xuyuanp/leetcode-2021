#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
# https://leetcode.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (66.58%)
# Likes:    150
# Dislikes: 16
# Total Accepted:    230.9K
# Total Submissions: 346.8K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
# The next greater element of some element x in an array is the first greater
# element that is to the right of x in the same array.
#
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where
# nums1 is a subset of nums2.
#
# For each 0 <= i < nums1.length, find the index j such that nums1[i] ==
# nums2[j] and determine the next greater element of nums2[j] in nums2. If
# there is no next greater element, then the answer for this query is -1.
#
# Return an array ans of length nums1.length such that ans[i] is the next
# greater element as described above.
#
#
# Example 1:
#
#
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so
# the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so
# the answer is -1.
#
#
# Example 2:
#
#
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so
# the answer is -1.
#
#
#
# Constraints:
#
#
# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 10^4
# All integers in nums1 and nums2 are unique.
# All the integers of nums1 also appear in nums2.
#
#
#
# Follow up: Could you find an O(nums1.length + nums2.length) solution?
#
from typing import List

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = [float('inf')]
        dic = {}
        for n in nums2:
            while stack[-1] < n:
                dic[stack.pop()] = n
            stack.append(n)

        for i, n in enumerate(nums1):
            res[i] = dic.get(n, -1)

        return res

# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    cases = [
        (([], []), []),
        (([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1]),
        (([2, 4], [1, 2, 3, 4]), [3, -1]),
    ]
    for (nums1, nums2), want in cases:
        got = sol.nextGreaterElement(nums1, nums2)
        if want != got:
            print(f'Failed => args: {(nums1, nums2)}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
