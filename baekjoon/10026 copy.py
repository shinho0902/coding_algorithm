import sys
sys.stdin = open("input1.txt", "r")



from collections import deque
def bfs(x, y):
    que = deque([(x,y)])
    cnt = 1
    while que:
        x, y = que.popleft()
        direction = [(0,1),(0,-1),(1,0),(-1,0)]

        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            # 방문하지 않은 노드를 만날 때 마다 카운팅
            # 이동한 값이 1 이면 
            if array[nx][ny] == 'R':
                que.append([nx, ny])
                array[nx][ny] = 'V' 
                cnt += 1
    return cnt


n = int(input())
array = []
for _ in range(n):
    array.append(list(map(str,input())))

result = []
for i in range(n):
    for j in range(n):
        ###### 좌표 돌면서 1 일때만 bfs 실행 ######
        if array[i][j] == 'R':
            array[i][j] = 'V' # 방문처리
            res = bfs(i, j)
            result.append(res)

result.sort()
print(len(result))
for res in result:
    print(res)

for a in array:
    print(a)
