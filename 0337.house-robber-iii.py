#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (52.14%)
# Likes:    4570
# Dislikes: 73
# Total Accepted:    226K
# Total Submissions: 432.5K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called root.
#
# Besides the root, each house has one and only one parent house. After a tour,
# the smart thief realized that all houses in this place form a binary tree. It
# will automatically contact the police if two directly-linked houses were
# broken into on the same night.
#
# Given the root of the binary tree, return the maximum amount of money the
# thief can rob without alerting the police.
#
#
# Example 1:
#
#
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#
#
# Example 2:
#
#
# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^4
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
ROB, SKIP = 0, 1


class Solution:
    # O(n), O(log(n)). bottom-up
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return 0, 0
            left = dfs(node.left)
            right = dfs(node.right)
            return node.val + left[SKIP] + right[SKIP], max(left) + max(right)

        return max(dfs(root))


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[1, 2, 3]], 5),
            ([[3, 1, 2]], 3),
            ([[3, 1, 4]], 5),
            ([[3, 2, 3, None, 3, None, 1]], 7),
            ([[3, 4, 5, 1, 3, None, 1]], 9),
            ([[4, 1, None, 2, None, 3]], 7),
            ([[2, 1, 3, None, 4]], 7),
        ]
        for args, want in cases:
            got = fn(TreeNode.from_list(*args))
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
