#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (52.40%)
# Likes:    12668
# Dislikes: 183
# Total Accepted:    802K
# Total Submissions: 1.5M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#
# Constraints:
#
#
# n == height.length
# 0 <= n <= 3 * 10^4
# 0 <= height[i] <= 10^5
#
#
#
from collections import deque
from typing import List


# @lc code=start
class Solution:
    # O(n), O(1)
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res

    # O(n), O(n)
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        res = 0
        stack = deque()
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(h, height[stack[-1]]) - height[top]
                res += distance * bounded_height
            stack.append(i)

        return res

    # O(n), O(n)
    def trap1(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        left_max, right_max = [0] * n, [0] * n
        left_max[0], right_max[n - 1] = height[0], height[n - 1]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
            right_max[n - i - 1] = max(right_max[n - i], height[n - i - 1])
        return sum(
            min(left_max[i], right_max[i]) - height[i]
            for i in range(1, n - 1))


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([3, 2, 1, 0, 1], 1),
        ([3, 2, 1, 0, 1, 2], 4),
        ([3, 2, 1, 0, 1, 2, 3], 9),
        ([3, 2, 1, 0, 1, 2, 3, 4], 9),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 0, 1], 1),
        ([1, 0, 2], 1),
        ([2, 0, 1], 1),
        ([], 0),
        ([2, 0, 1, 1, 0, 2], 6),
    ]
    for height, want in cases:
        got = sol.trap(height)
        if got != want:
            print(f"Failed => args: {height}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
