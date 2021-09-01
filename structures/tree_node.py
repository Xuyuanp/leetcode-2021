from typing import List, Optional
from collections import deque
from itertools import zip_longest

class TreeNode:
    def __init__(self, val=0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        def helper(node: TreeNode):
            q = deque([(node, 0)])
            while q:
                node, level = q.popleft()
                yield node.val, level
                if node.left:
                    q.append((node.left, level+1))
                if node.right:
                    q.append((node.right, level+1))

        return str(list(helper(self)))

    def __eq__(self, o) -> bool:
        def eq(n1, n2) -> bool:
            if n1 is None and n2 is None:
                return True
            if n1 and n2:
                return n1.val == n2.val and n1.left == n2.left and n1.right == n2.right
            return False
        return eq(self, o)

    @staticmethod
    def from_list(vals: List[int]) -> Optional['TreeNode']:
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
