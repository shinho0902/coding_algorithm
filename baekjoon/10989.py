import sys
sys.stdin = open("input1.txt", "r")

import sys
input = sys.stdin.readline

# # 계수정렬

n = int(input())
count = [0] * 10001

for i in range(n):
    data = int(input())
    count[data] += 1

for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)
