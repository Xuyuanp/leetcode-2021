#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (43.16%)
# Likes:    5851
# Dislikes: 459
# Total Accepted:    704.6K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome.
#
#
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
#
#
#
# Follow up: Could you do it in O(n) time and O(1) space?
#
from structures import ListNode


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        left, right = None, head
        # split link-list and reverse the first half
        while right and fast and fast.next:
            fast = fast.next.next

            left, right, left.next = right, right.next, left
            # the prev line is eq to:
            #   tmp = right.next
            #   right.next = left
            #   left = right
            #   right = tmp
            #
            #           left'    right'
            #             |        |
            #        <- ┌───┐    ┌───┐    ┌───┐
            #   None    │ 1 │ -> │ 2 │ -> │ 3 │ -> None
            #           └───┘ <- └───┘    └───┘
            #     |       |        |        |
            #    left   right    left''   right''

        if fast and right:  # odd
            right = right.next

        while left and right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True

    def isPalindrome1(self, head: ListNode) -> bool:
        slow = head
        fast = head.next
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow.next
        while curr and curr.next and slow:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = slow.next
            slow.next = tmp

        n1, n2 = head, slow.next
        slow.next = None

        while n1 and n2:
            if n1.val != n2.val:
                return False
            n1 = n1.next
            n2 = n2.next
        return not n1 or not n1.next


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([1], True),
        ([1, 2], False),
        ([1, 1], True),
        ([1, 2, 1], True),
        ([1, 2, 2, 1], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3], False),
    ]
    for args, want in cases:
        got = sol.isPalindrome(ListNode.from_list(args))
        if got != want:
            print(f"Failed => args {args}, want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
