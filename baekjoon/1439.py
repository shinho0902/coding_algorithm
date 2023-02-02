import sys
sys.stdin = open("input3.txt", "r")

nums = list(input())
# print(nums)
cnt = 0
for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        cnt += 1
print((cnt+1)//2)