#
# @lc app=leetcode id=470 lang=python3
#
# [470] Implement Rand10() Using Rand7()
#
# https://leetcode.com/problems/implement-rand10-using-rand7/description/
#
# algorithms
# Medium (46.17%)
# Likes:    736
# Dislikes: 246
# Total Accepted:    52K
# Total Submissions: 112.6K
# Testcase Example:  '1'
#
# Given the API rand7() that generates a uniform random integer in the range
# [1, 7], write a function rand10() that generates a uniform random integer in
# the range [1, 10]. You can only call the API rand7(), and you shouldn't call
# any other API. Please do not use a language's built-in random API.
#
# Each test case will have one internal argument n, the number of times that
# your implemented function rand10() will be called while testing. Note that
# this is not an argument passed to rand10().
#
# Follow up:
#
#
# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?
#
#
#
# Example 1:
# Input: n = 1
# Output: [2]
# Example 2:
# Input: n = 2
# Output: [2,8]
# Example 3:
# Input: n = 3
# Output: [3,8,10]
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
#
#
#
from random import randint
import statistics

def rand7():
    return randint(1, 7)

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    # (40/49 + 9/49 * 60/63 + 9/49 * 3/63 * 20/21)/10 ~= 0.09996
    # expect: 3 * 40/49 + 3 * 9/49 * 60/63 + 4 * 9/49 * 3/63 + 5 * 9/49 * 3/63 * 20/21 + (...) ~= 2.23
    def rand10(self) -> int:
        while True:
            row, col = rand7(), rand7()
            n = (row-1)*7 + col
            if n <= 40:
                return (n-1)%10 + 1
            n = (n-40-1)*7 + rand7()
            if n <= 60:
                return (n-1)%10 + 1
            n = (n-60-1)*7 + rand7()
            if n <= 20:
                return (n-1)%10 + 1

# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    counter = [0] * 10
    counter2 = [0] * 10
    N = 1_000_000
    for _ in range(N):
        counter[sol.rand10()-1] += 1
        counter2[randint(0, 9)] += 1

    print(counter)
    print(statistics.stdev(counter))
    print(counter2)
    print(statistics.stdev(counter2))
