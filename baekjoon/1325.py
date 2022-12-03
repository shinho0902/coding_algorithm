import sys
sys.stdin = open("input1.txt", "r")

# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline

from collections import deque
def bfs(v):
    yes = []
    que = deque([v])
    visited[v] = True
    while que:
        v = que.popleft()
        # print(v, end=' ')
        yes.append(v)
        for e in graph[v]:
            if visited[e] == False:
                que.append(e)
                visited[e] = True
    return len(yes)



n, m = map(int,input().split())

graph = [[] for _ in range(n+1)] # 정점의 개수 만큼 리스트 생성

for _ in range(m):
    x, y = map(int,input().split())
    # graph[x].append(y)
    graph[y].append(x)


# print(graph)


# 모든 정점을 방문
max_idx, max_cnt = -1, -1
cnts = []
res = []
for i in range(1, n+1):
    visited = [False] * (n+1)
    cnts.append(bfs(i))

max_cnt = max(cnts)
for i in range(len(cnts)):
    if cnts[i] == max_cnt:
        print(i+1, end=' ')

# print(cnts)
