import sys
sys.stdin = open("input1.txt", "r")

# 1568: 새

n = int(input())

cnt = 0

k = 1
while n > 0:
    if n < k:
        k = 1
        
    n -= k
    k += 1
    cnt += 1

print(cnt)