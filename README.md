# Notes

## 1. Dynamic Programming

### 1.1 Edit distance

Problems:

* [10. Regular expression matching](0010.regular-expression-matching.py)
* [44. Wildcard matching](0044.wildcard-matching.py)
* [62. Unique paths](0062.unique-paths.py)
* [63. Unique paths II](0063.unique-paths-ii.py)
* [72. Edit distance](0072.edit-distance.py)
* [97. Interleaving string](0097.interleaving-string.py)
* [115. Distinct subsequences](0115.distinct-subsequences.py)
* [583. Delete operation for two strings](0583.delete-operation-for-two-strings.py)
* [712. Minimum ascii delete sum for two strings](0712.minimum-ascii-delete-sum-for-two-strings.py)
* [718. Maximum length of repeated subarray](0718.maximum-length-of-repeated-subarray.py)
* [1143. Longest common subsequence](1143.longest-common-subsequence.py)
* [1035. Uncrossed lines](1035.uncrossed-lines.py)
* [1092. Shortest common supersequence](1092.shortest-common-supersequence.py)

### 1.1.1 General solution

```python
dp = [[0] * (n+1) for _ in range(m+1)]
dp[0][0] = INIT
for i in range(1, m+1):
    dp[i][0] = f1(dp[i-1][0])
for j in range(1, n+1):
    dp[0][j] = f2(dp[0][j-1])

for i in range(1, m+1):
    for j in range(1, n+1):
        if arr1[i-1] == arr2[j-1]:
            dp[i][j] = f(dp[i-1][j-1])
        else:
            dp[i][j] = g(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
return dp[m][n]
```

`Time complexity: O(M*N)`

`Space complexity: O(M*N)`

### 1.1.2 Optimize memory usage

```python
dp = [0] * (n+1)
dp[0] = INIT
for j in range(1, n+1):
    dp[j] = f2(dp[j-1])

for i in range(1, m+1):
    next_dp = [0] * (n+1)
    next_dp[0] = f1(dp[0])
    for j in range(1, n+1):
        if arr1[i-1] == arr2[j-1]:
            next_dp[j] = f(dp[j-1])
        else:
            next_dp[j] = g(next_dp[j-1], dp[j], dp[j-1])
    dp = next_dp
return dp[n]
```

`Time complexity: O(M*N)`

`Space complexity: O(N) or O(min(M, N))`

### 1.2 Split/Partition array for max/min value

Split an array with length `N` into `K` partitions.

For each partion `p`, there is a value: `f(p)`,

Find the `max/min` value of `g(p1, p2, p3...pk)`.

(`f` and `g` can be `max`, `min`, `sum`, `avg`...)

Problems:

* [410. Split array largest sum](0410.split-array-largest-sum.py)
* [813. Largest sum of average](0813.largest-sum-of-averages.py)
* [1278. Palindrome partition III](1278.palindrome-partitioning-iii.py)
* [1335. Minimum difficulty of a job schedule](1335.minimum-difficulty-of-a-job-schedule.py)

### 1.2.3 General solution

```python
from functools import cache

# left -> right
def solution(arr: List[int], K: int) -> int:
    N = len(arr)

    @cache
    def helper(start: int, k: int) -> int:
        if k == 1:
            return f(arr[start:])

        res = 0  # 1, -1, inf, -inf...
        for i in range(start, n-k+1):
            curr = f(arr[start:i+1])
            rest = helper(i+1, k-1)
            res = extremum(res, g(curr, rest))
        return res

    return helper(0, K)

# right -> left
def solution(arr: List[int], K: int) -> int:
    N = len(arr)

    @cache
    def helper(end: int, k: int) -> int:
        if k == 1:
            return f(arr[:end])

        res = 0  # 1, -1, inf, -inf...
        for i in range(end, k-1, -1):
            curr = f(arr[i-1:end])
            rest = helper(i-1, k-1)
            res = extremum(res, g(curr, rest))
        return res

    return helper(n, K)

# dp
def solution(arr: List[int], K: int) -> int:
    N = len(arr)
    dp = [[INIT] * (K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        dp[i][1] = f(arr[:i])
        for k in range(2, min(i, K)+1):
            for j in range(i, k-1, -1):
                curr = f(arr[j-1:i])
                dp[i][k] = extremum(dp[i][k], g(curr, dp[j-1][k-1]))

    return dp[n][k]
```

`Time complexity: O(N*N*K)`

`Space complexity: O(N*K)`
