#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (45.56%)
# Likes:    1672
# Dislikes: 98
# Total Accepted:    106K
# Total Submissions: 232.2K
# Testcase Example:  '2736'
#
# You are given an integer num. You can swap two digits at most once to get the
# maximum valued number.
#
# Return the maximum valued number you can get.
#
#
# Example 1:
#
#
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#
#
# Example 2:
#
#
# Input: num = 9973
# Output: 9973
# Explanation: No swap.
#
#
#
# Constraints:
#
#
# 0 <= num <= 10^8
#
#
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        zero = ord('0')
        s_num = str(num)
        mem = {ord(c)-zero: i for i, c in enumerate(s_num)}

        for i, c in enumerate(s_num):
            n = ord(c) - zero
            for j in range(9, n, -1):
                if j in mem and mem[j] > i:
                    c1, c2 = 10**(len(s_num)-mem[j]-1), 10**(len(s_num)-i-1)
                    num = num - n*c2 - j*c1 + j*c2 + n*c1
                    return num
        return num

# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    cases = [
        (1, 1),
        (12, 21),
        (21, 21),
        (2736, 7236),
        (9973, 9973),
        (1233, 3231),
        (122222, 222221),
        (98368, 98863),
    ]
    for num, want in cases:
        got = sol.maximumSwap(num)
        if want != got:
            print(f'Failed => args: {num}; want: {want}, but got: {got}')
            break
    else:
        print('All Passed')
