import sys
sys.stdin = open("input1.txt", "r")



from collections import deque
def bfs(x, y):
    que = deque([(x, y)])

    while que:
        x, y = que.popleft()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # 이동
        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            # 범위를 벗어날 경우
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            # 처음 방문하는 경우 & 이전과 같은 색상일 경우
            if visited[nx][ny] == False:
                if array[nx][ny] == array[x][y]:
                    que.append([nx, ny])
                    visited[nx][ny] = True # 방문처리



# 입력 #
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(str,input())))


# 색맹 X #
visited = [[False]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            visited[i][j] = True # 방문처리
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')


# R -> G 변경
for i in range(n):
    for j in range(n):
        if array[i][j] == 'R':
            array[i][j] = 'G' 


# 색맹 O #
visited = [[False]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            visited[i][j] = True # 방문처리
            bfs(i, j)
            cnt += 1
print(cnt)