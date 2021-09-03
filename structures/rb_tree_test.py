from datetime import datetime
import random

from .rb_tree import RBTree


def test_insert():
    tree = RBTree()
    keys = list(range(100))
    for key in keys:
        tree.insert(key)

    for i, key in enumerate(tree):
        assert i == key

def test_chaos():
    tree = RBTree()

    N = 10000

    keys = list(range(1,N+1))
    random.shuffle(keys)

    start = datetime.now()

    for key in keys:
        tree.insert(key)

    insert_end = datetime.now()
    print(f'inserts cost: {(insert_end-start).total_seconds()}s; rotates: {tree.left_rotates, tree.right_rotates, tree.left_rotates+tree.right_rotates, tree.insert_rotates}')

    assert tree.count == N

    tree.left_rotates = 0
    tree.right_rotates = 0

    random.shuffle(keys)
    remove_start = datetime.now()

    for key in keys:
        tree.remove(key)

    remove_end = datetime.now()
    print(f'removes cost: {(remove_end-remove_start).total_seconds()}s; rotates: {tree.left_rotates, tree.right_rotates, tree.left_rotates+tree.right_rotates, tree.remove_rotates}')

    assert tree.count == 0
