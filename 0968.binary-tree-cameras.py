#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#
# https://leetcode.com/problems/binary-tree-cameras/description/
#
# algorithms
# Hard (40.70%)
# Likes:    2021
# Dislikes: 29
# Total Accepted:    51.3K
# Total Submissions: 125.2K
# Testcase Example:  '[0,0,null,0,0]'
#
# You are given the root of a binary tree. We install cameras on the tree nodes
# where each camera at a node can monitor its parent, itself, and its immediate
# children.
#
# Return the minimum number of cameras needed to monitor all nodes of the
# tree.
#
#
# Example 1:
#
#
# Input: root = [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
#
#
# Example 2:
#
#
# Input: root = [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the
# tree. The above image shows one of the valid configurations of camera
# placement.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# Node.val == 0
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
    # O(n), O(log(n)). NOTE: leetcode doesn't support pattern matching
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node: Optional[TreeNode]) -> int:
            """
            0: covered by camera(s)
            1: uncovered by any camera
            2: placed camera
            """
            nonlocal res
            if not node:
                return 0
            match [dfs(node.left), dfs(node.right)]:
                case [1, _] | [_, 1]: # if any child is not covered by a camera, we should place a camera here
                    res += 1
                    return 2
                case [2, _] | [_, 2]: # else if any child placed a camera, we are coverd
                    return 0
                case _:               # otherwise, we need a camera
                    return 1

        if dfs(root) == 1:
            res += 1
        return res

    def minCameraCover1(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node: Optional[TreeNode]) -> int:
            """
            0: covered by camera(s)
            1: uncovered by any camera
            2: placed camera
            """
            nonlocal res
            if not node:
                return 0
            x, y = dfs(node.left), dfs(node.right)
            if 1 in (x, y):
                res += 1
                return 2
            if 2 in (x, y):
                return 0
            return 1

        if dfs(root) == 1:
            res += 1
        return res

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([[]], 0),
            ([[0,0,None,0,0]], 1),
            ([[0,0,None,0,None,0,None,None,0]], 2),
        ]
        for args, want in cases:
            got = fn(TreeNode.from_list(*args))
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
