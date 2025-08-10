def is_sparse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_elements = rows * cols
    zero_count = 0

    for row in matrix:
        for val in row:
            if val == 0:
                zero_count += 1

    return zero_count > total_elements / 2

# Example
matrix1 = [
    [0, 0, 3],
    [0, 0, 0],
    [4, 0, 0]
]
print(is_sparse(matrix1))  # True

matrix2 = [
    [1, 2],
    [3, 4]
]
print(is_sparse(matrix2))  # False
