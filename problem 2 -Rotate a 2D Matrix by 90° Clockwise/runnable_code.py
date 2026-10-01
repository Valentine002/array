import sys

#  Approach 2: Transpose + Reverse 
def rotate_transpose_reverse(matrix):
    n = len(matrix)
    
    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Input Parsing & Main 
def main():
   
    input_data = """3
1 2 3
4 5 6
7 8 9"""
    
    data = list(map(int, input_data.split()))
    
    if not data:
        return
        
    n = data[0]
    nums = data[1:]
    
    # Reconstruct the 2D matrix from the flat list
    matrix = []
    idx = 0
    for i in range(n):
        row = nums[idx : idx + n]
        matrix.append(row)
        idx += n
        
    # Rotate the matrix
    rotate_transpose_reverse(matrix)
    
    # Print the rotated matrix
    for row in matrix:
        print(*row)

if __name__ == "__main__":
    main()

#output
#7 4 1
#8 5 2
#9 6 3
    