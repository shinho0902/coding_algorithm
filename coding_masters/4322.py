# 4322
import sys
sys.stdin = open("input.txt", "r")

n = int(input())

student = []
for i in range(n):
    name, score = map(str,input().split())
    student.append((name, int(score)))

student = sorted(student, key=lambda x: x[1], reverse=True)

for x in student:
    print(x[0], end=' ')