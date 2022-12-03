import sys
sys.stdin = open("input1.txt", "r")


from collections import deque
n, k = map(int,input().split())
que = deque([i for i in range(1,n+1)])

# print(*que)


ans = []
for i in range(len(que)):
    for j in range(k):
        if j == k-1:
            num = que.popleft()
            ans.append(num)
        else:
            que.append(que.popleft())

# print(ans)

print('<',end='')
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end='')
    else:
        print(ans[i], end=', ')
print('>',end='')