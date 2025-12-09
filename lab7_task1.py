def sort(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for k in range(rows):
        for i in range(cols - 1):
            for j in range(cols - 1 - i):
                if matrix[k][j] < matrix[k][j + 1]:
                    matrix[k][j], matrix[k][j + 1] = matrix[k][j + 1], matrix[k][j]


def calculation(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    product = 1
    for j in range(cols):
        col_sum = 0
        has_elements = False
        for i in range(rows):
            if i < j:
                col_sum += matrix[i][j]
                has_elements = True
        if has_elements:
            product *= col_sum
    return product


matrix = [
    [9, 67, -65, 45, 1],
    [12, 61, 48, -5, -1],
    [0, 39, 0, 41, 2],
    [36, 95, -8, -5, 0],
    [11, 22, 71, 3, 63],
]

sort(matrix)

for row in matrix:
    print(f"{row}")

res = calculation(matrix)
print(res)