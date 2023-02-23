#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#
# https://leetcode.com/problems/heaters/description/
#
# algorithms
# Medium (33.98%)
# Likes:    1012
# Dislikes: 960
# Total Accepted:    77K
# Total Submissions: 225.5K
# Testcase Example:  '[1,2,3]\n[2]'
#
# Winter is coming! During the contest, your first job is to design a standard
# heater with a fixed warm radius to warm all the houses.
#
# Every house can be warmed, as long as the house is within the heater's warm
# radius range.
#
# Given the positions of houses and heaters on a horizontal line, return the
# minimum radius standard of heaters so that those heaters could cover all
# houses.
#
# Notice that all the heaters follow your radius standard, and the warm radius
# will the same.
#
#
# Example 1:
#
#
# Input: houses = [1,2,3], heaters = [2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the
# radius 1 standard, then all the houses can be warmed.
#
#
# Example 2:
#
#
# Input: houses = [1,2,3,4], heaters = [1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to
# use radius 1 standard, then all the houses can be warmed.
#
#
# Example 3:
#
#
# Input: houses = [1,5], heaters = [2]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= houses.length, heaters.length <= 3 * 10^4
# 1 <= houses[i], heaters[i] <= 10^9
#
#
#
import bisect
# @lc code=start
import sys
from typing import List


class Solution:
    # m, n = len(houses), len(heaters)
    # O(n*long(n)) + O(m*log(n))
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = -sys.maxsize
        for house in houses:
            index = bisect.bisect_right(heaters, house)
            to_left = house - heaters[index - 1] if index > 0 else sys.maxsize
            to_right = heaters[index] - house if index < len(
                heaters) else sys.maxsize

            res = max(res, min(to_left, to_right))

        return res

    # m, n = len(houses), len(heaters)
    # m*log(m) + n*log(n) + O(log(max(max(houses), max(heaters)))*n*log(m))
    def findRadius1(self, houses: List[int], heaters: List[int]) -> int:

        def in_range(rad: int) -> bool:
            last_right = 0
            for heater in heaters:
                left = bisect.bisect_left(houses, heater - rad)
                if left > last_right:
                    return False
                last_right = bisect.bisect_right(houses, heater + rad)
                if last_right >= len(houses):
                    return True
            return False

        houses.sort()
        heaters.sort()
        left, right = 0, max(houses[-1], heaters[-1])
        while left <= right:
            mid = (right + left) // 2
            if in_range(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1, 2, 3], [2]], 1),
            ([[1, 2, 3, 4], [1, 4]], 1),
            ([[1, 5], [2]], 3),
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
