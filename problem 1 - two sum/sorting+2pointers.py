def two_sum_sorting(nums, target):
    pairs = [(value, index) for index, value in enumerate(nums)]
    pairs.sort()
    
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = pairs[left][0] + pairs[right][0]
        
        if current_sum == target:
            i = pairs[left][1]
            j = pairs[right][1]
            if i > j:
                i, j = j, i
            print(i, j)
            return
        
        elif current_sum < target:
            left += 1
        
        else:
            right -= 1