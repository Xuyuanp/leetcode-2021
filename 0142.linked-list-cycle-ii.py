#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (40.76%)
# Likes:    4618
# Dislikes: 332
# Total Accepted:    480.2K
# Total Submissions: 1.2M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
#
# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to. Note that pos is not passed as a parameter.
#
# Notice that you should not modify the linked list.
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#
#
#
# Constraints:
#
#
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
#
#
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
#
#
from structures import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @lc code=start


class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or head.next == head:
            return head

        slow = fast = head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None

        slow = head
        while slow and fast and slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


# @lc code=end
