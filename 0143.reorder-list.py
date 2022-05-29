#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (42.20%)
# Likes:    3526
# Dislikes: 156
# Total Accepted:    343.4K
# Total Submissions: 809.7K
# Testcase Example:  '[1,2,3,4]'
#
# You are given the head of a singly linked-list. The list can be represented
# as:
#
#
# L0 → L1 → … → Ln - 1 → Ln
#
#
# Reorder the list to be on the following form:
#
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
#
# You may not modify the values in the list's nodes. Only nodes themselves may
# be changed.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000
#
#
#
from collections import deque
from structures import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        right = fast = head
        left = None
        # find the mid node and reverse the left half
        while right and fast and fast.next:
            fast = fast.next.next
            right.next, left, right = left, right, right.next

        tail = None
        if fast and right:  # odd case. tail is the mid node
            tail = right
            right = right.next
            tail.next = None

        # merge two list in reverse order
        while left and right:
            tmp_l, tmp_r = left, right
            left, right = left.next, right.next

            tmp_r.next = tail
            tmp_l.next = tmp_r
            tail = tmp_l

    def reorderList1(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        fast = slow = head
        while slow.next and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        tail = slow
        stack = deque()
        while slow.next:
            node = slow.next
            stack.append(slow.next)
            slow = slow.next
        tail.next = None

        node = head
        while stack:
            n = stack.pop()
            n.next = node.next
            node.next = n
            node = n.next


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ]
    for args, want in cases:
        head = ListNode.from_list(args)
        sol.reorderList(head)
        want = ListNode.from_list(want)
        got = head
        if got != want:
            print(f"Failed => args: {args}, want: {want}, but got: {got}")
            break
    else:
        print("All passed")
