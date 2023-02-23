#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (32.36%)
# Likes:    2749
# Dislikes: 1176
# Total Accepted:    401.3K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, rotate the list to the right by k places.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#
#
# Example 2:
#
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
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

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        sentinel = ListNode(float("inf"), next=head)
        slow = fast = sentinel
        kk = 0
        while fast.next and kk < k:
            fast = fast.next
            kk += 1
        if not fast.next:
            return self.rotateRight(head, k % kk)

        while fast.next and slow.next:
            fast = fast.next
            slow = slow.next
        fast.next = sentinel.next
        sentinel.next = slow.next
        slow.next = None
        return sentinel.next


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        (([1], 1), [1]),
        (([1], 2), [1]),
        (([1], 10), [1]),
        (([], 1), []),
        (([1, 2], 0), [1, 2]),
        (([1, 2], 1), [2, 1]),
        (([1, 2], 3), [2, 1]),
        (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]),
        (([0, 1, 2], 4), [2, 0, 1]),
        (([0, 1, 2], 7), [2, 0, 1]),
    ]
    for (head, k), want in cases:
        got = sol.rotateRight(ListNode.from_list(head), k)
        want = ListNode.from_list(want)
        if got != want:
            print(f"Falied => args: {head}, {k}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
