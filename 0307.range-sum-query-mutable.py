#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (37.77%)
# Likes:    2281
# Dislikes: 125
# Total Accepted:    160.7K
# Total Submissions: 422.8K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, handle multiple queries of the following
# types:
#
#
# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right
# inclusive where left <= right.
#
#
# Implement the NumArray class:
#
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be
# val.
# int sumRange(int left, int right) Returns the sum of the elements of nums
# between indices left and right inclusive (i.e. nums[left] + nums[left + 1] +
# ... + nums[right]).
#
#
#
# Example 1:
#
#
# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]
#
# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# At most 3 * 10^4 calls will be made to update and sumRange.
#
#
#
from typing import Optional, List

# @lc code=start
from dataclasses import dataclass


@dataclass
class Node:
    start: int
    end: int
    val: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    def update(self, index: int, val: int):
        if self.start == self.end == index:
            self.val = val
            return

        assert self.left and self.right

        mid = (self.start + self.end) // 2
        if index <= mid:
            self.left.update(index, val)
        else:
            self.right.update(index, val)

        self.val = self.left.val + self.right.val

    def query(self, i: int, j: int) -> int:
        if self.start == i and self.end == j:
            return self.val

        assert self.left and self.right

        mid = (self.start + self.end)//2

        if i > mid:
            return self.right.query(i, j)
        if j <= mid:
            return self.left.query(i, j)

        return self.left.query(i, mid) + self.right.query(mid+1, j)

class NumArray:
    root: Node

    def build_tree(self, start: int, end: int, vals: List[int]) -> Node:
        if start == end:
            self.end = end
            return Node(start, end, vals[start])
        mid = (start+end)//2
        left = self.build_tree(start, mid, vals)
        right = self.build_tree(mid+1, end, vals)
        return Node(start, end, left.val + right.val, left, right)

    def __init__(self, nums: List[int]):
        self.root = self.build_tree(0, len(nums)-1, nums)

    def update(self, index: int, val: int) -> None:
        self.root.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.root.query(left, right)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

