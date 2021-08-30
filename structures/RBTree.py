from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

KeyType = int

class Color(Enum):
    RED = auto()
    BLACK = auto()


@dataclass
class RBNode:
    key: KeyType
    color: Color = Color.RED
    left: Optional[RBNode] = None
    right: Optional[RBNode] = None

    @classmethod
    def is_black(cls, node: Optional[RBNode]) -> bool:
        return not node or node.color == Color.BLACK

    def __repr__(self) -> str:
        if not self.left and not self.right:
            return f'{{ {self.key}:{self.color} }}'
        return f'{{ {self.key}:{self.color} [{self.left} {self.right}] }}'


@dataclass
class Context:
    current: Optional[RBNode] = None
    sibling: Optional[RBNode] = None
    parent: Optional[RBNode] = None

    @property
    def left(self) -> Context:
        assert self.current is not None
        return Context(
            current=self.current.left,
            sibling=self.current.right,
            parent=self.current
        )

    @property
    def right(self) -> Context:
        assert self.current is not None
        return Context(
            current=self.current.right,
            sibling=self.current.left,
            parent=self.current
        )


class RBTree:
    root: Optional[RBNode] = None

    def __init__(self):
        self.root = None

    def insert(self, key: KeyType):
        self.root = self._insert(key, Context(current=self.root))
        self.root.color = Color.BLACK

    def _insert(self, key: KeyType, ctx: Context) -> RBNode:
        parent = ctx.current
        if not parent:
            child = RBNode(key)
        elif key < parent.key:
            child = self._insert(key, ctx.left)
            parent.left = child
        else:
            child = self._insert(key, ctx.right)
            parent.right = child

        return self._insert_fixup(child, ctx)

    # return new root of the current subtree
    def _insert_fixup(self, child: RBNode, ctx: Context) -> RBNode:
        parent = ctx.current
        uncle = ctx.sibling
        grandp = ctx.parent

        if child.color == Color.BLACK and parent:
            # internal black nodes don't need fixup
            return parent

        if not parent:
            # root or new created leaf node
            return child

        if parent.color == Color.BLACK:
            if child == parent.left and child.left and child.left.color == Color.RED:
                # CC = child of child
                #
                #      P:black                   C:black
                #     /                         / \
                #    C:red          ==>     CC:red P:red
                #   /
                #  CC:red
                #
                parent.color = Color.RED
                child.color = Color.BLACK
                self._right_rotate(child, parent)
            elif child == parent.right and child.right and child.right.color == Color.RED:
                # CC = child of child
                #
                #  P:black                       C:black
                #   \                           / \
                #    C:red          ==>     CC:red P:red
                #     \
                #     CC:red
                #
                parent.color = Color.RED
                child.color = Color.BLACK
                self._left_rotate(child, parent)
            else:
                assert RBNode.is_black(child.left) and RBNode.is_black(child.right)
                child = parent
            return child

        assert child.color == parent.color == Color.RED
        assert grandp, "grand_parent must not be None when parent.color == RED"
        assert grandp.color == Color.BLACK

        if uncle and uncle.color == Color.RED:
            #
            #     G:black                         G:red
            #    / \                             / \
            # U:red P:red          ==>      U:black P:black
            #        \                               \
            #         C:red                           C:red
            #
            grandp.color = Color.RED
            parent.color = Color.BLACK
            uncle.color = Color.BLACK

            return parent

        if child == parent.right and parent == grandp.left:
            #
            #    G:black                  G:black
            #   /                        /
            #  P:red          ==>       C:red
            #   \                      /
            #    C:red                P:red
            #
            self._left_rotate(child, parent)
        elif child == parent.left and parent == grandp.right:
            #
            #  G:black                G:black
            #   \                      \
            #    P:red        ==>       C:red
            #   /                        \
            #  C:red                      P:red
            #
            self._right_rotate(child, parent)
        else:
            # there is no guarantee that the subtree in this context is valid for now.
            child = parent

        return child

    def _left_rotate(self, child: RBNode, parent: RBNode):
        parent.right = child.left
        child.left = parent

    def _right_rotate(self, child: RBNode, parent: RBNode):
        parent.left = child.right
        child.right = parent

    # def remove(self, key: KeyType) -> bool:
    #     return self._remove(key, Context(node=self.root))
    #
    # def _remove(self, key: KeyType, ctx: Context) -> bool:
    #     if not ctx.node:
    #         return False
    #     if key < ctx.node.key:
    #         return self._remove(key, ctx.left)
    #     if key > ctx.node.key:
    #         return self._remove(key, ctx.right)
    #
    #     if not ctx.node.right:
    #         self._remove_one_child(ctx)
    #     else:
    #         ctx.node.key = self._remove_smallest_child(ctx)
    #
    #     return True
    #
    # def _remove_smallest_child(self, ctx: Context) -> KeyType:
    #     assert ctx.node
    #     if ctx.node.left:
    #         return self._remove_smallest_child(ctx.left)
    #     key = ctx.node.key
    #     self._remove_one_child(ctx)
    #     return key
    #
    # def _remove_one_child(self, ctx: Context):
    #     assert ctx.node
    #     if not ctx.node.left and not ctx.node.right:
    #         return

def test():
    print('Testing RBTree:')
    cases = [
        ([1], RBNode(1, color=Color.BLACK)),
        ([1,2], RBNode(1, color=Color.BLACK, right=RBNode(2))),
        ([1,2,3], RBNode(
            2, color=Color.BLACK,
            left=RBNode(1),
            right=RBNode(3)
        )),
        ([1,3,2], RBNode(
            2, color=Color.BLACK,
            left=RBNode(1),
            right=RBNode(3)
        )),
        ([2,3,1], RBNode(
            2, color=Color.BLACK,
            left=RBNode(1),
            right=RBNode(3)
        )),
        ([2,1,3], RBNode(
            2, color=Color.BLACK,
            left=RBNode(1),
            right=RBNode(3)
        )),
        ([3,2,1], RBNode(
            2, color=Color.BLACK,
            left=RBNode(1),
            right=RBNode(3)
        )),
        ([3,1,2], RBNode(
            2, color=Color.BLACK,
            left=RBNode(1),
            right=RBNode(3)
        )),
        ([3,2,4], RBNode(
            3, color=Color.BLACK,
            left=RBNode(2),
            right=RBNode(4)
        )),
        ([3,2,4,5], RBNode(
            3, color=Color.BLACK,
            left=RBNode(2, color=Color.BLACK),
            right=RBNode(
                4, color=Color.BLACK,
                right=RBNode(5))
        )),
    ]
    for keys, want in cases:
        tree = RBTree()
        for key in keys:
            if key > 0:
                tree.insert(key)

        got = tree.root
        assert want == got
    print('  All Passed')
    print()


if __name__ == '__main__':
    test()
