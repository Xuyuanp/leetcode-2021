import itertools


class Solution:
    # O(m*n), O(m*n)
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 if i > 0 and j > 0 else i + j for j in range(n + 1)]
              for i in range(m + 1)]
        for i, j in itertools.product(range(1, m + 1), range(1, n + 1)):
            dp[i][j] = (dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else
                        min(dp[i - 1][j], dp[i][j - 1]) + 1)
        return dp[m][n]

    # O(m*n), O(min(m, n))
    def minDistance1(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        m, n = len(word1), len(word2)
        dp = [0] * (n + 1)
        for i in range(m + 1):
            next_dp = [0] * (n + 1)
            for j in range(n + 1):
                if i == 0 or j == 0:
                    next_dp[j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    next_dp[j] = dp[j - 1]
                else:
                    next_dp[j] = min(dp[j], next_dp[j - 1]) + 1
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
            (["a", "b"], 2),
            (["a", "a"], 0),
            (["a", "ab"], 1),
            (["ab", "a"], 1),
            (["aaa", "a"], 2),
            (["sea", "eat"], 2),
            (["leetcode", "etco"], 4),
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
