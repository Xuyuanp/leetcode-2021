#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (36.43%)
# Likes:    6042
# Dislikes: 334
# Total Accepted:    935.3K
# Total Submissions: 2.6M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
#
# Example 2:
#
#
# Input: head = [1], n = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
#
# Follow up: Could you do this in one pass?
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

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        slow = head
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1], 1], []),
            ([[1, 2], 1], [1]),
            ([[1, 2], 2], [2]),
            ([[1, 2, 3, 4, 5], 2], [1, 2, 3, 5]),
            ([[1, 2, 3, 4, 5], 5], [2, 3, 4, 5]),
        ]
        for (vals, n), want in cases:
            got = func(ListNode.from_list(vals), n)
            want = ListNode.from_list(want)
            if want != got:
                print(
                    f"  Failed => args: {vals, n}; want: {want}, but got: {got}"
                )
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
