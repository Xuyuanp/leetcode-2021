#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#
# https://leetcode.com/problems/count-of-range-sum/description/
#
# algorithms
# Hard (36.25%)
# Likes:    1255
# Dislikes: 137
# Total Accepted:    53.7K
# Total Submissions: 148.5K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# Given an integer array nums and two integers lower and upper, return the
# number of range sums that lie in [lower, upper] inclusive.
#
# Range sum S(i, j) is defined as the sum of the elements in nums between
# indices i and j inclusive, where i <= j.
#
#
# Example 1:
#
#
# Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their
# respective sums are: -2, -1, 2.
#
#
# Example 2:
#
#
# Input: nums = [0], lower = 0, upper = 0
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# -10^5 <= lower <= upper <= 10^5
# The answer is guaranteed to fit in a 32-bit integer.
#
#
#
from __future__ import annotations

import bisect
from collections import Counter
from dataclasses import dataclass
from typing import List, Optional


BLACK, RED = 0, 1

@dataclass
class Node:
    val: int
    count: int = 1
    total: int = 1
    color: int = RED
    left: Optional[Node] = None
    right: Optional[Node] = None
    parent: Optional[Node] = None

    def __repr__(self) -> str:
        if not self.left and not self.right:
            return f'{{ {self.val}:{self.color}:{self.count}:{self.total} }}'
        return f'{{ {self.val}:{self.color}:{self.count}:{self.total} [{self.left} {self.right}] }}'


@dataclass
class Tree:
    root: Optional[Node] = None

    def count_range(self, lower: int, upper: int) -> int:
        node = self.root
        while node:
            if upper < node.val:
                node = node.left
            elif lower > node.val:
                node = node.right
            else:
                break
        if not node:
            return 0
        return node.total - self._count_lt(node.left, lower) - self._count_gt(node.right, upper)

    def _count_lt(self, node: Optional[Node], val: int) -> int:
        while node and node.val >= val:
            node = node.left
        return node.total - self._count_gt(node.right, val-1) if node else 0

    def _count_gt(self, node: Optional[Node], val: int) -> int:
        while node and node.val <= val:
            node = node.right
        return node.total - self._count_lt(node.left, val+1) if node else 0

    def insert(self, val: int):
        parent = None
        curr = self.root
        while curr:
            parent = curr
            if val < curr.val:
                curr.total += 1
                curr = curr.left
            elif val > curr.val:
                curr.total += 1
                curr = curr.right
            else:
                curr.count += 1
                curr.total += 1
                return
        node = Node(val)
        if not parent:
            self.root = node
        elif val < parent.val:
            parent.left = node
        else:
            parent.right = node
        node.parent = parent
        self._finxup(node)

    def _left_rotate(self, node: Node):
        total = node.total
        child = node.right
        assert child
        total -= child.total
        node.right = child.left
        if child.left:
            total += child.left.total
            child.total -= child.left.total
            child.left.parent = node
        child.parent = node.parent
        if not node.parent:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child

        child.total += total
        node.total = total
        child.left = node
        node.parent = child

    def _right_rotate(self, node: Node):
        total = node.total
        child = node.left
        assert child
        total -= child.total
        node.left = child.right
        if child.right:
            total += child.right.total
            child.total -= child.right.total
            child.right.parent = node
        child.parent = node.parent
        if not node.parent:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child

        child.total += total
        child.right = node
        node.total = total
        node.parent = child

    def _finxup(self, node: Node):
        while node.parent and node.parent.color == RED:
            parent = node.parent
            assert parent
            grandp = parent.parent
            assert grandp
            is_left = node == parent.left
            parent_is_left = parent == grandp.left
            uncle = grandp.right if parent_is_left else grandp.left

            if uncle and uncle.color == RED:
                parent.color = BLACK
                uncle.color = BLACK
                grandp.color = RED
                node = grandp
                continue

            if is_left:
                if parent_is_left:
                    self._right_rotate(grandp)
                    parent.color = BLACK
                    grandp.color = RED
                else:
                    self._right_rotate(parent)
            else:
                if parent_is_left:
                    self._left_rotate(parent)
                else:
                    self._left_rotate(grandp)
                    parent.color = BLACK
                    grandp.color = RED
            node = parent

        assert self.root
        self.root.color = BLACK

# @lc code=start
class Solution:
    # O(n+L*n), O(n). L = upper-lower+1. TLE
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        res = 0
        mem = Counter()
        for csum in presum:
            for target in range(lower, upper+1):
                res += mem[csum-target]
            mem[csum] += 1
        return res

    # TODO: WTF
    def countRangeSum1(self, nums: List[int], lower: int, upper: int) -> int:
        # for i < j
        # lower <= sum(nums[i:j]) <= upper
        # lower <= presum[j] - presum[i] <= upper
        # lower + presum[i] <= presum[j] <= upper + presum[i]
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        res = 0
        temp = []
        for csum in presum[::-1]:
            left = bisect.bisect_left(temp, csum+lower)
            right = bisect.bisect_right(temp, csum+upper)
            res += right-left
            bisect.insort(temp, csum)
        return res

    # O(n*log(n)), O(n). TLE. (AC in leetcode-cn)
    def countRangeSumRBTree(self, nums: List[int], lower: int, upper: int) -> int:
        # for i < j
        # lower <= sum(nums[i:j]) <= upper
        # lower <= presum[j] - presum[i] <= upper
        # presum[j] - upper <= presum[i] <= presum[j] - upper
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        res = 0
        tree = Tree()
        for csum in presum:
            res += tree.count_range(csum-upper, csum-lower)
            tree.insert(csum)
        return res

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[0], 0, 0], 1),
            ([[-2,5,-1], -2, 2], 3),
            ([[1,2,3,4,5,6,7], 3, 8], 9),
            ([[-4,0,-3,-1,1,2,1,-4], 0, 6], 13),
            ([[-100,-100,-100,-100,-100,-100], -300, 1000], 15),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
