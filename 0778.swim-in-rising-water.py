#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#
# https://leetcode.com/problems/swim-in-rising-water/description/
#
# algorithms
# Hard (57.62%)
# Likes:    1438
# Dislikes: 107
# Total Accepted:    55.7K
# Total Submissions: 96.2K
# Testcase Example:  '[[0,2],[1,3]]'
#
# You are given an n x n integer matrix grid where each value grid[i][j]
# represents the elevation at that point (i, j).
#
# The rain starts to fall. At time t, the depth of the water everywhere is t.
# You can swim from a square to another 4-directionally adjacent square if and
# only if the elevation of both squares individually are at most t. You can
# swim infinite distances in zero time. Of course, you must stay within the
# boundaries of the grid during your swim.
#
# Return the least time until you can reach the bottom right square (n - 1, n -
# 1) if you start at the top left square (0, 0).
#
#
# Example 1:
#
#
# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a
# higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
#
#
# Example 2:
#
#
# Input: grid =
# [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation: The final route is shown.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
#
#
#
# Constraints:
#
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] < n^2
# Each value grid[i][j] is unique.
#
#
#
from collections import deque
from typing import List


# @lc code=start
class Solution:
    # O(N*log(N)), O(N). N=n*n
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # union find
        def connected(time) -> bool:
            ufs = {}

            def find(index: int) -> int:
                if index != ufs.setdefault(index, index):
                    ufs[index] = find(ufs[index])
                return ufs[index]

            def union(x: int, y: int):
                rx, ry = find(x), find(y)
                if rx != ry:
                    ufs[rx] = ry

            for i in range(n):
                for j in range(n):
                    if grid[i][j] > time:
                        continue
                    if i > 0 and grid[i - 1][j] <= time:
                        union(i * n + j, (i - 1) * n + j)
                    if j > 0 and grid[i][j - 1] <= time:
                        union(i * n + j, i * n + j - 1)

            return find(0) == find(n**2 - 1)

        left, right = grid[0][0], n**2 - 1
        while left < right:
            mid = (left + right) // 2
            if not connected(mid):
                left = mid + 1
            else:
                right = mid

        return left

    # O(N*log(N)), O(N). N=n*n
    def swimInWater1(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # dfs
        def connected(time) -> bool:
            visited = set()

            def dfs(i: int, j: int) -> bool:
                if i == j == n - 1:
                    return True
                visited.add(grid[i][j])
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    x, y = i + dx, j + dy
                    if (0 <= x < n and 0 <= y < n and grid[x][y] not in visited
                            and grid[x][y] <= time) and dfs(x, y):
                        return True
                return False

            return dfs(0, 0)

        left, right = grid[0][0], n**2 - 1
        while left < right:
            mid = (left + right) // 2
            if not connected(mid):
                left = mid + 1
            else:
                right = mid

        return left

    # O(N*log(N)), O(N). N=n*n
    def swimInWater2(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # bfs
        def connected(time) -> bool:
            queue = deque([(0, 0)])
            visited = set()
            visited.add(grid[0][0])
            while queue:
                i, j = queue.popleft()
                if i == j == n - 1:
                    return True
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    x, y = i + dx, j + dy
                    if (0 <= x < n and 0 <= y < n and grid[x][y] not in visited
                            and grid[x][y] <= time):
                        visited.add(grid[x][y])
                        queue.append((x, y))

            return False

        left, right = grid[0][0], n**2 - 1
        while left < right:
            mid = (left + right) // 2
            if not connected(mid):
                left = mid + 1
            else:
                right = mid

        return left


# @lc code=end
def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([[[0, 2], [1, 3]]], 3),
            (
                [[
                    [0, 1, 2, 3, 4],
                    [24, 23, 22, 21, 5],
                    [12, 13, 14, 15, 16],
                    [11, 17, 18, 19, 20],
                    [10, 9, 8, 7, 6],
                ]],
                16,
            ),
            (
                [[
                    [
                        105,
                        209,
                        171,
                        91,
                        64,
                        394,
                        279,
                        11,
                        45,
                        84,
                        207,
                        321,
                        216,
                        197,
                        381,
                        377,
                        78,
                        19,
                        203,
                        198,
                    ],
                    [
                        141,
                        10,
                        335,
                        170,
                        265,
                        104,
                        338,
                        40,
                        397,
                        376,
                        346,
                        356,
                        212,
                        154,
                        280,
                        177,
                        247,
                        90,
                        87,
                        360,
                    ],
                    [
                        99,
                        59,
                        242,
                        149,
                        344,
                        172,
                        276,
                        230,
                        133,
                        193,
                        284,
                        345,
                        46,
                        363,
                        30,
                        142,
                        295,
                        70,
                        224,
                        200,
                    ],
                    [
                        251,
                        88,
                        379,
                        72,
                        319,
                        272,
                        243,
                        165,
                        180,
                        182,
                        387,
                        264,
                        23,
                        67,
                        137,
                        342,
                        125,
                        139,
                        144,
                        367,
                    ],
                    [
                        94,
                        211,
                        151,
                        37,
                        290,
                        112,
                        343,
                        157,
                        300,
                        271,
                        260,
                        373,
                        369,
                        294,
                        289,
                        57,
                        44,
                        12,
                        20,
                        340,
                    ],
                    [
                        220,
                        368,
                        186,
                        277,
                        181,
                        187,
                        273,
                        214,
                        315,
                        337,
                        328,
                        18,
                        231,
                        223,
                        331,
                        75,
                        275,
                        96,
                        135,
                        150,
                    ],
                    [
                        202,
                        74,
                        27,
                        184,
                        399,
                        341,
                        49,
                        62,
                        261,
                        86,
                        314,
                        383,
                        302,
                        257,
                        61,
                        148,
                        268,
                        120,
                        36,
                        25,
                    ],
                    [
                        15,
                        253,
                        285,
                        185,
                        226,
                        146,
                        126,
                        122,
                        83,
                        361,
                        110,
                        234,
                        183,
                        239,
                        52,
                        190,
                        152,
                        81,
                        136,
                        188,
                    ],
                    [
                        39,
                        199,
                        358,
                        26,
                        301,
                        116,
                        32,
                        386,
                        29,
                        138,
                        393,
                        159,
                        102,
                        140,
                        370,
                        227,
                        282,
                        111,
                        5,
                        33,
                    ],
                    [
                        189,
                        35,
                        132,
                        54,
                        210,
                        235,
                        28,
                        353,
                        281,
                        127,
                        318,
                        58,
                        100,
                        286,
                        384,
                        24,
                        307,
                        252,
                        80,
                        103,
                    ],
                    [
                        244,
                        176,
                        124,
                        79,
                        161,
                        355,
                        218,
                        398,
                        392,
                        380,
                        225,
                        121,
                        178,
                        352,
                        329,
                        322,
                        167,
                        51,
                        313,
                        85,
                    ],
                    [
                        107,
                        118,
                        351,
                        287,
                        324,
                        283,
                        48,
                        320,
                        82,
                        364,
                        357,
                        16,
                        219,
                        330,
                        89,
                        143,
                        241,
                        262,
                        71,
                        191,
                    ],
                    [
                        95,
                        97,
                        3,
                        7,
                        270,
                        249,
                        213,
                        339,
                        362,
                        298,
                        4,
                        258,
                        248,
                        390,
                        299,
                        306,
                        156,
                        164,
                        109,
                        229,
                    ],
                    [
                        221,
                        9,
                        228,
                        160,
                        274,
                        263,
                        374,
                        147,
                        98,
                        63,
                        13,
                        41,
                        326,
                        396,
                        349,
                        372,
                        385,
                        317,
                        325,
                        266,
                    ],
                    [
                        53,
                        131,
                        173,
                        312,
                        174,
                        114,
                        250,
                        119,
                        163,
                        22,
                        246,
                        92,
                        278,
                        365,
                        292,
                        215,
                        14,
                        304,
                        204,
                        73,
                    ],
                    [
                        233,
                        323,
                        366,
                        130,
                        378,
                        305,
                        311,
                        93,
                        134,
                        217,
                        297,
                        327,
                        232,
                        194,
                        240,
                        1,
                        208,
                        6,
                        310,
                        47,
                    ],
                    [
                        69,
                        101,
                        332,
                        195,
                        254,
                        236,
                        50,
                        166,
                        56,
                        168,
                        267,
                        17,
                        359,
                        347,
                        65,
                        316,
                        238,
                        296,
                        348,
                        222,
                    ],
                    [
                        76,
                        123,
                        129,
                        293,
                        391,
                        2,
                        245,
                        108,
                        303,
                        38,
                        66,
                        55,
                        43,
                        256,
                        162,
                        60,
                        179,
                        77,
                        336,
                        21,
                    ],
                    [
                        196,
                        388,
                        333,
                        395,
                        42,
                        382,
                        291,
                        237,
                        288,
                        375,
                        128,
                        145,
                        192,
                        158,
                        350,
                        259,
                        206,
                        34,
                        334,
                        255,
                    ],
                    [
                        201,
                        175,
                        153,
                        68,
                        205,
                        155,
                        115,
                        269,
                        389,
                        169,
                        371,
                        308,
                        117,
                        31,
                        354,
                        8,
                        113,
                        309,
                        106,
                        0,
                    ],
                ]],
                266,
            ),
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
