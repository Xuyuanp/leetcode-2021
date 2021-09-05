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
    color: int = 1
    left: Optional['Node'] = None
    right: Optional['Node'] = None


class Tree:
    root: Optional[Node] = None

    def count_lt(self, node: Optional[Node], val: int) -> int:
        while node and node.val >= val:
            node = node.left
        return node.total - self.count_gt(node.right, val-1) if node else 0

    def count_gt(self, node: Optional[Node], val: int) -> int:
        while node and node.val <= val:
            node = node.right
        return node.total - self.count_lt(node.left, val+1) if node else 0

    def insert(self, val: int):
        self.root = self._insert(val, self.root, None)
        self.root.color = BLACK

    def _insert(self, val: int, node: Optional[Node], parent: Optional[Node]) -> Node:
        if not node:
            child = Node(val)
        elif val < node.val:
            node.total += 1
            node.left = self._insert(val, node.left, node)
            child = node.left
        elif val > node.val:
            node.total += 1
            node.right = self._insert(val, node.right, node)
            child = node.right
        else:
            node.total += 1
            node.count += 1
            return node

        return self._fixup(child, node, parent)

    def _fixup(self, child: Node, parent: Optional[Node], grandp: Optional[Node]) -> Node:
        if child.color == BLACK and parent:
            return parent
        if not parent:
            return child

        is_left = child == parent.left

        if parent.color == BLACK:
            if is_left and child.left and child.left.color == RED:
                parent.color = RED
                child.color = BLACK
                self._right_rotate(child, parent)
            elif not is_left and child.right and child.right.color == RED:
                parent.color = RED
                child.color = BLACK
                self._left_rotate(child, parent)
            else:
                child = parent
            return child

        assert child.color == parent.color == RED
        assert grandp and grandp.color == BLACK

        parent_is_left = parent == grandp.left
        uncle = grandp.right if parent_is_left else grandp.left

        if uncle and uncle.color == RED:
            parent.color = BLACK
            uncle.color = BLACK
            grandp.color = RED
            return parent

        if is_left and not parent_is_left:
            self._right_rotate(child, parent)
        elif not is_left and parent_is_left:
            self._left_rotate(child, parent)
        else:
            child = parent
        return child

    def _left_rotate(self, child: Node, parent: Node):
        bak = child.left.total if child.left else 0
        parent.right = child.left
        child.left = parent

        parent.total -= child.total
        child.total -= bak
        parent.total += bak
        child.total += parent.total

    def _right_rotate(self, child: Node, parent: Node):
        bak = child.right.total if child.right else 0
        parent.left = child.right
        child.right = parent

        parent.total -= child.total
        child.total -= bak
        parent.total += bak
        child.total += parent.total

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
        return node.total - self.count_lt(node.left, lower) - self.count_gt(node.right, upper)

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

    # O(n*log(n)), O(n)
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


# go RBTree solution AC
#
#
# type Color int
#
# const (
# 	Red Color = iota
# 	Black
# )
#
# type Node struct {
# 	val   int
# 	color Color
# 	count int
# 	total int
#
# 	parent *Node
# 	left   *Node
# 	right  *Node
# }
#
# func newNode(val int) *Node {
# 	return &Node{
# 		val:   val,
# 		color: Red,
# 		count: 1,
# 		total: 1,
# 	}
# }
#
# type Tree struct {
# 	root *Node
# }
#
# func (t *Tree) insert(val int) {
# 	var parent *Node
# 	curr := t.root
# 	for curr != nil {
# 		parent = curr
# 		curr.total++
# 		if val < curr.val {
# 			curr = curr.left
# 		} else if val > curr.val {
# 			curr = curr.right
# 		} else {
# 			curr.count++
# 			return
# 		}
# 	}
# 	node := newNode(val)
# 	if parent == nil {
# 		t.root = node
# 	} else if parent.val < val {
# 		parent.right = node
# 	} else {
# 		parent.left = node
# 	}
# 	node.parent = parent
#
# 	t.fixup(node)
# }
#
# func (t *Tree) fixup(node *Node) {
# 	for node.parent != nil && node.parent.color == Red {
# 		parent := node.parent
# 		isLeft := node == parent.left
# 		grandp := parent.parent
# 		parentIsLeft := parent == grandp.left
#
# 		uncle := grandp.left
# 		if parentIsLeft {
# 			uncle = grandp.right
# 		}
#
# 		if uncle != nil && uncle.color == Red {
# 			uncle.color = Black
# 			parent.color = Black
# 			grandp.color = Red
#
# 			node = grandp
# 			continue
# 		}
#
# 		if isLeft {
# 			if parentIsLeft {
# 				t.rightRotate(grandp)
# 				parent.color = Black
# 				grandp.color = Red
# 			} else {
# 				t.rightRotate(parent)
# 			}
# 		} else {
# 			if parentIsLeft {
# 				t.leftRotate(parent)
# 			} else {
# 				t.leftRotate(grandp)
# 				parent.color = Black
# 				grandp.color = Red
# 			}
# 		}
#
# 		node = parent
# 	}
# 	t.root.color = Black
# }
#
# func (t *Tree) leftRotate(node *Node) {
# 	child := node.right
# 	total := node.total
#
# 	total -= child.total
#
# 	node.right = child.left
# 	if child.left != nil {
# 		child.total -= child.left.total
# 		total += child.left.total
# 		child.left.parent = node
# 	}
# 	child.parent = node.parent
# 	if node.parent == nil {
# 		t.root = child
# 	} else if node == node.parent.left {
# 		node.parent.left = child
# 	} else {
# 		node.parent.right = child
# 	}
#
# 	child.left = node
# 	node.parent = child
#
# 	child.total += total
# 	node.total = total
# }
#
# func (t *Tree) rightRotate(node *Node) {
# 	child := node.left
# 	total := node.total
#
# 	total -= child.total
#
# 	node.left = child.right
# 	if child.right != nil {
# 		child.total -= child.right.total
# 		total += child.right.total
# 		child.right.parent = node
# 	}
# 	child.parent = node.parent
# 	if node.parent == nil {
# 		t.root = child
# 	} else if node == node.parent.left {
# 		node.parent.left = child
# 	} else {
# 		node.parent.right = child
# 	}
#
# 	child.right = node
# 	node.parent = child
#
# 	child.total += total
# 	node.total = total
# }
#
# func (t *Tree) countRange(lower int, upper int) int {
# 	node := t.root
# 	for node != nil {
# 		if upper < node.val {
# 			node = node.left
# 		} else if lower > node.val {
# 			node = node.right
# 		} else {
# 			break
# 		}
# 	}
# 	if node == nil {
# 		return 0
# 	}
# 	return node.total - t.countLT(node.left, lower) - t.countGT(node.right, upper)
# }
#
# func (t *Tree) countLT(node *Node, val int) int {
# 	for node != nil && node.val >= val {
# 		node = node.left
# 	}
# 	if node == nil {
# 		return 0
# 	}
# 	return node.total - t.countGT(node.right, val-1)
# }
#
# func (t *Tree) countGT(node *Node, val int) int {
# 	for node != nil && node.val <= val {
# 		node = node.right
# 	}
# 	if node == nil {
# 		return 0
# 	}
# 	return node.total - t.countLT(node.left, val+1)
# }
#
#
# func countRangeSum(nums []int, lower int, upper int) int {
#     presum := make([]int, len(nums)+1)
# 	for i := 1; i < len(nums)+1; i++ {
# 		presum[i] = presum[i-1] + nums[i-1]
# 	}
#
# 	res := 0
# 	tree := &Tree{}
# 	for _, csum := range presum {
# 		res += tree.countRange(csum-upper, csum-lower)
# 		tree.insert(csum)
# 	}
#     return res
# }
