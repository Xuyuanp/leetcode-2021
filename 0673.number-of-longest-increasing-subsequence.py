#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (38.92%)
# Likes:    2590
# Dislikes: 133
# Total Accepted:    85.7K
# Total Submissions: 219.3K
# Testcase Example:  '[1,3,5,4,7]'
#
# Given an integer array nums, return the number of longest increasing
# subsequences.
#
# Notice that the sequence has to be strictly increasing.
#
#
# Example 1:
#
#
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1,
# 3, 5, 7].
#
#
# Example 2:
#
#
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1,
# and there are 5 subsequences' length is 1, so output 5.
#
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2000
# -10^6 <= nums[i] <= 10^6
#
#
#
from typing import List

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lis = [[[nums[0], 1]]]

        def binary_search(x: int) -> int:
            left, right = 0, len(lis)
            while left < right:
                mid = (left + right) // 2
                if lis[mid][-1][0] < x:
                    left = mid + 1
                else:
                    right = mid
            return left

        for x in nums[1:]:  # n*log(n)
            pos = binary_search(x)  # log(k)
            cnt = 1 if pos == 0 else sum(cnt for v, cnt in lis[pos - 1] if v < x)
            if pos == len(lis):
                lis.append([[x, cnt]])
            else:
                lis[pos].append([x, cnt])

        return sum(t[1] for t in lis[-1])


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
            ([[2, 1]], 2),
            ([[1, 1]], 2),
            ([[3, 1, 2]], 1),
            ([[1, 2, 6, 4, 5]], 1),
            ([[1, 3, 2]], 2),
            ([[1, 3, 5, 4, 7]], 2),
            ([[2, 2, 2, 2, 2]], 5),
            ([[1, 2, 4, 3, 5, 4, 7, 2]], 3),
            ([[1, 1, 1, 2, 2, 2, 3, 3, 3]], 27),
            ([[1, 2, 3, 1, 2, 3, 1, 2, 3]], 10),
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
