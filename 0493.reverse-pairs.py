#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#
# https://leetcode.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (27.84%)
# Likes:    1892
# Dislikes: 159
# Total Accepted:    64.1K
# Total Submissions: 225.5K
# Testcase Example:  '[1,3,2,3,1]'
#
# Given an integer array nums, return the number of reverse pairs in the
# array.
#
# A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] >
# 2 * nums[j].
#
#
# Example 1:
# Input: nums = [1,3,2,3,1]
# Output: 2
# Example 2:
# Input: nums = [2,4,3,5,1]
# Output: 3
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
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


# @lc code=start
class Solution:
    # O(n*2), O(1). TLE
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for j in range(1, n):
            for i in range(j):
                if nums[i] > 2*nums[j]:
                    res += 1
        return res

    # O(n*log(n)), O(n)
    def reversePairs1(self, nums: List[int]) -> int:
        tree = Tree()
        res = 0
        for num in nums:
            cnt = tree.count_gt(tree.root, 2*num)
            res += cnt
            tree.insert(num)
        return res

    # O(n*log(n)), O(n)
    def reversePairs2(self, nums: List[int]) -> int:
        res = 0

        def merge(left: List[int], right: List[int]) -> List[int]:
            m, n = len(left), len(right)

            new_nums = [0] * (m+n)

            i = j = k = 0
            while i < m and j < n:
                if left[i] < right[j]:
                    new_nums[k] = left[i]
                    i += 1
                else:
                    new_nums[k] = right[j]
                    j += 1
                k += 1
            while i < m:
                new_nums[k] = left[i]
                i += 1
                k += 1
            while j < n:
                new_nums[k] = right[j]
                j += 1
                k += 1

            return new_nums

        def merge_sort(nums: List[int]) -> List[int]:
            nonlocal res
            if len(nums) < 2:
                return nums

            mid = len(nums)//2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            m, n = len(left), len(right)
            i = j = 0
            while i < m and j < n:
                if left[i] <= right[j] * 2:
                    i += 1
                else:
                    res += m-i
                    j += 1

            return merge(left, right)

        merge_sort(nums)

        return res

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[1,3,2,3,1]], 2),
            ([[2,4,3,5,1]], 3),
            ([[5,4,3,2,1]], 4),
            ([[11,11,-11,-11,-11,11]], 9),
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
