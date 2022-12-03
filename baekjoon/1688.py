import sys
sys.stdin = open("input1.txt", "r")

# 1688: 트로피 진열


def func(arr):
    max, cnt = 0, 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            cnt += 1
    return cnt

n = int(input())
arr = []
for i in range(n):
    data = int(input())
    arr.append(data)

print(func(arr))

arr.reverse()

print(func(arr))