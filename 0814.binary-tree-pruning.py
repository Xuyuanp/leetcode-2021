#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#
# https://leetcode.com/problems/binary-tree-pruning/description/
#
# algorithms
# Medium (71.60%)
# Likes:    2005
# Dislikes: 64
# Total Accepted:    122K
# Total Submissions: 171.3K
# Testcase Example:  '[1,null,0,0,1]'
#
# Given the root of a binary tree, return the same tree where every subtree (of
# the given tree) not containing a 1 has been removed.
#
# A subtree of a node node is node plus every node that is a descendant of
# node.
#
#
# Example 1:
#
#
# Input: root = [1,null,0,0,1]
# Output: [1,null,0,null,1]
# Explanation:
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
#
#
# Example 2:
#
#
# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
#
#
# Example 3:
#
#
# Input: root = [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 200].
# Node.val is either 0 or 1.
#
#
#
from typing import Optional

from structures import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if not prune(node.left):
                node.left = None
            if not prune(node.right):
                node.right = None

            return node.val == 1 or node.left or node.right

        return root if prune(root) else None


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1]], [1]),
            ([[0]], []),
            ([[1, None, 0, 0, 1]], [1, None, 0, None, 1]),
            ([[1, 1, 0, 1, 1, 0, 1, 0]], [1, 1, 0, 1, 1, None, 1]),
            ([[1, 0, 1, 0, 0, 0, 1]], [1, None, 1, None, 1]),
        ]
        for args, want in cases:
            got = func(TreeNode.from_list(*args))
            if TreeNode.from_list(want) != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
