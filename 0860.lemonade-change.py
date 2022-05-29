#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#
# https://leetcode.com/problems/lemonade-change/description/
#
# algorithms
# Easy (51.95%)
# Likes:    945
# Dislikes: 107
# Total Accepted:    78.9K
# Total Submissions: 151.6K
# Testcase Example:  '[5,5,5,10,20]'
#
# At a lemonade stand, each lemonade costs $5. Customers are standing in a
# queue to buy from you, and order one at a time (in the order specified by
# bills). Each customer will only buy one lemonade and pay with either a $5,
# $10, or $20 bill. You must provide the correct change to each customer so
# that the net transaction is that the customer pays $5.
#
# Note that you don't have any change in hand at first.
#
# Given an integer array bills where bills[i] is the bill the i^th customer
# pays, return true if you can provide every customer with correct change, or
# false otherwise.
#
#
# Example 1:
#
#
# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation:
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.
#
#
# Example 2:
#
#
# Input: bills = [5,5,10,10,20]
# Output: false
# Explanation:
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5
# bill.
# For the last customer, we can not give change of $15 back because we only
# have two $10 bills.
# Since not every customer received correct change, the answer is false.
#
#
# Example 3:
#
#
# Input: bills = [5,5,10]
# Output: true
#
#
# Example 4:
#
#
# Input: bills = [10,10]
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= bills.length <= 10^5
# bills[i] is either 5, 10, or 20.
#
#
#
from typing import List

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dollar5 = dollar10 = 0
        for bill in bills:
            if bill == 5:
                dollar5 += 1
            elif bill == 10:
                if dollar5 == 0:
                    return False
                dollar5 -= 1
                dollar10 += 1
            else:
                if dollar10 > 0 and dollar5 > 0:
                    dollar5 -= 1
                    dollar10 -= 1
                elif dollar5 >= 3:
                    dollar5 -= 3
                else:
                    return False
        return True


# @lc code=end
def main():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        fn = getattr(sol, method)
        cases = [
            ([[5, 5, 10]], True),
            ([[5, 5, 5, 10, 20]], True),
            ([[5, 5, 10, 10, 20]], False),
            ([[10, 10]], False),
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
    main()
