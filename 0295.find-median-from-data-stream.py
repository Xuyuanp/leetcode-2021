#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (48.36%)
# Likes:    5289
# Dislikes: 95
# Total Accepted:    364.8K
# Total Submissions: 741.1K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
#  '[[],[1],[2],[],[3],[]]'
#
# The median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value and the median is the mean of the two
# middle values.
#
#
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
#
#
# Implement the MedianFinder class:
#
#
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data
# structure.
# double findMedian() returns the median of all elements so far. Answers within
# 10^-5 of the actual answer will be accepted.
#
#
#
# Example 1:
#
#
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
#
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
#
#
#
# Constraints:
#
#
# -10^5 <= num <= 10^5
# There will be at least one element in the data structure before calling
# findMedian.
# At most 5 * 10^4 calls will be made to addNum and findMedian.
#
#
#
# Follow up:
#
#
# If all integer numbers from the stream are in the range [0, 100], how would
# you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how
# would you optimize your solution?
#
#
#

# @lc code=start
import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # fill two heaps with dummy value to avoid empty checking later
        self.greater = [float("inf")]  # minheap
        self.smaller = [float("inf")]  # maxheap

    def addNum(self, num: int) -> None:
        if num <= -self.smaller[0]:
            heapq.heappush(self.smaller, -num)
        else:
            heapq.heappush(self.greater, num)

        if len(self.smaller) < len(self.greater):
            heapq.heappush(self.smaller, -heapq.heappop(self.greater))
        elif len(self.smaller) - len(self.greater) > 1:
            heapq.heappush(self.greater, -heapq.heappop(self.smaller))

    def findMedian(self) -> float:
        length = len(self.greater) + len(self.smaller)
        if length % 2 == 1:
            return -self.smaller[0]
        return (self.greater[0] - self.smaller[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
def test():
    null = None
    cases = [
        (
            [
                [
                    "MedianFinder",
                    "addNum",
                    "addNum",
                    "findMedian",
                    "addNum",
                    "findMedian",
                ],
                [[], [1], [2], [], [3], []],
            ],
            [null, null, null, 1.5, null, 2.0],
        ),
        (
            [
                [
                    "MedianFinder",
                    "addNum",
                    "findMedian",
                    "addNum",
                    "findMedian",
                    "addNum",
                    "findMedian",
                    "addNum",
                    "findMedian",
                    "addNum",
                    "findMedian",
                    "addNum",
                    "findMedian",
                    "addNum",
                    "findMedian",
                    "addNum",
                    "findMedian",
                    "addNum",
                    "findMedian",
                    "addNum",
                    "findMedian",
                    "addNum",
                    "findMedian",
                ],
                [
                    [],
                    [6],
                    [],
                    [10],
                    [],
                    [2],
                    [],
                    [6],
                    [],
                    [5],
                    [],
                    [0],
                    [],
                    [6],
                    [],
                    [3],
                    [],
                    [1],
                    [],
                    [0],
                    [],
                    [0],
                    [],
                ],
            ],
            [
                null,
                null,
                6.00000,
                null,
                8.00000,
                null,
                6.00000,
                null,
                6.00000,
                null,
                6.00000,
                null,
                5.50000,
                null,
                6.00000,
                null,
                5.50000,
                null,
                5.00000,
                null,
                4.00000,
                null,
                3.00000,
            ],
        ),
    ]
    for (actions, args), wants in cases:
        finder = MedianFinder()
        for action, arg, want in zip(actions[1:], args[1:], wants[1:]):
            got = getattr(finder, action)(*arg)
            assert got == want, f"{action}({arg}): {got} != {want}"
    print("  All Passed")


if __name__ == "__main__":
    test()
