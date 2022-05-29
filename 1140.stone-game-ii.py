#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#
# https://leetcode.com/problems/stone-game-ii/description/
#
# algorithms
# Medium (64.59%)
# Likes:    928
# Dislikes: 210
# Total Accepted:    30.7K
# Total Submissions: 47.5K
# Testcase Example:  '[2,7,9,4,4]'
#
# Alice and Bob continue their games with piles of stones.  There are a number
# of piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].  The objective of the game is to end with the most stones.
#
# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
#
# On each player's turn, that player can take all the stones in the first X
# remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
#
# The game continues until all the stones have been taken.
#
# Assuming Alice and Bob play optimally, return the maximum number of stones
# Alice can get.
#
#
# Example 1:
#
#
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alice takes one pile at the beginning, Bob takes two piles,
# then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total.
# If Alice takes two piles at the beginning, then Bob can take all three piles
# left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since
# it's larger.
#
#
# Example 2:
#
#
# Input: piles = [1,2,3,4,5,100]
# Output: 104
#
#
#
# Constraints:
#
#
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10^4
#
#
#
from functools import cache
from typing import List, Tuple

# @lc code=start
class Solution:
    # O(n^3), O(n^2)
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # helper return the answer of piles[i:] and the given m
        @cache
        def helper(i: int, m: int) -> Tuple[int, int]:
            if i + m + m >= n:
                return sum(piles[i:]), 0
            res = (0, 0)
            curr = 0
            for x in range(1, m + m + 1):
                curr += piles[i + x - 1]
                other, rest = helper(i + x, max(m, x))
                res = max(res, (curr + rest, other))

            return res

        return helper(0, 1)[0]

    # O(n^3), O(n^2)
    def stoneGameII1(self, piles: List[int]) -> int:
        n = len(piles)

        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]

        # helper return the answer of piles[i:] and the given m
        @cache
        def helper(i: int, m: int) -> Tuple[int, int]:
            if i + m + m >= n:
                return piles[i], 0
            res = (0, 0)
            for x in range(1, m + m + 1):
                curr = piles[i] - piles[i + x]
                other, rest = helper(i + x, max(m, x))
                res = max(res, (curr + rest, other))

            return res

        return helper(0, 1)[0]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[1, 2]], 3),
            ([[1, 2, 3]], 3),
            ([[1, 2, 3, 4]], 5),
            ([[1, 2, 3, 4, 5]], 8),
            ([[2, 7, 9, 4, 4]], 10),
            ([[1, 2, 3, 4, 5, 100]], 104),
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
