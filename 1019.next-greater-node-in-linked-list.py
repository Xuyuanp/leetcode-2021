#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#
# https://leetcode.com/problems/next-greater-node-in-linked-list/description/
#
# algorithms
# Medium (58.36%)
# Likes:    1633
# Dislikes: 83
# Total Accepted:    82.9K
# Total Submissions: 140.4K
# Testcase Example:  '[2,1,5]'
#
# You are given the head of a linked list with n nodes.
#
# For each node in the list, find the value of the next greater node. That is,
# for each node, find the value of the first node that is next to it and has a
# strictly larger value than it.
#
# Return an integer array answer where answer[i] is the value of the next
# greater node of the i^th node (1-indexed). If the i^th node does not have a
# next greater node, set answer[i] = 0.
#
#
# Example 1:
#
#
# Input: head = [2,1,5]
# Output: [5,5,0]
#
#
# Example 2:
#
#
# Input: head = [2,7,4,3,5]
# Output: [7,0,5,5,0]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is n.
# 1 <= n <= 10^4
# 1 <= Node.val <= 10^9
#
#
#
from collections import deque
from typing import List, Optional

from structures import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = deque()
        res = []
        while head:
            while stack and head.val > stack[-1][1]:
                res[stack.pop()[0]] = head.val
            stack.append((len(res), head.val))
            res.append(0)
            head = head.next
        return res

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[1]], [0]),
            ([[2,1,5]], [5,5,0]),
            ([[2,7,4,3,5]], [7,0,5,5,0]),
        ]
        for args, want in cases:
            got = func(ListNode.from_list(*args))

            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
