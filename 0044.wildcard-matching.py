import itertools


class Solution:
    # O(m*n), O(m*n) => O(n)
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == "*"

        for i, j in itertools.product(range(1, m + 1), range(1, n + 1)):
            dp[i][j] = (dp[i][j - 1] or dp[i - 1][j]
                        if p[j - 1] == "*" else dp[i - 1][j - 1] and
                        (s[i - 1] == p[j - 1] or p[j - 1] == "?"))
        return dp[m][n]

    # O(m*n), O(n)
    def isMatch1(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and p[j - 1] == "*"

        for i in range(1, m + 1):
            next_dp = [False] * (n + 1)
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    next_dp[j] = next_dp[j - 1] or dp[j]
                else:
                    next_dp[j] = dp[j - 1] and (s[i - 1] == p[j - 1]
                                                or p[j - 1] == "?")
            dp = next_dp
        return dp[n]


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            (["aa", "a"], False),
            (["aa", "*"], True),
            (["cb", "?a"], False),
            (["adceb", "*a*b"], True),
            (["acdcb", "a*c?b"], False),
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
