import sys
sys.stdin = open("input1.txt", "r")

n = int(input())
info = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    info.append((age, name))
# print(info)
info = sorted(info, key=lambda x:x[0])
# print(info)
for x in info:
    print(x[0], x[1])