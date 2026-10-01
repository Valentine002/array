Approach 1: Brute Force (O(n²))
Check every possible contiguous subarray and calculate its sum. Keep track of the maximum sum found.
Time Complexity: O(n²) because we use two nested loops.
Space Complexity: O(1)

this approach is too slow for large arrays

Approach 2: Prefix Sum (O(n))
A subarray sum from index i to j is prefix[j] - prefix[i-1]. To maximize this, we want the smallest possible prefix[i-1] 
Time Complexity: O(n)
Space Complexity: O(1) (if we calculate prefix sum on the fly).

Approach 3: Kadane's Algorithm (O(n))

This is the most elegant solution. As we iterate through the array, we maintain a current_sum. For each element x, we have two choices:
1. Add x to the existing current_sum (extend the subarray).
2. Start a new subarray from x (discard the previous sum).
We choose whichever is larger: current_sum = max(x, current_sum + x)
We also keep track of the max_sum seen so far.
Time Complexity: O(n) (One pass).
Space Complexity: O(1)

How Kadane's Algorithm reduces O(n²) to O(n):
In the brute force approach, we recalculate the sum of overlapping subarrays repeatedly.
Kadane's algorithm recognizes that if your current running sum becomes negative, it is useless to carry it forward. A negative prefix will only drag down the sum of any future elements.
So, we reset the current_sum to 0 (or in our code, just start a new subarray at the current element x).
This allows us to solve the problem in a single pass.
