#
# @lc app=leetcode id=2013 lang=python3
#
# [2013] Detect Squares
#
# https://leetcode.com/problems/detect-squares/description/
#
# algorithms
# Medium (34.56%)
# Likes:    110
# Dislikes: 58
# Total Accepted:    5.8K
# Total Submissions: 16.6K
# Testcase Example:  '["DetectSquares","add","add","add","count","count","add","count"]\n' +
# '[[],[[3,10]],[[11,2]],[[3,2]],[[11,10]],[[14,8]],[[11,2]],[[11,10]]]'
#
# You are given a stream of points on the X-Y plane. Design an algorithm
# that:
#
#
# Adds new points from the stream into a data structure. Duplicate points are
# allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from
# the data structure such that the three points and the query point form an
# axis-aligned square with positive area.
#
#
# An axis-aligned square is a square whose edges are all the same length and
# are either parallel or perpendicular to the x-axis and y-axis.
#
# Implement the DetectSquares class:
#
#
# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data
# structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares
# with point point = [x, y] as described above.
#
#
#
# Example 1:
#
#
# Input
# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
# [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11,
# 10]]]
# Output
# [null, null, null, null, 1, 0, null, 2]
#
# Explanation
# DetectSquares detectSquares = new DetectSquares();
# detectSquares.add([3, 10]);
# detectSquares.add([11, 2]);
# detectSquares.add([3, 2]);
# detectSquares.count([11, 10]); // return 1. You can choose:
# ⁠                              //   - The first, second, and third points
# detectSquares.count([14, 8]);  // return 0. The query point cannot form a
# square with any points in the data structure.
# detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
# detectSquares.count([11, 10]); // return 2. You can choose:
# ⁠                              //   - The first, second, and third points
# ⁠                              //   - The first, third, and fourth points
#
#
#
# Constraints:
#
#
# point.length == 2
# 0 <= x, y <= 1000
# At most 3000 calls in total will be made to add and count.
#
#
#
from collections import Counter
from typing import List

# @lc code=start
class DetectSquares:

    # add: O(1)
    # count: O(1)
    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x, y] += 1

    # <= O(1000)
    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        if len(self.points) < 1000:
            for (i, j), cnt in self.points.items():
                if i == x or j == y or abs(x - i) != abs(y - j):
                    continue
                res += cnt * self.points[i, y] * self.points[x, j]
            return res

        for i in range(0, 1001):
            if i == x:
                continue
            d = abs(x - i)
            for j in [y + d, y - d]:
                res += self.points[i, j] * self.points[x, j] * self.points[i, y]

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end
def test():
    print("Testing DetectSquares")
    null = None
    cases = [
        (
            [
                [
                    "DetectSquares",
                    "add",
                    "add",
                    "add",
                    "count",
                    "count",
                    "add",
                    "count",
                ],
                [
                    [],
                    [[3, 10]],
                    [[11, 2]],
                    [[3, 2]],
                    [[11, 10]],
                    [[14, 8]],
                    [[11, 2]],
                    [[11, 10]],
                ],
            ],
            [null, null, null, null, 1, 0, null, 2],
        )
    ]
    for (actions, args), wants in cases:
        obj = DetectSquares()
        for action, arg, want in zip(actions[1:], args[1:], wants[1:]):
            got = getattr(obj, action)(*arg)
            assert got == want, f"{action}({arg}): {got} != {want}"
    print("  All Passed")


if __name__ == "__main__":
    test()
