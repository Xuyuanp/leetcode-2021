#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#
# https://leetcode.com/problems/open-the-lock/description/
#
# algorithms
# Medium (54.73%)
# Likes:    2082
# Dislikes: 71
# Total Accepted:    122.1K
# Total Submissions: 223.1K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# You have a lock in front of you with 4 circular wheels. Each wheel has 10
# slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can
# rotate freely and wrap around: for example we can turn '9' to be '0', or '0'
# to be '9'. Each move consists of turning one wheel one slot.
#
# The lock initially starts at '0000', a string representing the state of the 4
# wheels.
#
# You are given a list of deadends dead ends, meaning if the lock displays any
# of these codes, the wheels of the lock will stop turning and you will be
# unable to open it.
#
# Given a target representing the value of the wheels that will unlock the
# lock, return the minimum total number of turns required to open the lock, or
# -1 if it is impossible.
#
#
# Example 1:
#
#
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" ->
# "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202"
# would be invalid,
# because the wheels of the lock become stuck after the display becomes the
# dead end "0102".
#
#
# Example 2:
#
#
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation:
# We can turn the last wheel in reverse to move from "0000" -> "0009".
#
#
# Example 3:
#
#
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# Output: -1
# Explanation:
# We can't reach the target without getting stuck.
#
#
# Example 4:
#
#
# Input: deadends = ["0000"], target = "8888"
# Output: -1
#
#
#
# Constraints:
#
#
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target will not be in the list deadends.
# target and deadends[i] consist of digits only.
#
#
#
from collections import deque
from typing import List

# @lc code=start
neighbours = {
    str(i): [str((i + 1) % 10), str((i - 1) % 10)]
    for i in range(10)
}


class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        seen = set(deadends)
        if "0000" in seen:
            return -1
        queue = deque()
        queue.append(("0000", 0))
        seen.add("0000")
        while queue:
            val, turns = queue.popleft()
            for i in range(4):
                for n in neighbours[val[i]]:
                    new_val = val[:i] + n + val[i + 1:]
                    if new_val == target:
                        return turns + 1
                    if new_val not in seen:
                        seen.add(new_val)
                        queue.append((new_val, turns + 1))
        return -1


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ((["8888"], "0000"), 0),
        ((["0201", "0101", "0102", "1212", "2002"], "0202"), 6),
        ((["8888"], "0009"), 1),
        (
            (["8887", "8889", "8878", "8898", "8788", "8988", "7888",
              "9888"], "8888"),
            -1,
        ),
        ((["0201", "0101", "0102", "1212", "2002"], "0202"), 6),
    ]
    for (deadends, target), want in cases:
        got = sol.openLock(deadends, target)
        if got != want:
            print(
                f"Failed => args: {deadends}, {target}; want: {want}, but got: {got}"
            )
            break
    else:
        print("All Passed")
