import sys
sys.stdin = open("input1.txt", "r")


N = int(input())
A = list(map(int,input().split()))
M = int(input())
data = list(map(int,input().split()))

A = set(A)
for num in data:
    if num in A:
        print(1)
    else:
        print(0)