#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Medium (43.59%)
# Likes:    2855
# Dislikes: 110
# Total Accepted:    225.4K
# Total Submissions: 514K
# Testcase Example:  '[1,3,null,null,2]'
#
# You are given the root of a binary search tree (BST), where exactly two nodes
# of the tree were swapped by mistake. Recover the tree without changing its
# structure.
#
# Follow up: A solution using O(n) space is pretty straight forward. Could you
# devise a constant space solution?
#
#
# Example 1:
#
#
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3
# makes the BST valid.
#
#
# Example 2:
#
#
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2
# and 3 makes the BST valid.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 1000].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#
from structures import TreeNode

# @lc code=start
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        def traverse(root: TreeNode):
            if root:
                yield from traverse(root.left)
                yield root
                yield from traverse(root.right)

        nodes = traverse(root)
        prev = next(nodes)
        drops = []
        for node in nodes:
            if node.val < prev.val:
                drops.append((prev, node))
            prev = node
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val

    # O(n), O(log(n))
    def recoverTree1(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # case 1:
        # ... < x1 < x2 > x3 < x4 < ...
        #    swap x2 x3
        # case 2:
        # ... < x1 > x2 < ... < x3 > x4 < ...
        #    swap x1 x4
        curr, prev = root, TreeNode(val=float('-inf'))
        drops, stack = [], []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            if node.val < prev.val:
                drops.append((prev, node))
            prev, curr = node, node.right
        # drops can be either [(x1, x2)] or [(x1, x2), (x3, x4)]
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val

# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    cases = [
        ([1,3,None,None,2], [3,1,None,None,2]),
        ([3,1,4,None, None, 2], [2, 1, 4, None, None, 3]),
    ]
    for args, want in cases:
        root = TreeNode.from_list(args)
        sol.recoverTree(root)
        got = root
        want = TreeNode.from_list(want)
        if want != got:
            print(f'Failed => args: {args}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
