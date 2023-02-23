#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/
#
# algorithms
# Medium (68.93%)
# Likes:    876
# Dislikes: 684
# Total Accepted:    59.5K
# Total Submissions: 86.3K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]'
#
# Given the root of a binary tree, return the lowest common ancestor of its
# deepest leaves.
#
# Recall that:
#
#
# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0. if the depth of a node is d, the
# depth of each of its children is d + 1.
# The lowest common ancestor of a set S of nodes, is the node A with the
# largest depth such that every node in S is in the subtree with root A.
#
#
# Note: This question is the same as 865:
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the
# diagram.
# The nodes coloured in blue are the deepest leaf-nodes of the tree.
# Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2,
# but the depth of nodes 7 and 4 is 3.
#
# Example 2:
#
#
# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree, and it's the lca of
# itself.
#
#
# Example 3:
#
#
# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest leaf node in the tree is 2, the lca of one node is
# itself.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree will be in the range [1, 1000].
# 0 <= Node.val <= 1000
# The values of the nodes in the tree are unique.
#
#
#
from typing import Optional, Tuple

from structures import TreeNode


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(node: Optional[TreeNode]) -> Tuple[Optional[TreeNode], int]:
            if not node:
                return None, 0
            if not node.left and not node.right:
                return node, 0
            left = helper(node.left)
            right = helper(node.right)
            if not left[0]:
                return right[0], right[1] + 1
            if not right[0]:
                return left[0], left[1] + 1
            if left[1] > right[1]:
                return left[0], left[1] + 1
            return ((right[0], right[1] + 1) if right[1] > left[1] else
                    (node, left[1] + 1))

        return helper(root)[0]


# @lc code=end
def test():
    null = None
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1]], [1]),
            ([[0, 1, 3, null, 2]], [2]),
            ([[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]], [2, 7, 4]),
        ]
        for args, want in cases:
            got = func(TreeNode.from_list(*args))
            want = TreeNode.from_list(want)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
