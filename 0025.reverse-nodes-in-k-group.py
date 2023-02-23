#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (46.47%)
# Likes:    4209
# Dislikes: 416
# Total Accepted:    372.7K
# Total Submissions: 799.4K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes, in
# the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may
# be changed.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
#
# Example 3:
#
#
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
#
#
# Example 4:
#
#
# Input: head = [1], k = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz
#
#
#
# Follow-up: Can you solve the problem in O(1) extra memory space?
#
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Tuple

from structures import ListNode


class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        def reverseFirstK(head: ListNode,
                          k: int) -> Tuple[ListNode, ListNode, bool]:
            sentinel = ListNode(-1, next=head)
            pre = sentinel
            tail = pre.next
            while tail and tail.next and k > 1:
                pre_next = pre.next
                pre.next = tail.next
                tail.next = pre.next.next
                pre.next.next = pre_next
                k -= 1

            return sentinel.next, tail, k > 1

        head, tail, _ = reverseFirstK(head, k)
        while tail:
            new_head, new_tail, undo = reverseFirstK(tail.next, k)

            if undo:
                new_head, new_tail, _ = reverseFirstK(new_head, k)
                tail.next = new_head
                tail = new_tail
                break

            tail.next = new_head
            tail = new_tail

        return head


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        (([1, 2, 3], 1), [1, 2, 3]),
        (([1, 2, 3], 2), [2, 1, 3]),
        (([1, 2, 3, 4], 2), [2, 1, 4, 3]),
        (([1, 2, 3, 4], 3), [3, 2, 1, 4]),
        (([1, 2, 3, 4], 4), [4, 3, 2, 1]),
    ]
    for (vals, k), want in cases:
        got = sol.reverseKGroup(ListNode.from_list(vals), k)
        want = ListNode.from_list(want)
        if want != got:
            print(f"Failed => args: {vals, k}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
