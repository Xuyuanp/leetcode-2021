#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (47.09%)
# Likes:    2863
# Dislikes: 154
# Total Accepted:    628.5K
# Total Submissions: 1.3M
# Testcase Example:  '[1,1,2]'
#
# Given the head of a sorted linked list, delete all duplicates such that each
# element appears only once. Return the linked list sorted as well.
#
#
# Example 1:
#
#
# Input: head = [1,1,2]
# Output: [1,2]
#
#
# Example 2:
#
#
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = sentinel = ListNode(-1, next=head)
        while start.next and start.next.next:
            n1, n2 = start.next, start.next.next
            if n1.val == n2.val:
                start.next = n2
            else:
                start = n1

        return sentinel.next

# @lc code=end


if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([], []),
        ([1], [1]),
        ([1, 1], [1]),
        ([1, 1, 2], [1, 2]),
        ([1, 2, 2], [1, 2]),
        ([1, 2, 2, 3], [1, 2, 3]),
        ([1, 2, 2, 3, 4, 4, 5], [1, 2, 3, 4, 5]),
    ]
    for args, want in cases:
        got = sol.deleteDuplicates(ListNode.from_list(args))
        want = ListNode.from_list(want)
        if got != want:
            print(f"Falied => args: {args}; want: {want}, but got: {got}")
            break
    else:
        print('All Passed')
