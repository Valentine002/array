def max_subarray_kadane(nums):
    if not nums:
        return 0
        
    max_sum = nums[0]
    current_sum = nums[0]
    
    for x in nums[1:]:
        # Either extend the current subarray or start a new one at x
        current_sum = max(x, current_sum + x)
        # Update the overall maximum
        max_sum = max(max_sum, current_sum)
        
    return max_sum