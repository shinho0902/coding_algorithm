import sys
sys.stdin = open("input1.txt", "r")



from collections import deque

def bfs(x, y):
    que = deque([(x, y)])

    array[x][y] == 1 # 방문

    while que:
        x, y = que.popleft()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue


            if array[nx][ny] == 1: # 방문하지 않았을때       
                que.append((nx, ny))    
                array[nx][ny] = array[x][y] + 1 # 방문처리

 
# 입력
n, m = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input())))



bfs(0,0)

# for a in array:
#     print(a)


print(array[n-1][m-1])
