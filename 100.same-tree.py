#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (54.53%)
# Likes:    3537
# Dislikes: 92
# Total Accepted:    756K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
#
#
# Example 1:
#
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#
#
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
#
#
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4
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
from collections import deque


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q:
            return p.vall == q.val and \
                self.isSameTree(p.left, q.right) and \
                self.isSameTree(p.right, q.right)
        return False

    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        def comp(p: TreeNode, q: TreeNode) -> bool:
            if p and q:
                return p.val == q.val
            if not p and not q:
                return True
            return False

        deq = deque([(p, q)])
        while deq:
            p, q = deq.popleft()
            if not comp(p, q):
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True


# @lc code=end

