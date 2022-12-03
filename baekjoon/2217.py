import sys
sys.stdin = open("input1.txt", "r")

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
res = []
for i in range(len(rope)):
    a = rope[i] * (i+1)
    res.append(a)

print(max(res))
