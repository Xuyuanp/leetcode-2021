from __future__ import annotations

from dataclasses import dataclass

from typing import Any, List, Optional


@dataclass
class ListNode:
    val: Any
    next: Optional[ListNode] = None

    def __repr__(self) -> str:
        def helper():
            head = self
            while head:
                yield head.val
                head = head.next

        return str(list(helper()))

    @staticmethod
    def from_list(vals: List) -> Optional[ListNode]:
        if not vals:
            return None
        head = tail = ListNode(vals[0], None)
        for val in vals[1:]:
            tail.next = ListNode(val, None)
            tail = tail.next
        return head
