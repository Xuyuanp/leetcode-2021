#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (66.69%)
# Likes:    7645
# Dislikes: 143
# Total Accepted:    1.5M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
#
#
# Example 3:
#
#
# Input: head = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
#
#
#
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverseList1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = None
        while head:
            node = head
            head = head.next
            node.next = new_head
            new_head = node
        return new_head

    def reverseList(self, head: ListNode) -> ListNode:
        sentinel = ListNode(-1, next=head)
        n = sentinel.next
        while n and n.next:
            s = sentinel.next
            sentinel.next = n.next
            n.next = sentinel.next.next
            sentinel.next.next = s

        return sentinel.next

# @lc code=end

