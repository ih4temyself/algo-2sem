"""
10.03.24
@author: дьяконенко денис

   "           ""#                                       ""#
 mmm             #     mmm   m   m   mmm           mmm     #     mmmm   mmm
   #             #    #" "#  "m m"  #"  #         "   #    #    #" "#  #" "#
   #             #    #   #   #m#   # " "         m" "#    #    #   #  #   #
 mm#mm           "mm  "#m#"    #    "#mm"         "mm"#    "mm  "#m"#  "#m#"
                                                                 m  #
"""


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
    # для тестів на еолімпі - проходить всі
    # n, matrix = read_matrix()
    # print(undirected_checker(n, matrix))
    n = 3
    matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    print(undirected_checker(n, matrix))
