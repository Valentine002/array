def max_subarray_prefix(nums):
    max_sum = float('-inf')
    current_prefix = 0
    min_prefix = 0
    
    for x in nums:
        current_prefix += x
        # Max subarray ending here is current_prefix - minimum prefix seen before
        max_sum = max(max_sum, current_prefix - min_prefix)
        # Update minimum prefix for future elements
        min_prefix = min(min_prefix, current_prefix)
        
    return max_sum