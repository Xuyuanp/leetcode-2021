#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
#
# algorithms
# Medium (53.92%)
# Likes:    1630
# Dislikes: 92
# Total Accepted:    86.6K
# Total Submissions: 159.9K
# Testcase Example:  '[[1,2],[2,3],[3,4]]'
#
# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and
# lefti < righti.
#
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can
# be formed in this fashion.
#
# Return the length longest chain which can be formed.
#
# You do not need to use up all the given intervals. You can select pairs in
# any order.
#
#
# Example 1:
#
#
# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
#
#
# Example 2:
#
#
# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: the longest chain is [1,2] -> [4,5] -> [7,8].
#
#
#
# Constraints:
#
#
# n == pairs.length
# 1 <= n <= 1000
# -1000 <= lefti < righti < 1000
#
#
#
from typing import List

# @lc code=start
class Solution:
    # O(n*log(n)), O(n). greedy
    def findlongestchain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: p[1])
        pre, res = pairs[0], 1
        for curr in pairs[1:]:
            if curr[0] > pre[1]:
                res += 1
                pre = curr
        return res

    # O(n*log(n)), O(n). binary search
    def findlongestchain1(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        lis = [pairs[0][1]]

        def binary_search(val: int) -> int:
            left, right = 0, len(lis)
            while left < right:
                mid = (left + right) // 2
                if lis[mid] < val:
                    left = mid + 1
                else:
                    right = mid
            return left

        for pair in pairs[1:]:
            pos = binary_search(pair[1])
            if pos == len(lis):
                # tails[-1]: |--------|
                # case1:      |---------|            -> drop
                # case1:                 |-----|     -> append
                if pair[0] > lis[-1]:
                    lis.append(pair[1])
            else:
                # tails[pos]:   |-------|
                # case1         |---|     -> replace
                # case2          |---|    -> replace
                lis[pos] = pair[1]
        return len(lis)

    # O(n*log(n)), O(n). binary search
    def findlongestchain2(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: p[1])
        lis = [pairs[0]]

        def binary_search(val: int) -> int:
            left, right = 0, len(lis)
            while left < right:
                mid = (left + right) // 2
                if lis[mid][1] < val:
                    left = mid + 1
                else:
                    right = mid
            return left

        for pair in pairs[1:]:
            pos = binary_search(pair[0])
            if pos == len(
                lis
            ):  # binary search is not needed. only compare with lis[-1] ==> greedy
                # tails[-1]: |--------|
                # case1:                 |-----|     -> append
                lis.append(pair)
            # else:
            # tails[pos]:   |-------|
            # case1          |---------|     -> drop
        return len(lis)


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[[1, 2]]], 1),
            ([[[1, 2], [3, 4]]], 2),
            ([[[1, 2], [2, 3]]], 1),
            ([[[1, 2], [2, 3], [3, 4]]], 2),
            ([[[1, 2], [7, 8], [4, 5]]], 3),
            ([[[1, 2], [1, 3], [1, 4], [10, 11]]], 2),
            (
                [
                    [
                        [-6, 9],
                        [1, 6],
                        [8, 10],
                        [-1, 4],
                        [-6, -2],
                        [-9, 8],
                        [-5, 3],
                        [0, 3],
                    ]
                ],
                3,
            ),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()


if __name__ == "__main__":
    test()
