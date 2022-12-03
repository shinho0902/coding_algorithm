import sys
sys.stdin = open("input1.txt", "r")


import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    visited[x][y] = True
    directions = [(0,1), (0,-1), (-1,0), (1,0)]
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if array[nx][ny]==1 and visited[nx][ny]==False:
            dfs(nx, ny)


T = int(input())
for t in range(T):
    m, n, k = map(int,input().split())
    array = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int,input().split())
        array[y][x] = 1


    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j]==1 and visited[i][j]==False:
                dfs(i, j)
                result += 1
    print(result)