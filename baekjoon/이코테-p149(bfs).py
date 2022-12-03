import sys
sys.stdin = open("input1.txt", "r")


from collections import deque


def bfs(x, y):

    que = deque([(x,y)])
    array[x][y] == 1  # array == visited 
    
    # print(que)
    flag = 0
    while que:
        
        x, y = que.popleft()
        for dx, dy in vec:
            nx, ny = x+dx, y+dy 
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if array[nx][ny] == 0:
                # print(nx, ny)
                que.append([nx, ny])
                array[nx][ny] = 1
                flag = 1
    return flag

        
n, m = map(int,input().split())

array = []

for i in range(n):
    array.append(list(map(int,input())))

vec = [(0,1),(0,-1),(1,0),(-1,0)]

res = 0
for i in range(n):
    for j in range(m):
        # print('**', bfs(i, j))
        res += bfs(i, j)

print(res)