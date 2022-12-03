import sys
sys.stdin = open("input2.txt", "r")

from collections import deque
def bfs(start, find):

    # 큐를 생성하고, 시작노드의 거리는 0 으로 초기화
    que = deque([(start, 0)])

    # 처음에 받은 노드 방문처리
    visited[start] = True 
    
    
    while que:
        # d : start노드부터 현재노드(v) 까지의 거리
        v, d = que.popleft()
        
        # 현재노드(v)가 찾고자 하는 노드(find) 일 경우 d(거리)를 반환
        if v == find:
            return d
        
        # 현재 노드에 연결되어 있는 : 다음노드(e), 길이(l) <--for-- graph
        for e, l in graph[v]:
            if visited[e] == False: # 연결된노드(e) 가 처음 방문
                visited[e] = True # 방문처리
                que.append((e, d+l)) # 지금까지 노드를 찾으면서 거리를 기록
                print(que)    

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
    