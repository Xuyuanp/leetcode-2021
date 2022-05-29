#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (57.04%)
# Likes:    2731
# Dislikes: 211
# Total Accepted:    263.3K
# Total Submissions: 458.3K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Example 1:
#
#
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
#
#
# Example 2:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
#
#
# Example 3:
#
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
#
#
#
# Follow up: Could you solve it without reversing the input lists?
#
#
from typing import Optional

from structures import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(m+n), O(1)
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        x = y = 0

        while l1:
            x = x * 10 + l1.val
            l1 = l1.next

        while l2:
            y = y * 10 + l2.val
            l2 = l2.next

        total, curr = divmod(x + y, 10)
        head = ListNode(curr)

        while total:
            total, curr = divmod(total, 10)
            head = ListNode(curr, next=head)

        return head


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[0], [0]], [0]),
            ([[1], [9]], [1, 0]),
            ([[1, 1], [9]], [2, 0]),
            ([[7, 2, 4, 3], [5, 6, 4]], [7, 8, 0, 7]),
        ]
        for args, want in cases:
            got = func(ListNode.from_list(args[0]), ListNode.from_list(args[1]))
            if ListNode.from_list(want) != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
