#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (40.12%)
# Likes:    2993
# Dislikes: 129
# Total Accepted:    498.5K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Given the head of a linked list and an integer val, remove all the nodes of
# the linked list that has Node.val == val, and return the new head.
#
#
# Example 1:
#
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#
#
# Example 2:
#
#
# Input: head = [], val = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [7,7,7,7], val = 7
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 10^4].
# 1 <= Node.val <= 50
# 0 <= val <= 50
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = sentinel = ListNode(val=-1, next=head)
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return sentinel.next

# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        (([1], 1), []),
        (([1, 2], 1), [2]),
        (([1, 2], 2), [1]),
        (([1, 1, 1, 1], 1), []),
        (([1, 2, 2, 2, 2], 2), [1]),
        (([1, 2, 2, 2, 2, 3], 2), [1, 3]),
    ]
    for (args, val), want in cases:
        got = sol.removeElements(ListNode.from_list(args), val)
        want = ListNode.from_list(want)
        if got != want:
            print(f'Failed => args: {args}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
