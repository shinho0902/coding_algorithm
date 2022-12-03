import sys
sys.stdin = open("input1.txt", "r")



m, n, k = map(int,input().split())
graph = [[0] * m for _ in range(n)]

for _ in range(k):
    x, y = map(int,input().split())
    graph[y][x] = 1     # y가 행이니까 (위아래)

# 확인용    
for a in graph:
    print(a)

