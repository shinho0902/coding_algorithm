import sys
sys.stdin = open("input1.txt", "r")

from collections import deque

T = int(input())

for t in range(T):

    n, m = map(int,input().split())
    que = deque(map(int,input().split()))
    
    que = deque((i, idx) for idx, i in enumerate(que))
    
    cnt = 0
    while True:
        # 맨 앞에 값이 큐의 최대값이면
        if que[0][0] == max(que, key=lambda x:x[0])[0]:
            cnt += 1

            # m번째 있던 원소라면 출력
            if que[0][1] == m:
                print(cnt)
                break
            # 맨앞 원소 제거
            else:
                que.popleft()

        # 최대값이 아니면 계속 회전
        else:
            que.append(que.popleft())


    # print(que)
   