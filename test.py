a = [[1, 2, 3], [3, 4, 7], [5, 3, 2]]
b = [[5, 6, 7], [7, 8, 3], [5, 8, 7]]


def matrix_sum(m1, m2):
    m3 = list()
    for i in range(len(m1)):
        m3.append(list())
        for j in range(len(m1[0])):
            m3[i].append(m1[i][j] + m2[i][j])

    return m3


print(matrix_sum(a, b))
