#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (35.16%)
# Likes:    2089
# Dislikes: 222
# Total Accepted:    184K
# Total Submissions: 518.9K
# Testcase Example:  '[1,0,2]'
#
# There are n children standing in a line. Each child is assigned a rating
# value given in the integer array ratings.
#
# You are giving candies to these children subjected to the following
# requirements:
#
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
#
#
# Return the minimum number of candies you need to have to distribute the
# candies to the children.
#
#
# Example 1:
#
#
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
#
#
# Example 2:
#
#
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two
# conditions.
#
#
#
# Constraints:
#
#
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4
#
#
#
from typing import List

# @lc code=start
class Solution:
    # same as candy3, but more readable
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ratings.append(-1)
        res = 0
        i = 0
        pre = 0

        while i < n:
            j = i
            while j < n and ratings[j] == ratings[j-1]:
                pre = 1
                res += 1
                j += 1

            while j < n and ratings[j] > ratings[j-1]:
                pre += 1
                res += pre
                j += 1

            top = j
            while j < n and ratings[j] < ratings[j-1]:
                pre -= 1
                res += pre
                j += 1

            if pre > 1:
                res -= (pre-1) * (j-top)
            elif pre < 1:
                res -= (pre-1) * (j-top+1)

            pre = 1
            i = j

        return res

    # O(n), O(1)
    def candy3(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = 0
        i = 0
        while i < n:
            j = i
            pre = 1 if i > 0 and ratings[i] > ratings[i-1] else 0
            # increasing sequence
            while j < n:
                pre += 1
                res += pre
                if j+1 == n or ratings[j] >= ratings[j+1]:
                    break
                j += 1

            if j + 1 == n:
                break

            # decreacing sequence
            k = j + 1
            while k < n and ratings[k] < ratings[k-1]:
                pre -= 1
                res += pre
                k += 1

            if k - j > 1:
                if pre > 1:
                    #
                    #            *
                    #          * * *
                    #        * * * * *
                    #      * * * * - -
                    # 0 ---------------------------
                    #      1 2 3 4 2 1
                    #
                    res -= (pre-1) * (k-j-1)
                elif pre < 1:
                    #
                    #
                    #          *
                    #        * * *
                    #      * * * * *
                    # 0 -------+-+-+-+-+-----------
                    #          + + + + +
                    #      1 2 5 4 3 2 1
                    #
                    res += (1-pre) * (k-j)

            i = k

        return res

    # O(n), O(n)
    def candy2(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                candies[i] = candies[i-1] + 1

        pre = 1
        res = max(candies[-1], pre)
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                pre+=1
                candies[i] = max(candies[i], pre)
            else:
                pre = 1
            res += candies[i]

        return res

    # O(n), O(n)
    def candy1(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies_left = [1] * n
        candies_right = [1] * n
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                candies_left[i] = candies_left[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies_right[i] = candies_right[i+1] + 1

        return sum(max(candies_left[i], candies_right[i]) for i in range(n))


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        fn = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[1,1,1,1]], 4),
            ([[1,2,4,3,2,1]], 13),
            ([[1,2,4,3,2]], 9),
            ([[1,0,2]], 5),
            ([[1,2,2]], 4),
            ([[1,2,3]], 6),
            ([[3,2,1]], 6),
            ([[2,2,2,1]], 5),
            ([[1,2,2,4,3,2,2,1]], 13),
            ([[1,3,4,5,2]], 11),
            ([[1,2,3,1]], 7),
            ([[1,2,3,1,2,3]], 12),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f'  Failed => args: {args}; want: {want}, but got: {got}')
                break
        else:
            print('  All Passed')
        print()


if __name__ == '__main__':
    main()
