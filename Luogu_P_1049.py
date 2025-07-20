from typing import List
from functools import lru_cache


def solve():
    # 处理单个测试用例的逻辑
    V = int(input())
    n = int(input())
    # v = list(map(int, input().split()))
    v = []
    for _ in range(n):
        v.append(int(input()))

    @lru_cache(maxsize=None)
    def dfs(i, R):
        if i == 0:
            return v[i] if v[i] <= R else 0
        if v[i] > R:
            return dfs(i - 1, R)
        else:
            return max(dfs(i - 1, R), dfs(i - 1, R - v[i]) + v[i])

    print(V - dfs(n - 1, V))


def main():
    # T = int(input())  # 测试用例数量
    # for _ in range(T):
    solve()


if __name__ == "__main__":
    main()
