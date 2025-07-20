def solve():
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    x = int(data[1])
    friends = []
    index = 2
    for _ in range(n):
        lose = int(data[index])
        win = int(data[index + 1])
        use = int(data[index + 2])
        friends.append((lose, win, use))
        index += 3

    if n == 0:
        print(0)
        return

    dp = [0] * (x + 1)
    for lose, win, use in friends:
        for j in range(x, -1, -1):
            if j >= use:
                dp[j] = max(dp[j] + lose, dp[j - use] + win)
            else:
                dp[j] += lose

    print(5 * dp[x])


def main():
    solve()


if __name__ == "__main__":
    main()
