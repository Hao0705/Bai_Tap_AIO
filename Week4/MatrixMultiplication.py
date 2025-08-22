import numpy as np

def compute_matrix_multiplication(matrixA, matrixB):
    colA = len(matrixA[0])
    rowA = len(matrixA)

    colB = len(matrixB[0])
    rowB = len(matrixB)

    result_matrix = [[0 for _ in range(colB)] for _ in range(rowA)]

    if colA != rowB:
        print("Cannot perform multiplication on these two matrices.")
        return None
    else:
        for row in range(rowA):
            for col in range(colB):
                for k in range(colA):
                    result_matrix[row][col] += matrixA[row][k] * matrixB[k][col]

        return result_matrix

def compute_use_numpy(matrixA, matrixB):
    return np.dot(matrixA, matrixB)

matrixA = [[1, 2], [3, 4], [5, 6]]
matrixB = [[1, 2, 3, 4], [5, 6, 7, 8]]

result = compute_matrix_multiplication(matrixA, matrixB)

matrixC = np.array(matrixA)
matrixD = np.array(matrixB)
result_numpy = compute_use_numpy(matrixC, matrixD)

print(result)
print(result_numpy)

