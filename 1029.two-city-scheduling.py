#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#
# https://leetcode.com/problems/two-city-scheduling/description/
#
# algorithms
# Medium (58.59%)
# Likes:    2041
# Dislikes: 205
# Total Accepted:    119.6K
# Total Submissions: 203.5K
# Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'
#
# A company is planning to interview 2n people. Given the array costs where
# costs[i] = [aCosti, bCosti], the cost of flying the i^th person to city a is
# aCosti, and the cost of flying the i^th person to city b is bCosti.
#
# Return the minimum cost to fly every person to a city such that exactly n
# people arrive in each city.
#
#
# Example 1:
#
#
# Input: costs = [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation:
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
#
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
# interviewing in each city.
#
#
# Example 2:
#
#
# Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# Output: 1859
#
#
# Example 3:
#
#
# Input: costs =
# [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
# Output: 3086
#
#
#
# Constraints:
#
#
# 2 * n == costs.length
# 2 <= costs.length <= 100
# costs.length is even.
# 1 <= aCosti, bCosti <= 1000
#
#
#
import heapq
from typing import List


# @lc code=start
class Solution:
    # let all persons go to city B, the total cost is sum(costs[i][1])
    # let n of them go to city A, delta is price_a - price_b
    # so we should find the n smallest price_a - price_b
    # O(N*log(N)), O(N), N=len(costs) = 2*n
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        heap = []
        A, B = 0, 1

        for i, cost in enumerate(costs):
            heapq.heappush(heap, (cost[A] - cost[B], i))
        res = 0

        for _ in range(n):
            _, i = heapq.heappop(heap)
            res += costs[i][A]
        for _ in range(n):
            _, i = heapq.heappop(heap)
            res += costs[i][B]

        return res

    # O(N*log(n)), O(n), N=2*n
    def twoCitySchedCost1(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        A, B = 0, 1
        heap = []
        res = 0

        for i in range(n):
            cost = costs[i]
            res += cost[A]
            heapq.heappush(heap, (cost[B] - cost[A], i))

        for i in range(n, 2 * n):
            cost = costs[i]
            curr = (cost[B] - cost[A], i)
            top = heap[0]
            if curr[0] > top[0]:
                heapq.heapreplace(heap, curr)
                res += top[0] + cost[A]
            else:
                res += cost[B]

        return res

    # O(N*log(N)), O(N), N=2*n
    def twoCitySchedCost2(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        A, B = 0, 1
        costs.sort(key=lambda c: c[A] - c[B])
        res = sum(costs[i][A] for i in range(n))
        for i in range(n, 2 * n):
            res += costs[i][B]

        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[[10, 20], [30, 40]]], 50),
            ([[[10, 20], [40, 30]]], 40),
            ([[[10, 20], [30, 200], [400, 50], [30, 20]]], 110),
            (
                [[
                    [259, 770],
                    [448, 54],
                    [926, 667],
                    [184, 139],
                    [840, 118],
                    [577, 469],
                ]],
                1859,
            ),
            (
                [[
                    [515, 563],
                    [451, 713],
                    [537, 709],
                    [343, 819],
                    [855, 779],
                    [457, 60],
                    [650, 359],
                    [631, 42],
                ]],
                3086,
            ),
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
