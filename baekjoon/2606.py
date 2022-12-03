import sys
sys.stdin = open("input1.txt", "r")


# 2606
n = int(input()) # 노드수
m = int(input()) # 간선수

# 그래프 생성 (정점의 개수 만큼)
graph = [[] for _ in range(n+1)]
# print(graph)

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph)



from collections import deque
def bfs(n):
    cnt = 0
    que = deque([n])
    visited[n] = True
    while que:
        v = que.popleft()
        # print(v, end=' ')
        cnt += 1
        for e in graph[v]:
            if visited[e] == False:
                que.append(e)
                visited[e] = True
    return cnt

visited = [False] * (n+1)

print(bfs(1)-1)
