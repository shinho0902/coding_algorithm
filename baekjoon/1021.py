import sys
sys.stdin = open("input1.txt", "r")


from collections import deque

n, m = map(int,input().split())
lst = list(map(int,input().split()))
que = deque([i for i in range(1, n+1)])

# left # 맨앞 -> 맨뒤
def two(que):
    que.append(que.popleft())

# right # 맨뒤-> 맨앞
def three(que):
    que.appendleft(que.pop())

# 첫번째 연산해서 뽑아낼수 있을때까지
# 하나하나씩 찾아가면 됨 (왼, 오 어디가 가까운지 어떻게 알지?)

ans = 0
for i in range(len(lst)):
    target = lst[i]

    # 왼/오 가까운 곳 찾기 cnt1, cnt2
    cnt1 = 0
    for j in range(0, len(que)):
        cnt1 += 1
        if que[j] == target:
            break
    
    cnt2 = 0
    for k in range(len(que)-1, 0, -1):
        cnt2 += 1
        if que[k] == target:
            break
    
    # print('target', target)
    # print('que', *que)
    # print(cnt1, cnt2)

    while True:
        # print('que[0]', que[0])
        if que[0] == target:
            que.popleft()
            break

        # print('target', target)
        if cnt1 <= cnt2:
            two(que)
            ans += 1
            # print(que)
        else:
            three(que)
            ans += 1
            # print(que)

print(ans)

