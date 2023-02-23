#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (36.10%)
# Likes:    7012
# Dislikes: 448
# Total Accepted:    577K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,3]'
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes in the sequence has an edge connecting them. A node can only appear in
# the sequence at most once. Note that the path does not need to pass through
# the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any path.
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 =
# 6.
#
#
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7
# = 42.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000
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

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return -float("inf"), -float("inf")

            left_use, left_skip = dfs(node.left)
            right_use, right_skip = dfs(node.right)

            max_use = max(node.val, node.val + left_use, node.val + right_use)
            max_skip = max(
                left_skip,
                right_skip,
                left_use,
                right_use,
                node.val + left_use + right_use,
            )
            return max_use, max_skip

        return max(dfs(root))


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[-1]], -1),
            ([[-2, 1]], 1),
            ([[1, 2, 3]], 6),
            ([[-10, 9, 20, None, None, 15, 7]], 42),
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
