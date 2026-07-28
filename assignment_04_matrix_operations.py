# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, name="Matrix"):
    matrix = []
    print(f"\nEntering {name} ({rows}x{cols}):")
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}: ").split()
        row = [float(x) for x in row_input]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        formatted_row = []
        for val in row:
            if val.is_integer():
                formatted_row.append(f"{int(val):>4}")
            else:
                formatted_row.append(f"{val:>6.2f}")
        print(" ".join(formatted_row))


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
        
    return transposed


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
        
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            sum_val = 0
            for k in range(cols_a):
                sum_val += matrix_a[i][k] * matrix_b[k][j]
            row.append(sum_val)
        result.append(row)
        
    return result


if __name__ == "__main__":
    print("=== PART A: Transpose Matrix ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    mat_a = read_matrix(m, n, "Matrix")
    
    print("\nOriginal Matrix:")
    print_matrix(mat_a)
    print("\nTransposed Matrix:")
    print_matrix(transpose_matrix(mat_a))

    print("\n" + "=" * 40)
    print("=== PART B: Add Two Matrices ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    mat_1 = read_matrix(m, n, "Matrix 1")
    mat_2 = read_matrix(m, n, "Matrix 2")
    
    print("\nMatrix 1 + Matrix 2:")
    print_matrix(add_matrices(mat_1, mat_2))

    print("\n" + "=" * 40)
    print("=== PART C: Multiply Two Matrices ===")
    m = int(input("Enter rows for Matrix A: "))
    n = int(input("Enter columns for Matrix A (and rows for Matrix B): "))
    p = int(input("Enter columns for Matrix B: "))
    
    mat_a = read_matrix(m, n, "Matrix A")
    mat_b = read_matrix(n, p, "Matrix B")
    
    print("\nMatrix A x Matrix B:")
    print_matrix(multiply_matrices(mat_a, mat_b))