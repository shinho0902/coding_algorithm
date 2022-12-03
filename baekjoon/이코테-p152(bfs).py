import sys
sys.stdin = open("input1.txt", "r")


from collections import deque
def bfs(x, y):
    que = deque([(x, y)])
    array[x][y] == 1 # visited

    # 방향
    # directions = [(0,1),(0,-1),(-1,0),(1,0)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    while que:
        x, y = que.popleft()

        # 다음 이동
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            # print(nx, ny)

            # 좌표의 범위를 벗어나면
            if nx<0 or nx>=n or ny<0 or ny>=m:
                # print(nx, ny)
                continue
            
            # 벽인 경우
            if array[nx][ny] == 0:
                continue
            
            # 이동한 값이 1 이면
            if array[nx][ny] == 1:
                que.append((nx, ny))
                array[nx][ny] = array[x][y] + 1



# n * m  5x6
# 입력
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input())))


bfs(0, 0)

# for a in array:
#     print(a)

print(array[n-1][m-1])