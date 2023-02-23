#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (45.48%)
# Likes:    2519
# Dislikes: 428
# Total Accepted:    289.6K
# Total Submissions: 634.8K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
#
# Example 1:
#
#
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [2,1], x = 2
# Output: [1,2]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
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

    def partition(self, head: ListNode, x: int) -> ListNode:
        less_head = less_tail = ListNode(-1, next=None)
        greater_head = greater_tail = ListNode(-1, next=None)

        while head:
            if head.val < x:
                less_tail.next = head
                less_tail = less_tail.next
            else:
                greater_tail.next = head
                greater_tail = greater_tail.next
            head = head.next

        less_tail.next = greater_head.next
        greater_tail.next = None
        return less_head.next


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (([], 1), []),
            (([1], 1), [1]),
            (([1], 2), [1]),
            (([2], 1), [2]),
            (([1, 4, 3, 2, 5, 2], 3), [1, 2, 2, 4, 3, 5]),
            (([2, 1], 2), [1, 2]),
            (([2, 1], 10), [2, 1]),
            (([2, 1], 0), [2, 1]),
        ]
        for args, want in cases:
            got = func(ListNode.from_list(args[0]), args[1])
            want = ListNode.from_list(want)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
