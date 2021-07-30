#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (29.23%)
# Likes:    6551
# Dislikes: 721
# Total Accepted:    1M
# Total Submissions: 3.5M
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
#
# A valid BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#
from structures import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def isValidBST1(self, root: TreeNode) -> bool:
        def traverse(node: TreeNode):
            if node:
                yield from traverse(node.left)
                yield node.val
                yield from traverse(node.right)
        vals = traverse(root)
        prev = next(vals)
        for v in vals:
            if v <= prev:
                return False
            prev = v
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node: TreeNode, min_v: int, max_v: int) -> bool:
            if node is None:
                return True
            if min_v < node.val < max_v:
                return helper(node.left, min_v, node.val) \
                    and helper(node.right, node.val, max_v)
            return False
        return helper(root, -math.inf, math.inf)

# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([TreeNode.from_list([1])], True),
            ([TreeNode.from_list([1, 2, 3])], False),
            ([TreeNode.from_list([2, 1, 3])], True),
            ([TreeNode.from_list([5,1,4,None,None,3,6])], False),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()
