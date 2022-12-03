import sys
sys.stdin = open("input1.txt", "r")

# 1697

# MAX 범위 잘 봐야함 
from collections import deque
def bfs(n):
    que = deque([n])
    while que:
        now_pos = que.popleft()

        # 같다면 현재 노드의 방문회수 리턴
        if now_pos == k:
            return visited[now_pos]
        

        directions = [now_pos-1, now_pos+1, now_pos*2]
        for next_pos in directions: # i는 만들어진 노드들
            if (0 <= next_pos <= MAX) and (visited[next_pos] == 0): # not visited[next_pos]
                # 방문 리스트에 (이전 노드의 간선수(시간)) + 1 을 해주어 시간을 셈
                visited[next_pos] = visited[now_pos] + 1 
                que.append(next_pos)



n, k = map(int,input().split())
MAX = 100001
visited = [0] * (MAX+1)

print(bfs(n))