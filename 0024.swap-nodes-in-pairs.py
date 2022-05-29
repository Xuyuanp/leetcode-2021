#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (54.42%)
# Likes:    4077
# Dislikes: 223
# Total Accepted:    642.6K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1]
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
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
    def swapPairs(self, head: ListNode) -> ListNode:
        sentinel = ListNode(-1, next=head)
        pre = sentinel
        while pre.next and pre.next.next:
            n1, n2 = pre.next, pre.next.next
            n1.next = n2.next
            n2.next = n1
            pre.next = n2
            pre = n1

        return sentinel.next


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4], [2, 1, 4, 3]),
    ]
    for args, want in cases:
        got = sol.swapPairs(ListNode.from_list(args))
        want = ListNode.from_list(want)
        if want != got:
            print(f"Failed => args: {args}; want: {want}, but got: {got}")
            break
    else:
        print("All Passed")
