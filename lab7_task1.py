def sort(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    snapshots = []
    for k in range(rows):
        for step in range(cols * cols):
            j = step % (cols - 1)
            if matrix[k][j] < matrix[k][j + 1]:
                matrix[k][j], matrix[k][j + 1] = matrix[k][j + 1], matrix[k][j]
                snapshots.append(list(matrix[k]))
    return snapshots

def calculation(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    product = 1
    for j in range(cols):
        col_sum = 0
        has_elements = False
        limit = min(rows, j)
        for i in range(limit):
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

memory_hog = sort(matrix)

for row in matrix:
    print(f"{row}")

res = calculation(matrix)
print(res)