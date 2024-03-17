def zeros(n: int) -> int:
    if n == 1:
        return 2

    F = [0] * (n + 1)
    G = [0] * (n + 1)

    F[1], G[1] = 1, 0

    for i in range(2, n + 1):
        F[i] = F[i - 1] + G[i - 1]
        G[i] = F[i - 1]

    return F[n] + G[n]


if __name__ == "__main__":
    print(zeros(5))
