#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
#
# algorithms
# Medium (66.42%)
# Likes:    917
# Dislikes: 53
# Total Accepted:    68.9K
# Total Submissions: 104K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# You are given the head of a linked list, and an integer k.
#
# Return the head of the linked list after swapping the values of the k^th node
# from the beginning and the k^th node from the end (the list is 1-indexed).
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
#
#
# Example 2:
#
#
# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
#
#
# Example 3:
#
#
# Input: head = [1], k = 1
# Output: [1]
#
#
# Example 4:
#
#
# Input: head = [1,2], k = 1
# Output: [2,1]
#
#
# Example 5:
#
#
# Input: head = [1,2,3], k = 2
# Output: [1,2,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is n.
# 1 <= k <= n <= 10^5
# 0 <= Node.val <= 100
#
#
#
from typing import Optional

from structures import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n), O(1)
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        fast = slow = head
        while k > 1:
            fast = fast.next
            k -= 1

        node1 = fast

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.val, node1.val = node1.val, slow.val

        return head


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1], 1], [1]),
            ([[1, 2], 1], [2, 1]),
            ([[1, 2, 3, 4, 5], 1], [5, 2, 3, 4, 1]),
            ([[1, 2, 3, 4, 5], 2], [1, 4, 3, 2, 5]),
            ([[1, 2, 3, 4, 5], 3], [1, 2, 3, 4, 5]),
            ([[1, 2, 3, 4, 5], 4], [1, 4, 3, 2, 5]),
            ([[1, 2, 3, 4, 5], 5], [5, 2, 3, 4, 1]),
        ]
        for args, want in cases:
            got = func(ListNode.from_list(args[0]), args[1])
            if ListNode.from_list(want) != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
