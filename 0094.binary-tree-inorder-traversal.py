#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (67.29%)
# Likes:    5096
# Dislikes: 222
# Total Accepted:    1M
# Total Submissions: 1.5M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the inorder traversal of its nodes'
# values.
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
# Example 4:
#
#
# Input: root = [1,2]
# Output: [2,1]
#
#
# Example 5:
#
#
# Input: root = [1,null,2]
# Output: [1,2]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
from collections import deque
from typing import List

from structures import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def traverse(node: TreeNode):
            if node:
                yield from traverse(node.left)
                yield node.val
                yield from traverse(node.right)

        return list(traverse(root))

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        res = []

        stack = deque()

        current = root  # root of the current sub stree
        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            res.append(current.val)

            current = current.right

        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[]], []),
            ([[1]], [1]),
            ([[1, 2]], [2, 1]),
            ([[1, 2, 3]], [2, 1, 3]),
            ([[1, None, 2]], [1, 2]),
            ([[1, None, 2, 3]], [1, 3, 2]),
        ]
        for args, want in cases:
            got = func(TreeNode.from_list(*args))
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
# if __name__ == '__main__':
#     sol = Solution()
#     cases = [
#         ([], []),
#         ([1], [1]),
#         ([1,2], [2,1]),
#         ([1,2,3], [2,1,3]),
#         ([1,None,2], [1, 2]),
#         ([1,None,2,3], [1,3,2]),
#     ]
#     for args, want in cases:
#         got = sol.inorderTraversal(TreeNode.from_list(args))
#         if want != got:
#             print(f'Failed => args: {args}; want: {want}, but got: {got}')
#             break
#     else:
#         print('All Passed')
#
