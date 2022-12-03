import sys
sys.stdin = open("input1.txt", "r")


import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x, y = map(int,input().split())
    arr.append((x,y))

arr = sorted(arr)

for a in arr:
    print(a[0], a[1])