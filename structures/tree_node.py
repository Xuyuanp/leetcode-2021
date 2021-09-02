from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Optional
from collections import deque
from itertools import zip_longest

@dataclass
class TreeNode:
    val: Any
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None

    def __repr__(self) -> str:
        if not self.left and not self.right:
            return f'{{ {self.val} }}'
        return f'{{ {self.val} [{self.left}, {self.right}] }}'

    @staticmethod
    def from_list(vals: List[int]) -> Optional[TreeNode]:
        if not vals:
            return None
        root = TreeNode(vals[0])
        q = deque([root])
        for val1, val2 in zip_longest(vals[1::2], vals[2::2]):
            node = q.popleft()
            if val1 is not None:
                node.left = TreeNode(val=val1)
                q.append(node.left)
            if val2 is not None:
                node.right = TreeNode(val=val2)
                q.append(node.right)

        return root
