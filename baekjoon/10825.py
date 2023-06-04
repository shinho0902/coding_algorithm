import sys
sys.stdin = open("input1.txt", "r")


n = int(input())
# print(n)

arr = []
for i in range(n):
    arr.append(input().split())


arr = sorted(arr, key=lambda arr : (-int(arr[1]),int(arr[2]),-int(arr[3]),arr[0]))

for i in range(n):
    print(arr[i][0])
