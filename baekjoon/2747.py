import sys
sys.stdin = open("input1.txt", "r")

# 2747: 피보나치수
import sys
input = sys.stdin.readline
n = int(input())

# # 재귀 불가능
# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)

# print(fibo(n))

a, b = 0, 1
while n > 0:
    a, b = b, a + b
    n -= 1
print(a)

"""
0 1 1 2 3
a b
  a b
    a b
      a  b
"""