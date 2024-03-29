#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (57.11%)
# Likes:    7464
# Dislikes: 815
# Total Accepted:    1.5M
# Total Submissions: 2.6M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a sorted list. The list should
# be made by splicing together the nodes of the first two lists.
#
#
# Example 1:
#
#
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
#
#
# Input: l1 = [], l2 = []
# Output: []
#
#
# Example 3:
#
#
# Input: l1 = [], l2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.
#
#
#
from structures import ListNode


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tail = sentinel = ListNode(val=-1, next=None)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2

        return sentinel.next

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val > l2.val:
            l1, l2 = l2, l1
        head = l1
        head.next = self.mergeTwoLists(l1.next, l2)
        return head


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        (([], []), []),
        (([1, 2, 4], []), [1, 2, 4]),
        (([], [1, 2, 4]), [1, 2, 4]),
        (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
    ]
    for (l1, l2), want in cases:
        got = sol.mergeTwoLists(ListNode.from_list(l1), ListNode.from_list(l2))
        want = ListNode.from_list(want)
        if got != want:
            print(f"Failed => args: {l1}, {l2}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
