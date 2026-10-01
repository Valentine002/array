#  Approach 1: Brute Force
def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                print(f"Brute Force: {i} {j}")
                return

#  Approach 2: Sorting + Two Pointers 
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
            print(f"Sorting + Two Pointers: {i} {j}")
            return
        elif current_sum < target:
            left += 1
        else:
            right -= 1

#  Approach 3: Hash Map (Best)
def two_sum_hashmap(nums, target):
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        required = target - x
        if required in seen:
            print(f"Hash Map: {seen[required]} {i}")
            return
        seen[x] = i

if __name__ == "__main__":
  
    nums = [3, 2, 4, 6, 8]
    target = 6

    print("Expected Output: 1 2\n")
    
    two_sum_brute(nums, target)
    two_sum_sorting(nums, target)
    two_sum_hashmap(nums, target)

    #outputExpected Output: 1 2

#Brute Force: 1 2
#Sorting + Two Pointers: 1 2
#Hash Map: 1 2