# 1026 그리디 (19분?)

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()

result = 0
for a in A:
    max_B = max(B)
    result += a*max_B

    max_B_idx = B.index(max_B)
    del B[max_B_idx]

print(result)
