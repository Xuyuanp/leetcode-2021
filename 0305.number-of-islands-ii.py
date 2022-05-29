# https://leetcode-cn.com/problems/number-of-islands-ii/
from typing import List, Tuple


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res = []

        ufs = {}
        cnt = 0

        def find(pos: Tuple[int]) -> Tuple[int]:
            nonlocal cnt
            if pos not in ufs:
                cnt += 1
                ufs[pos] = pos
            elif ufs[pos] != pos:
                ufs[pos] = find(ufs[pos])
            return ufs[pos]

        def union(p1: Tuple[int], p2: Tuple[int]):
            nonlocal cnt
            r1, r2 = find(p1), find(p2)
            if r1 == r2:
                return
            cnt -= 1
            ufs[r1] = r2

        for x, y in positions:
            find((x, y))
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) in ufs:
                    union((x, y), (nx, ny))
            res.append(cnt)

        return res


def test():
    sol = Solution()
    methods = [name for name in dir(sol) if not name.startswith("__")]
    for method in methods:
        print(f"Testing {method}:")
        func = getattr(sol, method)
        cases = [
            ([3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]], [1, 1, 2, 3]),
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
