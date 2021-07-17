#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (43.82%)
# Likes:    7903
# Dislikes: 369
# Total Accepted:    932.7K
# Total Submissions: 2.1M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
#
# Example 1:
#
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
#
# Example 2:
#
#
# Input: lists = []
# Output: []
#
#
# Example 3:
#
#
# Input: lists = [[]]
# Output: []
#
#
#
# Constraints:
#
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.
#
#
#
from typing import List

from structures import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        tail = sentinel = ListNode(float('inf'), next=None)

        q = PriorityQueue()
        for i, head in enumerate(lists):
            if head:
                q.put((head.val, i))

        while not q.empty():
            _, index = q.get()
            head = lists[index]
            tail.next = head
            tail = tail.next

            head = head.next
            lists[index] = head
            if head:
                q.put((head.val, index))

        return sentinel.next

# @lc code=end


if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([], []),
        ([[1, 2]], [1, 2]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([[1, 2], [], [3, 4]], [1, 2, 3, 4]),
        ([[2, 3], [5], [1, 4]], [1, 2, 3, 4, 5]),
        ([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6])
    ]
    for args, want in cases:
        got = sol.mergeKLists([ListNode.from_list(arg) for arg in args])
        want = ListNode.from_list(want)
        if got != want:
            print(f"Falied => args: {args}; want: {want}, but got: {got}")
            break
    else:
        print('All Passed')
