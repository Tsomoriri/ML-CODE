"""
Task 1.2: NumPy Core Mastery: Implement vector/matrix operations, broadcasting, linear algebra, etc., using only Python lists first, then master NumPy equivalents (np.array, np.dot, slicing, np.linalg, etc.) from memory.

    Goal: Internalize NumPy's array logic and syntax. Memorize core functions/attributes.
"""
"""
Okay, let's structure Task 1.2. The goal is to first understand the operations using fundamental Python lists and loops, and then master the efficient and concise NumPy equivalents.

Here are 13 questions designed for this purpose. For each question, first try to implement the solution using only standard Python lists, loops, and built-in functions. Then, implement the same task using NumPy arrays and functions, aiming to do it from memory.

Task 1.2: NumPy Core Mastery Questions

Part 1: Vector Operations

    Vector Creation and Addition:
        Python Lists: Create two lists representing vectors, v1 = [1, 2, 3] and v2 = [4, 5, 6]. Write a Python function add_vectors_py(vec1, vec2) that takes two lists (assume they have the same length) and returns a new list containing the element-wise sum.
        NumPy: Create v1 and v2 as NumPy arrays. Perform the vector addition using NumPy's element-wise addition.

    Vector Dot Product:
        Python Lists: Using the lists v1 and v2 from Q1, write a function dot_product_py(vec1, vec2) that calculates their dot product (sum of element-wise products).
        NumPy: Calculate the dot product of the NumPy arrays v1 and v2 using np.dot() or the @ operator.

    Vector Scalar Multiplication:
        Python Lists: Given v1 = [1, 2, 3] and a scalar s = 5. Write a function scalar_multiply_py(vec, scalar) that returns a new list where each element is multiplied by the scalar.
        NumPy: Perform the scalar multiplication on the NumPy array v1 using the * operator.

Part 2: Matrix Operations

    Matrix Creation and Addition:
        Python Lists: Represent matrices as lists of lists: M1 = [[1, 2, 3], [4, 5, 6]] and M2 = [[7, 8, 9], [10, 11, 12]]. Write a function add_matrices_py(mat1, mat2) for element-wise addition (assume compatible dimensions).
        NumPy: Create M1 and M2 as NumPy arrays. Perform matrix addition using NumPy.

    Matrix Multiplication (Dot Product):
        Python Lists: Represent matrices A = [[1, 2], [3, 4]] and B = [[5, 6], [7, 8]]. Write a function multiply_matrices_py(mat1, mat2) to compute their matrix product using nested loops (ensure you understand the row-column multiplication rule).
        NumPy: Create A and B as NumPy arrays. Compute their matrix product using np.matmul() or the @ operator.

    Element-wise Matrix Multiplication (Hadamard Product):
        Python Lists: Using M1 and M2 from Q4, write a function elementwise_multiply_py(mat1, mat2) that computes the element-wise product (Hadamard product).
        NumPy: Compute the element-wise product of the NumPy arrays M1 and M2 using the * operator.

Part 3: Broadcasting

    Broadcasting: Matrix and Vector:
        Python Lists: Given M1 = [[1, 2, 3], [4, 5, 6]] and v = [10, 20, 30]. Write a function broadcast_add_row_py(matrix, vector) that adds the vector v to each row of the matrix M1 using loops.
        NumPy: Create M1 and v as NumPy arrays. Add v to M1 using NumPy's + operator, relying on broadcasting rules.

    Broadcasting: Matrix and Scalar:
        Python Lists: Given M1 = [[1, 2, 3], [4, 5, 6]] and scalar s = 100. Write a function scalar_add_matrix_py(matrix, scalar) that adds the scalar to every element of the matrix using nested loops.
        NumPy: Add scalar s to the NumPy array M1 using the + operator. Observe broadcasting in action.

Part 4: Slicing and Indexing

    Matrix Slicing:
        Python Lists: Given Matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]].
            Extract the second row: [5, 6, 7, 8].
            Extract the third column: [3, 7, 11].
            Extract the sub-matrix [[6, 7], [10, 11]].
        NumPy: Create Matrix as a NumPy array. Perform the same extractions using NumPy's slicing syntax (e.g., arr[row_slice, col_slice]).

    Boolean Indexing:
        Python Lists: Given v = [10, -5, 20, -15, 30, -25]. Create a new list containing only the positive elements from v using a list comprehension with a condition.
        NumPy: Create v as a NumPy array. Use boolean indexing (e.g., arr[arr > 0]) to select only the positive elements.

Part 5: Linear Algebra & Statistics

    Matrix Transposition:
        Python Lists: Given M1 = [[1, 2, 3], [4, 5, 6]]. Write a function transpose_py(matrix) to compute its transpose (swap rows and columns).
        NumPy: Compute the transpose of the NumPy array M1 using the .T attribute or np.transpose().

    Linear Algebra: Inverse and Determinant:
        Python Lists: (Conceptual) Explain why calculating the inverse or determinant for a general matrix using only standard lists and loops is complex. (No implementation needed). For a 2x2 matrix A = [[a, b], [c, d]], how would you calculate the determinant ad - bc?
        NumPy: Create the matrix A = np.array([[1, 2], [3, 4]]). Calculate its determinant using np.linalg.det(). Calculate its inverse using np.linalg.inv(). Verify that A @ inv(A) is close to the identity matrix (np.eye(2)).

    Solving Linear Equations & Basic Stats:
        Python Lists: (Conceptual) How would you approach solving the system Ax = b where A = [[1, 2], [3, 4]] and b = [5, 6] using standard Python (e.g., substitution/elimination)? Calculate the sum and average of data = [1, 5, 2, 8, 3, 9, 4] using sum() and len().
        NumPy: Define A and b as NumPy arrays. Solve for x using np.linalg.solve(A, b). Create data as a NumPy array. Calculate its sum, mean, min, and max using np.sum(), np.mean(), np.min(), np.max().
"""
