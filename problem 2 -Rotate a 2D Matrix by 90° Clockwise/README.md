Problem Restatement
Given an N x N matrix, rotate it 90 degrees clockwise.
Example:

1 2 3       7 4 1
4 5 6  -->  8 5 2
7 8 9       9 6 3

Approach 1: Using an Extra Matrix (Brute Force)
I created a new N x N matrix. The element at (i, j) moves to (j, N-1-i) in the rotated matrix.
Time Complexity: O(N^2)
Space Complexity: O(N^2) 

Approach 2: Transpose + Reverse 
This is the most elegant and commonly used in place solution.
Transpose the matrix (swap rows with columns): matrix[i][j] swaps with matrix[j][i].
Reverse each row.Time Complexity: O(N^2)Space Complexity: O(1)

Approach 3: Layer-by-Layer / 4-Way Swapping
 Rotate the outer boundary layer, then move inward. For each layer, we perform a 4-way swap.
 Time Complexity: O(N^2)
Space Complexity: O(1) (Uses only a few temporary variables)


I have the runnable_code.py that include the code for all approaches because the compiler in have doesnt have the input box so the code in that file is hardcoded on the input into the main() function.
