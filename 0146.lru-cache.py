#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (37.21%)
# Likes:    9137
# Dislikes: 362
# Total Accepted:    804.8K
# Total Submissions: 2.2M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
#  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
#
# Implement the LRUCache class:
#
#
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
#
#
# The functions get and put must each run in O(1) average time complexity.
#
#
# Example 1:
#
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
#
#
# Constraints:
#
#
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.
#
#
#

# @lc code=start
from collections import OrderedDict


class Node:
    def __init__(self, key: int, val: int, next, prev) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


# Double Linked-List
class LRUCache1:
    def __init__(self, capacity: int):
        self.head = Node(0, 0, None, None)
        self.tail = Node(0, 0, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        self.capacity = capacity

    def priority_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def evict(self):
        if len(self.cache) < self.capacity:
            return
        node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev

        del self.cache[node.key]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.priority_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.priority_node(node)
            node.key = key
            node.val = value
            return

        self.evict()
        node = Node(key, value, self.head.next, self.head)
        self.head.next.prev = node
        self.head.next = node

        self.cache[key] = node


# OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key: int, val: int):
        self.cache[key] = val
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            oldest = next(iter(self.cache))
            del self.cache[oldest]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
