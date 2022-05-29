#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (41.93%)
# Likes:    4306
# Dislikes: 219
# Total Accepted:    388.6K
# Total Submissions: 925.6K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Given the head of a singly linked list and two integers left and right where
# left <= right, reverse the nodes of the list from position left to position
# right, and return the reversed list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#
#
# Example 2:
#
#
# Input: head = [5], left = 1, right = 1
# Output: [5]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
#
# Follow up: Could you do it in one pass?
#
from structures import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n), O(1)
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        sentinel = ListNode(-1, next=head)
        pre = sentinel
        for _ in range(left - 1):
            pre = pre.next

        curr = pre.next
        for _ in range(left, right):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp

        return sentinel.next


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        (([1], 1, 1), [1]),
        (([1, 2], 1, 1), [1, 2]),
        (([1, 2], 1, 2), [2, 1]),
        (([1, 2, 3, 4, 5], 2, 4), [1, 4, 3, 2, 5]),
        (([1, 2, 3, 4, 5], 1, 5), [5, 4, 3, 2, 1]),
    ]
    for (vals, left, right), want in cases:
        got = sol.reverseBetween(ListNode.from_list(vals), left, right)
        want = ListNode.from_list(want)
        if got != want:
            print(
                f"Failed => args: {vals}, {left}, {right}; want: {want}, but got: {got}"
            )
            break
    else:
        print("All Passed")
