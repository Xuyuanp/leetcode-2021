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
    # O(n*)
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {stones[0], -stones[0]}
        for stone in stones[1:]:
            next_dp = set()
            for s in dp:
                next_dp.add(s+stone)
                next_dp.add(s-stone)
            dp = next_dp
        return min(abs(s) for s in dp)

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[1,2]], 1),
            ([[1,2,3]], 0),
            ([[1,2,3,4]], 0),
            ([[31,26,33,21,40]], 5),
            ([[2,7,4,1,8,1]], 1),
        ]
        for args, want in cases:
            got = func(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    test()
