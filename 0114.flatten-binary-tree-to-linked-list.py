#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (54.05%)
# Likes:    4895
# Dislikes: 425
# Total Accepted:    478.6K
# Total Submissions: 882.3K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given the root of a binary tree, flatten the tree into a "linked list":
#
#
# The "linked list" should use the same TreeNode class where the right child
# pointer points to the next node in the list and the left child pointer is
# always null.
# The "linked list" should be in the same order as a pre-order traversal of the
# binary tree.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
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
# Input: root = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Can you flatten the tree in-place (with O(1) extra space)?
#
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

from structures import TreeNode


class Solution:

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = deque()
        node = root
        while node:
            left, right = node.left, node.right
            if right:
                stack.append(right)
            if left:
                node.right = left
                node.left = None
            elif stack:
                node.right = stack.pop()
            else:
                return
            node = node.right


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [([1, 2, 5, 3, 4, None,
               6], [1, None, 2, None, 3, None, 4, None, 5, None, 6])]
    for args, want in cases:
        root = TreeNode.from_list(args)
        sol.flatten(root)
        got = root
        want = TreeNode.from_list(want)
        if got != want:
            print(f"Failed => args: {args}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
