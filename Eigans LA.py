#Program by Mosses Ross
import numpy as np


matrix = np.array([[5, 2], [5, 1]])

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print(f"Eigenvalues of {matrix} is: ")
for eigenvalue in eigenvalues:
    print(eigenvalue)

print("\nEigenvectors:")
for eigenvector in eigenvectors:
    print(eigenvector)

coefficients = np.poly(matrix)
characteristic_equation = np.poly1d(coefficients)

print("\nCharacteristic Equation:")
print(characteristic_equation)
