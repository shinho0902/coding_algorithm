import sys
sys.stdin = open("input2.txt", "r")

max_val = 0
for i in range(5):
    tot = sum(list(map(int,input().split())))
    if max_val < tot:
        max_val = tot
        max_i = i + 1

print(max_i, max_val)


