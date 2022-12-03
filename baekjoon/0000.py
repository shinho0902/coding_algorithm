import sys
sys.stdin = open("input1.txt", "r")



n, m, k = map(int,input().split())
graph = [[0]*m for _ in range(n)]

for j in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1

# 확인용    
for a in graph:
    print(a)




