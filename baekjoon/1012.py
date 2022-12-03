import sys
sys.stdin = open("input1.txt", "r")


import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    visited[x][y] = True
    directions = [(0,1),(0,-1),(-1,0),(1,0)] # 상하좌우
    for dx, dy in directions:
        nx, ny = x+dx, y+dy # 이동
        if nx<0 or nx>=n or ny<0 or ny>=m: # 맵밖으로 벗어나면
            continue # 넘어감
        if array[nx][ny]==1 and visited[nx][ny]==0 :
            dfs(nx, ny)
        # if array[nx][ny] and not visited[nx][ny] :    # 위와 동일
        #     dfs(nx, ny)


T = int(input())
for t in range(T):
    m, n, k = map(int,input().split())
    array = [[0] * m for _ in range(n)] # 가로(m) X 세로(n)
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int,input().split())
        array[y][x] = 1     # y가 행이니까 (위아래)

    # # 입력 확인용    
    # for a in array:
    #     print(a)

    result = 0

    # 모든 정점을 돌면서 dfs 수행 (방문하지 않았을 경우에만)
    for i in range(n):
        for j in range(m):
            if array[i][j]==1 and visited[i][j]==0 :
                dfs(i, j)
                result += 1
    print(result)
