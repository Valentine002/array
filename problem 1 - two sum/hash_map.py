import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    
    n = data[0]
    nums = data[1:1 + n]
    target = data[1 + n]
    
    seen = {}  # value -> index
    
    for i, x in enumerate(nums):
        need = target - x
        
        if need in seen:
            print(seen[need], i)
            return
        
        seen[x] = i

if __name__ == "__main__":
    main()