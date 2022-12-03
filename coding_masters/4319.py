import sys
sys.stdin = open("input.txt", "r")

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(len(arr)):
    for num in arr:
        if arr[i] == num:
            
