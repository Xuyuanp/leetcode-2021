#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (51.12%)
# Likes:    3842
# Dislikes: 132
# Total Accepted:    541.6K
# Total Submissions: 1.1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the zigzag level order traversal of
# its nodes' values. (i.e., from left to right, then right to left for the next
# level and alternate between).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([(root, 1)])
        curr_level = 0

        while q:
            node, level = q.popleft()
            if level != curr_level:
                curr_level += 1
                res.append([])
            if level % 2 == 1:
                res[-1].append(node.val)
            else:
                res[-1] = [node.val] + res[-1]
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return res


# @lc code=end


# [1,2,3,4,null,null,5], [[1],[3,2],[4,5]]
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([], []),
        ([1], [[1]]),
        ([1, 2, 3, 4, None, None, 5], [[1], [3, 2], [4, 5]]),
    ]
    for args, want in cases:
        got = sol.zigzagLevelOrder(TreeNode.from_list(args))
        if got != want:
            print(f"Failed => args: {args}; want: {want} but got: {got}")
            break
    else:
        print("All Passed")
