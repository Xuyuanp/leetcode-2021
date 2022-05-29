#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#
# https://leetcode.com/problems/fruit-into-baskets/description/
#
# algorithms
# Medium (43.19%)
# Likes:    230
# Dislikes: 12
# Total Accepted:    149.3K
# Total Submissions: 345.5K
# Testcase Example:  '[1,2,1]'
#
# You are visiting a farm that has a single row of fruit trees arranged from
# left to right. The trees are represented by an integer array fruits where
# fruits[i] is the type of fruit the i^th tree produces.
#
# You want to collect as much fruit as possible. However, the owner has some
# strict rules that you must follow:
#
#
# You only have two baskets, and each basket can only hold a single type of
# fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from
# every tree (including the start tree) while moving to the right. The picked
# fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must
# stop.
#
#
# Given the integer array fruits, return the maximum number of fruits you can
# pick.
#
#
# Example 1:
#
#
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
#
#
# Example 2:
#
#
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
#
#
# Example 3:
#
#
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
#
#
# Example 4:
#
#
# Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can pick from trees [1,2,1,1,2].
#
#
#
# Constraints:
#
#
# 1 <= fruits.length <= 10^5
# 0 <= fruits[i] < fruits.length
#
#
#
from collections import defaultdict
from typing import List

# @lc code=start
K = 2


class Solution:
    # O(n), O(1). sliding window
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        baskets = defaultdict(int)
        left = 0
        hold = 0
        for fruit in fruits:
            if fruit not in baskets and len(baskets) == K:
                while len(baskets) == K:
                    f = fruits[left]
                    baskets[f] -= 1
                    hold -= 1
                    if baskets[f] == 0:
                        del baskets[f]
                    left += 1

            baskets[fruit] += 1
            hold += 1
            res = max(res, hold)

        return res


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[0, 1, 2, 2]], 3),
            ([[1, 2, 3, 2, 2]], 4),
            ([[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]], 5),
            ([[1, 0, 3, 4, 3]], 3),
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
