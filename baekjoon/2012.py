import sys
sys.stdin = open("input1.txt", "r")

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)
arr2 = list(range(1,n+1))

# print(arr)
# print(arr2)
tot = 0
for i in range(n):
    tot += abs(arr2[i] - arr[i])

print(tot)