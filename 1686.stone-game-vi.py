#
# @lc app=leetcode id=1686 lang=python3
#
# [1686] Stone Game VI
#
# https://leetcode.com/problems/stone-game-vi/description/
#
# algorithms
# Medium (51.33%)
# Likes:    334
# Dislikes: 25
# Total Accepted:    7.9K
# Total Submissions: 15.2K
# Testcase Example:  '[1,3]\n[2,1]'
#
# Alice and Bob take turns playing a game, with Alice starting first.
#
# There are n stones in a pile. On each player's turn, they can remove a stone
# from the pile and receive points based on the stone's value. Alice and Bob
# may value the stones differently.
#
# You are given two integer arrays of length n, aliceValues and bobValues. Each
# aliceValues[i] and bobValues[i] represents how Alice and Bob, respectively,
# value the i^th stone.
#
# The winner is the person with the most points after all the stones are
# chosen. If both players have the same amount of points, the game results in a
# draw. Both players will play optimally. Both players know the other's
# values.
#
# Determine the result of the game, and:
#
#
# If Alice wins, return 1.
# If Bob wins, return -1.
# If the game results in a draw, return 0.
#
#
#
# Example 1:
#
#
# Input: aliceValues = [1,3], bobValues = [2,1]
# Output: 1
# Explanation:
# If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
# Bob can only choose stone 0, and will only receive 2 points.
# Alice wins.
#
#
# Example 2:
#
#
# Input: aliceValues = [1,2], bobValues = [3,1]
# Output: 0
# Explanation:
# If Alice takes stone 0, and Bob takes stone 1, they will both have 1 point.
# Draw.
#
#
# Example 3:
#
#
# Input: aliceValues = [2,4,3], bobValues = [1,6,7]
# Output: -1
# Explanation:
# Regardless of how Alice plays, Bob will be able to have more points than
# Alice.
# For example, if Alice takes stone 1, Bob can take stone 2, and Alice takes
# stone 0, Alice will have 6 points to Bob's 7.
# Bob wins.
#
#
#
# Constraints:
#
#
# n == aliceValues.length == bobValues.length
# 1 <= n <= 10^5
# 1 <= aliceValues[i], bobValues[i] <= 100
#
#
#
from typing import List


# @lc code=start
class Solution:
    # O(n*log(n)), O(n)
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)

        indexes = sorted(list(range(n)),
                         key=lambda i: aliceValues[i] + bobValues[i],
                         reverse=True)

        values = [aliceValues, bobValues]
        points = [0, 0]
        player = 0

        for i in indexes:
            points[player] += values[player][i]
            player = (player + 1) % 2

        diff = points[0] - points[1]
        return 1 if diff > 0 else -1 if diff < 0 else 0


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1], [2]], 1),
            ([[1, 3], [2, 1]], 1),
            ([[1, 2], [3, 1]], 0),
            ([[2, 4, 3], [1, 6, 7]], -1),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(
                    f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
