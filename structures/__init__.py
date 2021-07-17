from typing import List, Optional

class ListNode:
    def __init__(self, val, next: Optional['ListNode']):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        def helper():
            head = self
            while head:
                yield head.val
                head = head.next
        return str(list(helper()))

    @staticmethod
    def from_list(vals: List) -> Optional['ListNode']:
        if not vals:
            return None
        head = ListNode(vals[0], None)
        tail = head
        for val in vals[1:]:
            tail.next = ListNode(val, None)
            tail = tail.next
        return head
