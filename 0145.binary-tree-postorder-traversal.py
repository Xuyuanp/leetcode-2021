#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (59.24%)
# Likes:    3082
# Dislikes: 121
# Total Accepted:    552K
# Total Submissions: 914.7K
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the postorder traversal of its nodes'
# values.
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [3,2,1]
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
# Output: [2,1]
#
#
#
# Constraints:
#
#
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
from typing import Optional, List
from collections import deque

from structures import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node: Optional[TreeNode]):
            if node:
                yield from postorder(node.left)
                yield from postorder(node.right)
                yield node.val

        return list(postorder(root))

    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = deque()
        stack.append(root)
        res = deque()

        while stack:
            node = stack.pop()
            res.appendleft(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return list(res)

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque()
        res = []
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if not root:
                pass
            elif not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res

    def postorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = deque()
        path = deque()

        res = []

        stack.append(root)
        while stack:
            root = stack[-1]
            assert root
            if path and path[-1] == root:
                res.append(root.val)
                stack.pop()
                path.pop()
            else:
                path.append(root)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1, 2]], [2, 1]),
            ([[1, None, 2, 3]], [3, 2, 1]),
        ]
        for args, want in cases:
            got = func(TreeNode.from_list(*args))
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
