#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Medium (48.63%)
# Likes:    5915
# Dislikes: 331
# Total Accepted:    295.6K
# Total Submissions: 604.2K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# Given the root of a binary tree and an integer targetSum, return the number
# of paths where the sum of the values along the path equals targetSum.
#
# The path does not need to start or end at the root or a leaf, but it must go
# downwards (i.e., traveling only from parent nodes to child nodes).
#
#
# Example 1:
#
#
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
#
#
# Example 2:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 1000].
# -10^9 <= Node.val <= 10^9
# -1000 <= targetSum <= 1000
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

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0

        def dfs(node: Optional[TreeNode], target: int):
            if not node:
                return
            calc(node, target)
            dfs(node.left, target)
            dfs(node.right, target)

        def calc(node: TreeNode, target: int):
            nonlocal res
            if node.val == target:
                res += 1

            if node.left:
                calc(node.left, target - node.val)
            if node.right:
                calc(node.right, target - node.val)

        dfs(root, targetSum)

        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[], 1], 0),
            ([[10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8], 3),
            ([[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22], 3),
        ]
        for args, want in cases:
            got = func(TreeNode.from_list(args[0]), args[1])
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
