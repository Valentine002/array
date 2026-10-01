i have an array nums and target. I need 2 different indices i and j such that nums[i] + nums[j] == target, Return the indices separated by a space and only 1 valid answer exist.

Approach 1: Brute Force
Check every pair of different indices, For every i, check every j > i. this approach is slow for large arrays.

Complexity
Time: O(n^2)

Space: O(1)

Approach 2: Hash Map / Dictionary
this is the best approach, While scanning the array, for each number x, compute what number you need:
need = target - x
If need was already seen before, then its index and the current index form the answer.We store numbers and their indices in a dictionary.
We only store elements seen before the current index, so we never use the same element twice.
Complexity
Time: O(n)

Space: O(n)
 input: 
 5
3 2 4 6 8
6

process:
i = 0, x = 3, need = 3, seen = {}
i = 1, x = 2, need = 4, seen = {3:0}
i = 2, x = 4, need = 2, seen contains 2 at index 1

output: 1 2

Approach 3: Sorting + Two Pointers

Create pairs: (value, original_index).Sort by value.
Use two pointers:
left = 0
right = n - 1

If sum is too small, move left right.If sum is too large, move right left.If sum equals target, print the original indices.

Complexity
Time: O(n log n) because of sorting

Space: O(n) for the pairs


I have the runnable_code.py that includes the hardcorded input for it to run and show output, that file call the functions and provide the test data directly in the code
