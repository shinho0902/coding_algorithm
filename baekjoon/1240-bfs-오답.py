import sys
sys.stdin = open("input2.txt", "r")

from collections import deque
def bfs(v, b):

    que = deque([(v)])

    visited[v] = True # 처음에 받은 노드 방문처리
    cnt = 0
    while que:

        v = que.popleft()

        for e in graph[v]:

            if e[0] == b:
                # print('e[0],e[1]', e[0], e[1])
                cnt += e[1]
                break
            if visited[e[0]] == False: # 연결된노드(e) 가 처음 방문
                que.append(e[0])
                visited[e[0]] = True # 방문처리
                # print('e[0],e[1]', e[0], e[1])
                cnt += e[1]

    return cnt


n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

# d: x,y 사이 거리
for _ in range(n-1):
    x, y, d = map(int,input().split())
    graph[x].append((y, d))
    graph[y].append((x, d))

# print(graph)
# print()

for _ in range(m):
    a, b = map(int,input().split())
    # print(a, b)
    visited = [False for _ in range(n+1)]
    print(bfs(a, b))



