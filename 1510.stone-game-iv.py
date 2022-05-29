#
# @lc app=leetcode id=1510 lang=python3
#
# [1510] Stone Game IV
#
# https://leetcode.com/problems/stone-game-iv/description/
#
# algorithms
# Hard (59.19%)
# Likes:    488
# Dislikes: 28
# Total Accepted:    29.9K
# Total Submissions: 50.5K
# Testcase Example:  '1\r'
#
# Alice and Bob take turns playing a game, with Alice starting first.
#
# Initially, there are n stones in a pile.  On each player's turn, that player
# makes a move consisting of removing any non-zero square number of stones in
# the pile.
#
# Also, if a player cannot make a move, he/she loses the game.
#
# Given a positive integer n. Return True if and only if Alice wins the game
# otherwise return False, assuming both players play optimally.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: true
# Explanation: Alice can remove 1 stone winning the game because Bob doesn't
# have any moves.
#
# Example 2:
#
#
# Input: n = 2
# Output: false
# Explanation: Alice can only remove 1 stone, after that Bob removes the last
# one winning the game (2 -> 1 -> 0).
#
# Example 3:
#
#
# Input: n = 4
# Output: true
# Explanation: n is already a perfect square, Alice can win with one move,
# removing 4 stones (4 -> 0).
#
#
# Example 4:
#
#
# Input: n = 7
# Output: false
# Explanation: Alice can't win the game if Bob plays optimally.
# If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should
# remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 ->
# 0).
# If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only
# can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 ->
# 0).
#
# Example 5:
#
#
# Input: n = 17
# Output: false
# Explanation: Alice can't win the game if Bob plays optimally.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
#
#
#

# @lc code=start
from functools import cache


class Solution:
    # O(n*sqrt(n)), O(n)
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def helper(i: int) -> bool:
            if i == 0:
                return False
            j = 1
            while (curr := j * j) <= i:
                if not helper(i - curr):
                    return True
                j += 1
            return False

        return helper(n)

    # O(n*sqrt(n)), O(n)
    def winnerSquareGame1(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            while (curr := j * j) <= i:
                if not dp[i - curr]:
                    dp[i] = True
                    break
                j += 1
        return dp[n]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([1], True),
            ([2], False),
            ([3], True),
            ([4], True),
            ([5], False),
            ([6], True),
            ([7], False),
            ([8], True),
            ([9], True),
            ([17], False),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
