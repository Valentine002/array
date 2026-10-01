def rotate_transpose_reverse(matrix):
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n): # j starts at i+1 to avoid double swapping
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()