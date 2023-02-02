import sys
sys.stdin = open("input2.txt", "r")

"""
25 5

2
"""
"""
17 4

3
"""
n, k = map(int,input().split()) # n: 주어지는 수, k: 나눠지는 수

res = 0
while n != 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    res += 1

print(res)
