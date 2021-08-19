#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#
# https://leetcode.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (51.50%)
# Likes:    1912
# Dislikes: 146
# Total Accepted:    67.8K
# Total Submissions: 130.2K
# Testcase Example:  '[3,4,2]'
#
# You are given an integer array nums. You want to maximize the number of
# points you get by performing the following operation any number of
# times:
#
#
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must
# delete every element equal to nums[i] - 1 and every element equal to nums[i]
# + 1.
#
#
# Return the maximum number of points you can earn by applying the above
# operation some number of times.
#
#
# Example 1:
#
#
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
#
#
# Example 2:
#
#
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums =
# [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] <= 10^4
#
#
#
from collections import Counter
from typing import List

# @lc code=start
class Solution:
    # O(n^2), O(n), TLE
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)

        def backtracking(curr: int) -> int:
            res = curr
            for point, cnt in counter.items():
                if cnt > 0:
                    p, n = None, None
                    if point-1 in counter and counter[point-1] > 0:
                        p = counter[point-1]
                        counter[point-1] = 0
                    if point+1 in counter and counter[point+1] > 0:
                        n = counter[point+1]
                        counter[point+1] = 0

                    counter[point] = 0
                    res = max(res, backtracking(curr+point*cnt))
                    counter[point] = cnt

                    if p:
                        counter[point-1] = p
                    if n:
                        counter[point+1] = n
            return res

        return backtracking(0)

    # same as 198(house-robber)
    # O(n+k), O(k). k = max(nums)-min(nums)
    def deleteAndEarn2(self, nums: List[int]) -> int:
        counter = Counter()
        start = end = 0
        for num in nums:
            counter[num] += 1
            start = min(start, num)
            end = max(end, num)

        pre, curr = 0, start
        for point in range(start+1, end+1):
            pre, curr = curr, max(pre+counter[point]*point, curr)
        return curr

# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith('__')]
    for method in methods:
        print(f'Testing {method}:')
        func = getattr(sol, method)
        cases = [
            ([[1]], 1),
            ([[1,2]], 2),
            ([[1,1,1,1]], 4),
            ([[1,3,5]], 9),
            ([[3,4,2]], 6),
            ([[2,2,3,3,3,4]], 9)
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
