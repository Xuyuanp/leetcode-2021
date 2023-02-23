#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (40.06%)
# Likes:    3224
# Dislikes: 130
# Total Accepted:    346.1K
# Total Submissions: 861.3K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the
# linked list sorted as well.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
#
#
# Example 2:
#
#
# Input: head = [1,1,1,2,3]
# Output: [2,3]
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
        start = sentinel = ListNode(val=-1, next=head)
        while start.next and start.next.next:
            n1, n2 = start.next, start.next.next
            if n1.val != n2.val:
                start = start.next
                continue

            while n2 and n2.val == n1.val:
                n2 = n2.next
            start.next = n2

        return sentinel.next


# @lc code=end

if __name__ == "__main__":
    cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 1], []),
        ([1, 1, 1, 2, 3], [2, 3]),
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 2, 3, 4, 5, 5, 5], [1, 2, 3, 4]),
    ]
    sol = Solution()
    for args, want in cases:
        got = sol.deleteDuplicates(ListNode.from_list(args))
        want = ListNode.from_list(want)
        if got != want:
            print(f"Failed => args: {args}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
