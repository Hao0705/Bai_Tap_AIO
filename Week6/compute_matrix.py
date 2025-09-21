import numpy as np
from altair import vegalite_compilers


# ham tinh do dai vector
def compute_vector_length(vector):

    length = np.linalg.norm(vector)
    return length

# ham tinh tich vo huong cua hai vector
def compute_dot(vector1, vector2):
    return vector1 @ vector2

# ham nhan hai ma tran su dung dot cua numpy
def compute_multiplying(A, B):
    result = np.dot(A, B)
    return result

# tinh ma tran nghich dao
def inverse_matrix(A):
    return np.linalg.inv(A)

# ham tinh eigenvector va eigenvalue cua ma tran vuong
def compute_eigvector_eigvalue(A):
    eigenvalue, eigen_vector = np.linalg.eig(A)
    return eigenvalue, eigen_vector

# ham tinh gia tri cosine Similarity giua hai vector
def compute_cosine(A, B):
    result = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))
    return result

vector1 = np.array([10, 20, 30, 40])
vector2 = np.array([1, 1, 1, 1])

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

C = np.array([
    [1, 2],
    [3, 4]
])

print(compute_vector_length(vector1))
print(compute_dot(vector1, vector2))
print(compute_multiplying(A, B))
print(inverse_matrix(C))

eig_value, eig_vector = compute_eigvector_eigvalue(C)
print(compute_cosine(A, B))
