from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Iterator, Optional, Tuple

KeyType = Any

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

    @classmethod
    def ensure_black(cls, node: Optional[RBNode]):
        if node:
            node.color = Color.BLACK

    def has_red_children(self) -> bool:
        return self.left and self.left.color == Color.RED or \
            self.right and self.right.color == Color.BLACK

    def __repr__(self) -> str:
        if not self.left and not self.right:
            return f'{{ {self.key}:{self.color} }}'
        return f'{{ {self.key}:{self.color} [{self.left} {self.right}] }}'

    def __iter__(self) -> Iterator[KeyType]:
        if self.left:
            yield from self.left.__iter__()

        yield self.key

        if self.right:
            yield from self.right.__iter__()


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
        self._count = 0

    def __iter__(self) -> Iterator[KeyType]:
        if self.root:
            yield from self.root.__iter__()

    def __len__(self) -> int:
        return self.count

    @property
    def count(self) -> int:
        return self._count

    def insert(self, key: KeyType):
        self.root = self._insert(key, Context(current=self.root))
        RBNode.ensure_black(self.root)
        self._count += 1

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

    def remove(self, key: KeyType):
        self.root = self._remove(key, Context(current=self.root))
        RBNode.ensure_black(self.root)

    def _remove_fix(self, old_child: RBNode, new_child: Optional[RBNode], ctx: Context) -> RBNode:
        parent = ctx.current
        assert parent

        if old_child.color == Color.RED:
            assert not new_child
            return parent

        if new_child and new_child.color == Color.RED:
            new_child.color = Color.BLACK
            return parent

        # double black
        sibling = parent.left if new_child == parent.right else parent.right
        assert sibling, 'double black node always has a sibling'

        sibling_is_left = sibling == parent.left

        # parent is not None, we ignore case1 here

        # case2
        if sibling.color == Color.RED:
            #
            #        P:black               S:black
            #       /  \                  /     \
            #  C:black  S:red   =>       P:red   b2
            #          / \              /   \
            #         b1  b2        C:black  b1
            #
            assert parent.color == Color.BLACK

            rotate_fn = self._right_rotate if sibling_is_left else self._left_rotate
            rotate_fn(sibling, parent)
            parent.color = Color.RED
            sibling.color = Color.BLACK

            return sibling

        if not sibling.has_red_children():
            if parent.color == Color.BLACK:
                # case3
                #
                #        P:black               P:black
                #       /  \                  /     \
                #  C:black  S:black    =>   C:black  S:red
                #          / \                       / \
                #         b1  b2                    b1  b2
                #
                sibling.color = Color.RED
            else:
                # case4
                #
                #        P:red                 P:black
                #       /  \                   /     \
                #  C:black  S:black    =>    C:black  S:red
                #          / \                       / \
                #         b1  b2                    b1  b2
                #
                parent.color, sibling.color = sibling.color, parent.color

            return parent

        closer_node = sibling.right if sibling_is_left else sibling.left
        outer_node = sibling.left if sibling_is_left else sibling.right

        # case5
        if closer_node and closer_node.color == Color.RED and RBNode.is_black(outer_node):
            if sibling_is_left:
                #
                #           P:any                    P:any
                #          /   \                    /   \
                #      S:black  C:black   =>    SR:black C:black
                #      /    \                      /   \
                #  SL:black SR:red               S:red  b2
                #           / \                  /   \
                #          b1  b2           SL:black  b1
                #
                self._left_rotate(closer_node, sibling)
                parent.left = closer_node
            else:
                #
                #        P:any                    P:any
                #       /  \                     /     \
                #  C:black  S:black      =>    C:black SL:black
                #          / \                         / \
                #      SL:red SR:black                b1  S:red
                #     / \                                / \
                #    b1  b2                             b2  SR:black
                #
                self._right_rotate(closer_node, sibling)
                parent.right = closer_node

            closer_node.color = Color.BLACK
            sibling.color = Color.RED

            sibling = closer_node
            sibling_is_left = sibling == parent.left

        outer_node = sibling.left if sibling_is_left else sibling.right

        # case6
        if outer_node and outer_node.color == Color.RED:
            if sibling_is_left:
                #
                #           P:c                         S:c
                #          /   \                       /   \
                #      S:black  C:black   =>      SL:black  P:black
                #       /    \                             /  \
                #  SL:red    b1                           b1   C:black
                #
                self._right_rotate(sibling, parent)
            else:
                #
                #        P:c                           S:c
                #       /  \                          /   \
                #  C:black  S:black      =>       P:black SR:black
                #          / \                    /  \
                #         b1  SR:red         C:black  b1
                #
                self._left_rotate(sibling, parent)
            sibling.color = parent.color
            RBNode.ensure_black(sibling.left)
            RBNode.ensure_black(sibling.right)
            return sibling

        return parent

    def _remove(self, key: KeyType, ctx: Context) -> Optional[RBNode]:
        current = ctx.current
        if not current:
            # key not found
            return None

        if key < current.key:
            if not current.left:
                return current
            old_child = current.left
            new_child = self._remove(key, ctx.left)
            current.left = new_child
        elif key > current.key:
            if not current.right:
                return current
            old_child = current.right
            new_child = self._remove(key, ctx.right)
            current.right = new_child
        elif current.left and current.right:
            # current has two children
            # replace current key with the smallest key in the right subtree
            # and remove the smallest node
            old_child = current.right
            new_child, current.key = self._remove_smallest_node(ctx.right)
            current.right = new_child
        else:
            # current has 0 or 1 child
            return self._remove_current(ctx)

        return self._remove_fix(old_child, new_child, ctx)

    def _remove_smallest_node(self, ctx: Context) -> Tuple[Optional[RBNode], KeyType]:
        current = ctx.current
        assert current
        if current.left:
            old_child = current.left
            new_child, key_of_removed = self._remove_smallest_node(ctx.left)
            current.left = new_child

            replaced = self._remove_fix(old_child, new_child, ctx)
        else:
            key_of_removed = current.key
            replaced = self._remove_current(ctx)

        return replaced, key_of_removed

    def _remove_current(self, ctx: Context) -> Optional[RBNode]:
        current = ctx.current
        assert current and not (current.left and current.right), \
            'node should have at most one child'

        child = current.left if current.left else current.right

        if current.color == Color.RED:
            assert not child, 'a red node can NOT have exactly one child'
        elif child and child.color == Color.RED:
            # a black node has a red leaf child
            assert not child.left and not child.right, \
                "a black node's single red child node can NOT have children"
        else:
            # child is nil or black
            pass

        self._count -= 1
        return child

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
        ([1,-1], None),
        ([1, 2,-1], RBNode(2, color=Color.BLACK)),
        ([1, 2, 3, -1], RBNode(2, color=Color.BLACK, right=RBNode(3))),
        ([1, 2, 3, -2], RBNode(3, color=Color.BLACK, left=RBNode(1))),
        ([1, 2, 3, -3], RBNode(2, color=Color.BLACK, left=RBNode(1))),
        ([3,2,4,5,-4], RBNode(
            3, color=Color.BLACK,
            left=RBNode(2, color=Color.BLACK),
            right=RBNode(5, color=Color.BLACK)
        )),
        ([3,2,4,5,-4,-3,-2], RBNode(5, color=Color.BLACK)),
    ]
    for keys, want in cases:
        tree = RBTree()
        for key in keys:
            if key > 0:
                tree.insert(key)
            elif key < 0:
                tree.remove(-key)

        got = tree.root
        assert want == got, f"want: {want}, but got: {got}"
    print('  All Passed')

    print()


if __name__ == '__main__':
    test()

