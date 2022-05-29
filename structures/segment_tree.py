from dataclasses import dataclass

from typing import List, Optional


@dataclass
class SegmentTreeNode:
    start: int
    end: int
    val: int
    left: Optional["SegmentTreeNode"] = None
    right: Optional["SegmentTreeNode"] = None

    @classmethod
    def build_tree(cls, start: int, end: int, vals: List[int]) -> "SegmentTreeNode":
        if start == end:
            return SegmentTreeNode(start, end, vals[start])

        mid = (start + end) // 2
        left = cls.build_tree(start, mid, vals)
        right = cls.build_tree(mid + 1, end, vals)

        return SegmentTreeNode(start, end, left.val + right.val, left=left, right=right)

    def update(self, index, val):
        if self.start == self.end == index:
            self.val = val
            return

        assert self.left and self.right

        mid = (self.start + self.end) // 2
        if index <= mid:
            self.left.update(index, val)
        else:
            self.right.update(index, val)

        self.val = self.left.val + self.right.val

    def query(self, i: int, j: int) -> int:
        if self.start == i and self.end == j:
            return self.val

        assert self.left and self.right

        mid = (self.start + self.end) // 2

        if i > mid:
            return self.right.query(i, j)
        if j <= mid:
            return self.left.query(i, j)

        return self.left.query(i, mid) + self.right.query(mid + 1, j)


def test():
    root = SegmentTreeNode.build_tree(0, 9, list(range(10)))

    assert root.query(0, 9) == sum(range(10))
    assert root.query(0, 0) == 0
    assert root.query(0, 1) == 1
    assert root.query(7, 9) == 24

    assert root.query(2, 4) == 9

    root.update(3, 100)

    assert root.query(3, 3) == 100
    assert root.query(2, 4) == 106

    print("ok")


if __name__ == "__main__":
    test()
