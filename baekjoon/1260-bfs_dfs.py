import sys
sys.stdin = open("input1.txt", "r")

# 1260: DFS 와 BFS
from collections import deque

def dfs(v):
    visited[v] = True # 현재 노드를 방문처리
    print(v, end=' ')
    for e in graph[v]: # 현재 노드(v)와 연결된 노드(e)
        if not visited[e]: # 연결된 노드(e)가 방문처리 되있지 않을경우
            dfs(e)

def bfs(v):
    que = deque([v])
    visited[v] = True # 처음에 받은 노드 방문처리
    while que:
        v = que.popleft()
        print(v, end=' ')
        for e in graph[v]: # 현재 노드(v)와 연결된 노드(e)
            if visited[e] == False: # 연결된 노드(e)가 방문처리 되있지 않을경우
                que.append(e) # 큐(que)에 연결된 노드(e)를 넣는다
                visited[e] = True # 연결된 노드(e) 방문처리

# 입력
n, m, v = map(int,input().split())

# 정점의 갯수(n) 만큼 리스트를 생성
graph = [[] for _ in range(n+1)]

# 간선의 갯수(m) 만큼 반복 입력 받음
for _ in range(m):
    x, y = map(int,input().split())
    # x, y가 서로 연결되어 있으니까
    graph[x].append(y)
    graph[y].append(x)

# 가장 낮은 번호부터 방문할수 있게 정렬
for e in graph:
    e.sort()

# print('graph:', graph)

# 각 노드가 방문된 정보 기록
visited = [False] * (n+1)

dfs(v)
print()

# 각 노드가 방문된 정보 기록
visited = [False] * (n+1)

bfs(v)