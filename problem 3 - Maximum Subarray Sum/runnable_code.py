import sys

#  Kadane's Algorithm 
def max_subarray_kadane(nums):
    if not nums:
        return 0
        
    max_sum = nums[0]
    current_sum = nums[0]
    
    for x in nums[1:]:
        current_sum = max(x, current_sum + x)
        max_sum = max(max_sum, current_sum)
        
    return max_sum

#  Main Execution 
if __name__ == "__main__":
   
    n = 9
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    
    result = max_subarray_kadane(nums)
    
    print("Array:", nums)
    print("Maximum Subarray Sum:", result)

    #output
        #Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        #Maximum Subarray Sum: 6