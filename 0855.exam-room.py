#
# @lc app=leetcode id=855 lang=python3
#
# [855] Exam Room
#
# https://leetcode.com/problems/exam-room/description/
#
# algorithms
# Medium (43.41%)
# Likes:    810
# Dislikes: 324
# Total Accepted:    41.1K
# Total Submissions: 94.5K
# Testcase Example:  '["ExamRoom","seat","seat","seat","seat","leave","seat"]\n' +
#  '[[10],[],[],[],[],[4],[]]'
#
# There is an exam room with n seats in a single row labeled from 0 to n - 1.
#
# When a student enters the room, they must sit in the seat that maximizes the
# distance to the closest person. If there are multiple such seats, they sit in
# the seat with the lowest number. If no one is in the room, then the student
# sits at seat number 0.
#
# Design a class that simulates the mentioned exam room.
#
# Implement the ExamRoom class:
#
#
# ExamRoom(int n) Initializes the object of the exam room with the number of
# the seats n.
# int seat() Returns the label of the seat at which the next student will
# set.
# void leave(int p) Indicates that the student sitting at seat p will leave the
# room. It is guaranteed that there will be a student sitting at seat p.
#
#
#
# Example 1:
#
#
# Input
# ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
# [[10], [], [], [], [], [4], []]
# Output
# [null, 0, 9, 4, 2, null, 5]
#
# Explanation
# ExamRoom examRoom = new ExamRoom(10);
# examRoom.seat(); // return 0, no one is in the room, then the student sits at
# seat number 0.
# examRoom.seat(); // return 9, the student sits at the last seat number 9.
# examRoom.seat(); // return 4, the student sits at the last seat number 4.
# examRoom.seat(); // return 2, the student sits at the last seat number 2.
# examRoom.leave(4);
# examRoom.seat(); // return 5, the student sits at the last seat number
# 5.
#
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^9
# It is guaranteed that there is a student sitting at seat p.
# At most 10^4 calls will be made to seat and leave.
#
#
#

# @lc code=start
import heapq

START, END = 1, 2


class ExamRoom:

    def __init__(self, n: int):
        self.heap = []
        self.n = n
        heapq.heappush(self.heap, [-n + 1, -1, n])

    # O(log(n))
    def seat(self) -> int:
        _, start, end = heapq.heappop(self.heap)

        mid = 0 if start < 0 else self.n - 1 if end == self.n else (start +
                                                                    end) // 2

        heapq.heappush(self.heap, [-self._get_max_closed(mid, end), mid, end])
        heapq.heappush(self.heap,
                       [-self._get_max_closed(start, mid), start, mid])
        return mid

    def _get_max_closed(self, start: int, end: int) -> int:
        if start == -1:
            return end - 1
        if end == self.n:
            return self.n - start - 2
        dist = end - start - 1
        return (dist - 1) // 2 if dist % 2 == 0 else dist // 2

    def _remove_double(self, i: int, j: int):
        if i > j:
            i, j = j, i
        assert i < j < len(self.heap)

        if j == len(self.heap) - 1:
            self.heap.pop()
            self.heap[i] = self.heap[-1]
        else:
            self.heap[i] = self.heap[-1]
            self.heap.pop()
            self.heap[j] = self.heap[-1]
        self.heap.pop()
        heapq.heapify(self.heap)

    # O(n)
    def leave(self, p: int) -> None:
        firsti = lasti = -1
        for i, segment in enumerate(self.heap):
            if segment[END] == p:
                firsti = i
            if segment[START] == p:
                lasti = i
            if firsti >= 0 and lasti >= 0:
                break
        else:
            assert False, "unreachable"

        first, last = self.heap[firsti], self.heap[lasti]

        self._remove_double(firsti, lasti)

        start, end = first[START], last[END]
        heapq.heappush(self.heap,
                       [-self._get_max_closed(start, end), start, end])


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
# @lc code=end
def test():
    print("Testing ExamRoom")
    null = None
    cases = [
        (
            [
                [
                    "ExamRoom",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "leave",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "leave",
                    "seat",
                    "leave",
                    "seat",
                    "leave",
                    "leave",
                    "seat",
                    "seat",
                    "leave",
                    "seat",
                    "leave",
                    "seat",
                    "leave",
                    "seat",
                    "leave",
                ],
                [
                    [7],
                    [],
                    [],
                    [],
                    [],
                    [1],
                    [],
                    [],
                    [],
                    [],
                    [4],
                    [],
                    [5],
                    [],
                    [0],
                    [1],
                    [],
                    [],
                    [4],
                    [],
                    [6],
                    [],
                    [2],
                    [],
                    [0],
                ],
            ],
            [
                null,
                0,
                6,
                3,
                1,
                null,
                1,
                2,
                4,
                5,
                null,
                4,
                null,
                5,
                null,
                null,
                0,
                1,
                null,
                4,
                null,
                6,
                null,
                2,
                null,
            ],
        ),
        (
            [
                [
                    "ExamRoom", "seat", "seat", "seat", "seat", "leave",
                    "leave", "seat"
                ],
                [[4], [], [], [], [], [1], [3], []],
            ],
            [null, 0, 3, 1, 2, null, null, 1],
        ),
        (
            [
                [
                    "ExamRoom",
                    "seat",
                    "seat",
                    "seat",
                    "leave",
                    "leave",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "leave",
                ],
                [[10], [], [], [], [0], [4], [], [], [], [], [], [], [], [],
                 [], [0]],
            ],
            [None, 0, 9, 4, None, None, 0, 4, 2, 6, 1, 3, 5, 7, 8, None],
        ),
        (
            [
                [
                    "ExamRoom",
                    "seat",
                    "seat",
                    "seat",
                    "leave",
                    "leave",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "seat",
                    "leave",
                    "leave",
                    "seat",
                    "seat",
                    "leave",
                    "seat",
                    "leave",
                    "seat",
                    "leave",
                    "seat",
                    "leave",
                    "seat",
                    "leave",
                    "leave",
                    "seat",
                    "seat",
                    "leave",
                    "leave",
                    "seat",
                    "seat",
                    "leave",
                ],
                [
                    [10],
                    [],
                    [],
                    [],
                    [0],
                    [4],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [0],
                    [4],
                    [],
                    [],
                    [7],
                    [],
                    [3],
                    [],
                    [3],
                    [],
                    [9],
                    [],
                    [0],
                    [8],
                    [],
                    [],
                    [0],
                    [8],
                    [],
                    [],
                    [2],
                ],
            ],
            [
                None,
                0,
                9,
                4,
                None,
                None,
                0,
                4,
                2,
                6,
                1,
                3,
                5,
                7,
                8,
                None,
                None,
                0,
                4,
                None,
                7,
                None,
                3,
                None,
                3,
                None,
                9,
                None,
                None,
                0,
                8,
                None,
                None,
                0,
                8,
                None,
            ],
        ),
    ]
    for (actions, args), wants in cases:
        obj = ExamRoom(*args[0])
        for action, arg, want in zip(actions[1:], args[1:], wants[1:]):
            got = getattr(obj, action)(*arg)
            assert got == want, f"{action}, {arg}, {want}, {got}"
    print("  All Passed")


if __name__ == "__main__":
    test()
