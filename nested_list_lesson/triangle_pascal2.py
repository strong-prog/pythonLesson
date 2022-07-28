"""
На вход программе подается натуральное число n.
Напишите программу, которая выводит первые n строк треугольника Паскаля.
"""


def pascal(num):

    pyramid = []
    for i in range(num):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = pyramid[i - 1][j - 1] + pyramid[i - 1][j]

        pyramid.append(row)

    for row in pyramid:
        for elem in row:
            print(elem, end=' ')
        print()


pascal(5)
