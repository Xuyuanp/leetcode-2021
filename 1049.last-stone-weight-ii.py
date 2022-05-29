#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#
# https://leetcode.com/problems/last-stone-weight-ii/description/
#
# algorithms
# Medium (47.54%)
# Likes:    1548
# Dislikes: 57
# Total Accepted:    39.1K
# Total Submissions: 81K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# You are given an array of integers stones where stones[i] is the weight of
# the i^th stone.
#
# We are playing a game with the stones. On each turn, we choose any two stones
# and smash them together. Suppose the stones have weights x and y with x <= y.
# The result of this smash is:
#
#
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has
# new weight y - x.
#
#
# At the end of the game, there is at most one stone left.
#
# Return the smallest possible weight of the left stone. If there are no stones
# left, return 0.
#
#
# Example 1:
#
#
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0, so the array converts to [1], then that's
# the optimal value.
#
#
# Example 2:
#
#
# Input: stones = [31,26,33,21,40]
# Output: 5
#
#
# Example 3:
#
#
# Input: stones = [1,2]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 100
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(n*sum(stones)*2), O(sum(stones)*2)
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        for stone in stones:
            next_dp = set()
            for s in dp:
                next_dp.add(s + stone)
                next_dp.add(s - stone)
            dp = next_dp
        return min(abs(s) for s in dp)

    # O(n*sum(stones)), O(sum(stones))
    def lastStoneWeightII1(self, stones: List[int]) -> int:
        # sum(S1) + sum(S2) = sum(S)
        # sum(S1) - sum(S2) = diff
        # 2*sum(S1) = diff + sum(S)
        # diff = 2*sum(S1) - sum(S)
        # => find the min abs(diff)
        dp = {0}
        total = 0
        for stone in stones:
            total += stone
            dp |= {s + stone for s in dp}

        return min(abs(s * 2 - total) for s in dp)

    # equivalent to lastStoneWeightII
    def lastStoneWeightII2(self, stones: List[int]) -> int:
        total = sum(stones)
        offset = total
        dp = [False] * (total * 2 + 1)
        dp[offset] = True
        for stone in stones:
            next_dp = [False] * (total * 2 + 1)
            for s, ok in enumerate(dp):
                if ok:
                    next_dp[s + stone] = True
                    next_dp[s - stone] = True
            dp = next_dp
        return min(abs(s - offset) for s, ok in enumerate(dp) if ok)

    # equivalent to lastStoneWeightII1
    def lastStoneWeightII3(self, stones: List[int]) -> int:
        total = sum(stones)
        dp = [False] * (total + 1)
        dp[0] = True
        for stone in stones:
            next_dp = list(dp)
            for s, ok in enumerate(dp):
                if ok:
                    next_dp[s + stone] = True
            dp = next_dp

        return min(abs(s * 2 - total) for s, ok in enumerate(dp) if ok)

    # equivalent to lastStoneWeightII3
    def lastStoneWeightII4(self, stones: List[int]) -> int:
        total = sum(stones)
        dp = [False] * (total + 1)
        dp[0] = True
        for stone in stones:
            for s in range(len(dp) - 1, stone - 1, -1):
                dp[s] = dp[s] or dp[s - stone]

        return min(abs(s * 2 - total) for s, ok in enumerate(dp) if ok)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[1, 2]], 1),
            ([[1, 2, 3]], 0),
            ([[1, 2, 3, 4]], 0),
            ([[31, 26, 33, 21, 40]], 5),
            ([[2, 7, 4, 1, 8, 1]], 1),
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
