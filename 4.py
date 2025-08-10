def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]  # Create empty transposed matrix
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    
    return result

# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transposed = transpose(matrix)
for row in transposed:
    print(row)
