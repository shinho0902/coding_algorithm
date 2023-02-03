import sys
sys.stdin = open("input2.txt", "r")

"""
0001100

1
"""

# 앞뒤가 다른 갯수 + 1 (홀수인경우)  / 2 

s = list(input())

cnt = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1

print((cnt+1)//2)

