def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        line = input()
        row = [int(num) for num in line.split()]
        matrix.append(row)
    return n, matrix


def undirected_checker(n, matrix):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return "NO"
            if i == j and matrix[i][j] != 0:
                return "NO"
    return "YES"


if __name__ == "__main__":
    n, matrix = read_matrix()
    print(undirected_checker(n, matrix))
