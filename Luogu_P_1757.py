from typing import List
from functools import lru_cache


# test for font
def solve():
    m, n = map(int, input().split())
    Q = [[0] for _ in range(101)]  # Group numbers up to 100

    groups = 0

    for _ in range(n):
        a, b, c = map(int, input().split())
        Q[c] += [a, b]
        groups = max(groups, c)

    if m == 0 or n == 0 or groups == 0:
        print(0)
        return

    @lru_cache(maxsize=None)
    def dfs(i, remaining):
        if remaining <= 0 or i < 1:
            return 0

        L = (len(Q[i]) - 1) // 2
        max_value = dfs(i - 1, remaining)  # Option to skip the current group

        for j in range(1, L + 1):
            weight = Q[i][2 * j - 1]
            value = Q[i][2 * j]
            if weight <= remaining:
                current_value = dfs(i - 1, remaining - weight) + value
                if current_value > max_value:
                    max_value = current_value

        return max_value

    print(dfs(groups, m))


def main():
    solve()


if __name__ == "__main__":
    main()
