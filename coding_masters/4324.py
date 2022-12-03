# 4324
import sys
sys.stdin = open("input.txt", "r")


n = int(input())
cnt = 1

a, b = map(int,input().split())
min = a * b

for i in range(n-1):
    a, b = map(int,input().split())
    if min > abs(a * b):
        min = abs(a * b)
        cnt += 1

print(cnt)


