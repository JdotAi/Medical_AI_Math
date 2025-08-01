def matrix_multiply(A, B):
    """
    Implement matrix multiplication without NumPy
    Must handle medical data matrices (1000x100 typical size)
    Include error checking for dimension compatibility
    """
    if len(A[0])!= len(B):
        print("The matrix size is not right, check metrix size")

    result = [ [0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k]* B[k][j]
    return result


    
def eigenvalue_decomposition(matrix):
    """
    Implement eigenvalue/eigenvector computation
    Use for finding patterns in medical correlation matrices
    Must converge within 1000 iterations
    """
    pass
def singular_value_decomposition(matrix):
    """
    Implement SVD for medical data compression
    Essential for processing large medical datasets
    Return U, S, V matrices
    """
    pass
def medical_feature_extraction(patient_data_matrix):
    """
    Use eigenvalues to identify most important medical features
    Return ranked list of medical features by importance
    """
    pass