import sys
input = sys.stdin.readline

t = int(input())

nums = []

for i in range(t): 
    nums.append(int(input()))

memory = []

for i in range(max(nums)+1):
    if i == 0: 
        memory.append([1, 0])
    elif i == 1: 
        memory.append([0, 1])
    else: 
        memory.append([memory[i-1][0]+memory[i-2][0], memory[i-1][1]+memory[i-2][1]])

for i in nums: 
    print(" ".join(list(map(lambda x: str(x), memory[i]))))
