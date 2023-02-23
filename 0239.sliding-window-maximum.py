#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (45.18%)
# Likes:    6436
# Dislikes: 245
# Total Accepted:    420.3K
# Total Submissions: 930.1K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
#
# Return the max sliding window.
#
#
# Example 1:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# Example 2:
#
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Example 3:
#
#
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
#
#
# Example 4:
#
#
# Input: nums = [9,11], k = 2
# Output: [11]
#
#
# Example 5:
#
#
# Input: nums = [4,-2], k = 2
# Output: [4]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#
from collections import deque
from typing import List

# @lc code=start


class Queue:

    def __init__(self):
        self._data = deque()

    def push(self, x):
        while self._data and self._data[-1] < x:
            self._data.pop()
        self._data.append(x)

    def max(self):
        return self._data[0]

    def pop(self, x):
        if self._data and self._data[0] == x:
            self._data.popleft()


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        queue = Queue()

        for i in range(k - 1):
            queue.push(nums[i])

        for i in range(k - 1, len(nums)):
            queue.push(nums[i])
            res.append(queue.max())
            queue.pop(nums[i - k + 1])

        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1], 1], [1]),
            ([[1, -1], 1], [1, -1]),
            ([[9, 11], 2], [11]),
            ([[4, -2], 2], [4]),
            ([[1, 3, -1, -3, 5, 3, 6, 7], 3], [3, 3, 5, 5, 6, 7]),
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
