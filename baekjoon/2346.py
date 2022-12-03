import sys
sys.stdin = open("input1.txt", "r")


from collections import deque

n = int(input())
data = list(map(int,input().split()))

que = deque()
for idx, num in enumerate(data):
    que.append([idx+1, num])

result = [] # index es

# 초기
pop_data = que.popleft()
m = pop_data[1] # 회전수
result.append(pop_data[0]) # index

for i in range(n-1):

    if m > 0:
        for j in range(m-1):
            que.append(que.popleft())

    else:
        for k in range(abs(m)):
            que.appendleft(que.pop())

    pop_data = que.popleft()
    m = pop_data[1] # 회전수
    result.append(pop_data[0]) # index
    

print(*result)

# 1 4 5 3 2 