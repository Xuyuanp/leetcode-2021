#
# @lc app=leetcode id=801 lang=python3
#
# [801] Minimum Swaps To Make Sequences Increasing
#
# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description/
#
# algorithms
# Hard (38.72%)
# Likes:    1684
# Dislikes: 120
# Total Accepted:    45.7K
# Total Submissions: 117.5K
# Testcase Example:  '[1,3,5,4]\n[1,2,3,7]'
#
# You are given two integer arrays of the same length nums1 and nums2. In one
# operation, you are allowed to swap nums1[i] with nums2[i].
#
#
# For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the
# element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
#
#
# Return the minimum number of needed operations to make nums1 and nums2
# strictly increasing. The test cases are generated so that the given input
# always makes it possible.
#
# An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] <
# ... < arr[arr.length - 1].
#
#
# Example 1:
#
#
# Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
# Output: 1
# Explanation:
# Swap nums1[3] and nums2[3]. Then the sequences are:
# nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
# which are both strictly increasing.
#
#
# Example 2:
#
#
# Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
# Output: 1
#
#
#
# Constraints:
#
#
# 2 <= nums1.length <= 10^5
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 2 * 10^5
#
#
#
from typing import List

# @lc code=start

KEEP, SWAP = 0, 1


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        prev = [0, 1]
        curr = [0, 0]
        for i in range(1, len(nums1)):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                curr[KEEP] = prev[KEEP]
                curr[SWAP] = prev[SWAP] + 1
            else:
                curr[KEEP] = prev[SWAP]
                curr[SWAP] = prev[KEEP] + 1

            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                curr[KEEP] = min(curr[KEEP], prev[SWAP])
                curr[SWAP] = min(curr[SWAP], prev[KEEP] + 1)

            prev[KEEP] = curr[KEEP]
            prev[SWAP] = curr[SWAP]

        return min(curr)

    def minSwap1(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums1))]
        dp[0][SWAP] = 1

        for i in range(1, len(nums1)):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                dp[i][KEEP] = dp[i - 1][KEEP]
                dp[i][SWAP] = dp[i - 1][SWAP] + 1
            else:
                dp[i][KEEP] = dp[i - 1][SWAP]
                dp[i][SWAP] = dp[i - 1][KEEP] + 1

            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                dp[i][KEEP] = min(dp[i - 1][SWAP], dp[i][KEEP])
                dp[i][SWAP] = min(dp[i - 1][KEEP] + 1, dp[i][SWAP])

        return min(dp[-1])


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[1, 2], [3, 4]], 0),
            ([[3, 2], [1, 4]], 1),
            ([[1, 3, 5, 4], [1, 2, 3, 7]], 1),
            ([[0, 3, 5, 8, 9], [2, 1, 4, 6, 9]], 1),
            ([[0, 4, 4, 5, 9], [0, 1, 6, 8, 10]], 1),
        ]
        for args, want in cases:
            got = fn(*args)
            if want != got:
                print(f"  Failed => args: {args}; want: {want}, but got: {got}")
                break
        else:
            print("  All Passed")
        print()
