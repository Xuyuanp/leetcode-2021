# Notes

## 1. Dynamic Programming

Problems:

* [10. Regular expression matching](0010.regular-expression-matching.py)
* [44. Wildcard maching](0044.wildcard-matching.py)
* [62. Unique paths](0062.unique-paths.py)
* [63. Unique paths II](0063.unique-paths-ii.py)
* [72. Edit distance](0072.edit-distance.py)
* [97. Interleaving string](0097.interleaving-string.py)
* [115. Distinct subsequence](0115.distinct-subsequences.py)
* [583. Delete operation for two strings](0583.delete-operation-for-two-strings.py)
* [712. Minimum ascii delete sum for two strings](0712.minimum-ascii-delete-sum-for-two-strings.py)
* [718. Maximum length of repeated subarray](0718.maximum-length-of-repeated-subarray.py)
* [1143. Longest common subsequence](1143.longest-common-subsequence.py)
* [1035. Uncrossed lines](1035.uncrossed-lines.py)
* [1092. Shortest common supersequence](1092.shortest-common-supersequence.py)

### 1.1 General solution

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

_Time complexity: O(m*n)_

_Space complexity: O(m*n)_

### 1.2 Optimize memory usage

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

_Time complexity: O(m*n)_

_Space complexity: O(n) or O(min(m, n))_
