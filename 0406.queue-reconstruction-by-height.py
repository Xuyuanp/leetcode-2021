#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (69.01%)
# Likes:    4290
# Dislikes: 470
# Total Accepted:    203.4K
# Total Submissions: 294K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# You are given an array of people, people, which are the attributes of some
# people in a queue (not necessarily in order). Each people[i] = [hi, ki]
# represents the i^th person of height hi with exactly ki other people in front
# who have a height greater than or equal to hi.
#
# Reconstruct and return the queue that is represented by the input array
# people. The returned queue should be formatted as an array queue, where
# queue[j] = [hj, kj] is the attributes of the j^th person in the queue
# (queue[0] is the person at the front of the queue).
#
#
# Example 1:
#
#
# Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# Explanation:
# Person 0 has height 5 with no other people taller or the same height in
# front.
# Person 1 has height 7 with no other people taller or the same height in
# front.
# Person 2 has height 5 with two persons taller or the same height in front,
# which is person 0 and 1.
# Person 3 has height 6 with one person taller or the same height in front,
# which is person 1.
# Person 4 has height 4 with four people taller or the same height in front,
# which are people 0, 1, 2, and 3.
# Person 5 has height 7 with one person taller or the same height in front,
# which is person 1.
# Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
#
#
# Example 2:
#
#
# Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
#
#
#
# Constraints:
#
#
# 1 <= people.length <= 2000
# 0 <= hi <= 10^6
# 0 <= ki < people.length
# It is guaranteed that the queue can be reconstructed.
#
#
#
from collections import deque
from typing import List


# @lc code=start
class Solution:
    # O(n*log(n) + n^2), O(log(n))
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = deque()
        H, K = 0, 1
        people.sort(key=lambda p: (-p[H], p[K]))
        for p in people:
            res.insert(p[K], p)
        return list(res)


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            (
                [[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]],
                [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
            ),
            (
                [[[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]],
                [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]],
            ),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    main()
