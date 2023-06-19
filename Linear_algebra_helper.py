import numpy as np

# Matrix multiplication or dot product
matrix_a = np.array([[9, 2], [8, 4]])
matrix_b = np.array([[5, 9], [7, 4]])
dot_product = np.dot(matrix_a, matrix_b)
print("Matrix Multiplication (Dot Product):\n", dot_product)
print()

# Inverse of a square matrix
matrix_c = np.array([[2, 2], [1, 4]])
inverse_matrix = np.linalg.inv(matrix_c)
print("Inverse of Matrix C:\n", inverse_matrix)
print()

# Determinant of a square matrix
matrix_d = np.array([[4, 2], [0, 4]])
determinant = np.linalg.det(matrix_d)
print("Determinant of Matrix D:", determinant)
print()

# Eigenvalues and eigenvectors of a square matrix
matrix_e = np.array([[8, 2], [3, 7]])
eigenvalues, eigenvectors = np.linalg.eig(matrix_e)
print("Eigenvalues of Matrix E:", eigenvalues)
print("Eigenvectors of Matrix E:\n", eigenvectors)
print()

# Solving a system of linear equations
matrix_f = np.array([[8, -1, 1], [1, 2, -1], [8, 3, -2]])
vector = np.array([4, 9, 6])
solution = np.linalg.solve(matrix_f, vector)
print("Solution of the System of Equations:", solution)
