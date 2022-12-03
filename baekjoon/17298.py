import sys
sys.stdin = open("input2.txt", "r")

import sys
input = sys.stdin.readline


n = int(input())
ans = [-1] * n
A = list(map(int, input().split()))
stack = [] # [ [val, idx], [val, idx] ... ]

for i in range(n):
    while stack and (stack[-1][0] < A[i]):
        val, idx = stack.pop()
        ans[idx] = A[i]
    stack.append([A[i], i])


print(*ans)