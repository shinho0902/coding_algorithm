import sys
sys.stdin = open("input1.txt", "r")


n = int(input())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)
nums.sort()

for num in nums:
    print(num)