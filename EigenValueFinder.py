import numpy as np
from sympy import symbols, Matrix, Eq, solve

def input_matrix():
    try:
        dimensions = int(input("Enter the dimension (ex: for a 6x6 matrix, enter 6): "))
        matrix = []
        print(f"Enter a {dimensions}x{dimensions} matrix:")
        for i in range(dimensions):
            row = input(f"Row {i + 1} (space-separated values): ").split()
            if len(row) != dimensions:
                print(f"Please enter {dimensions} values for each row.")
                return None
            matrix.append([float(val) for val in row])
        return np.array(matrix, dtype=np.float64)  # Convert to float64 (To prevent error)
    except ValueError:
        print("Invalid input for dimension.")
        return None

def calculate_eigenvalues(matrix):
    if matrix is not None:
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        return eigenvalues, eigenvectors

def main():
    matrix = input_matrix()
    if matrix is not None:
        eigenvalues, eigenvectors = calculate_eigenvalues(matrix)
        if eigenvalues is not None:
            print("Eigenvalues:")
            for eigenvalue in eigenvalues:
                print(eigenvalue)
            print("\nEigenvectors:")
            print(eigenvectors)

            # Characteristic equation
            x = symbols('x')
            char_matrix = Matrix(matrix - x * Matrix.eye(matrix.shape[0]))
            char_eq = char_matrix.det()
            print("\nCharacteristic Equation:")
            print(char_eq)
            solutions = solve(char_eq, x)
            print("\nSolutions to Characteristic Equation:")
            print(solutions)

if __name__ == "__main__":
    main()
