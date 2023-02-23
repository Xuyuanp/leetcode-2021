#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (57.69%)
# Likes:    3545
# Dislikes: 347
# Total Accepted:    404.6K
# Total Submissions: 699.8K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, group all the nodes with odd indices
# together followed by the nodes with even indices, and return the reordered
# list.
#
# The first node is considered odd, and the second node is even, and so on.
#
# Note that the relative order inside both the even and odd groups should
# remain as it was in the input.
#
# You must solve the problem in O(1) extra space complexity and O(n) time
# complexity.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
#
#
# Example 2:
#
#
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
#
#
#
# Constraints:
#
#
# n == number of nodes in the linked list
# 0 <= n <= 10^4
# -10^6 <= Node.val <= 10^6
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

    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd_tail = head
        even_head = head.next
        even_tail = even_head
        while even_tail and even_tail.next:
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next
            even_tail.next = odd_tail.next
            even_tail = even_tail.next

        odd_tail.next = even_head
        return head

    def oddEvenList1(self, head: ListNode) -> ListNode:
        ODD, EVEN = 0, 1
        heads = [ListNode(-1, None), ListNode(-1, None)]
        tails = [heads[0], heads[1]]
        idx = 0
        curr = head
        while curr:
            tails[idx].next = curr
            tails[idx] = curr
            curr = curr.next
            idx = (idx + 1) % 2

        tails[EVEN].next = None
        tails[ODD].next = heads[EVEN].next
        return heads[ODD].next


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4], [1, 3, 2, 4]),
        ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
    ]
    for vals, want in cases:
        got = sol.oddEvenList(ListNode.from_list(vals))
        want = ListNode.from_list(want)
        if want != got:
            print(f"Failed => args: {vals}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
