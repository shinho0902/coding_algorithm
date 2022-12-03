import sys
sys.stdin = open("input1.txt", "r")

# MAX 범위 잘 봐야함 


from collections import deque
def dfs(n, k):
    que = deque([n])

    while que:
        n = que.popleft()
        
        if n == k:
            return visited[n]

        directions = [n-1, n+1, n*2]
        for nx in directions:
            if (0 <= nx <= MAX) and visited[nx] == 0:
                visited[nx] = visited[n] + 1
                que.append(nx) 
                    

n, k = map(int,input().split())

MAX = 100001
visited = [0] * (MAX+1)

print(dfs(n, k))


# print(visited)

