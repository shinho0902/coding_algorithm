import sys
sys.stdin = open("input4.txt", "r")

import sys
# input = sys.stdin.readline
from collections import deque

# n: 트럭수, w: 다리길이, l: 최대하중
n, w, l = map(int,input().split())
# a: 트럭무게 리스트
a = list(map(int,input().split()))

bridge = deque([0 for i in range(w)])
wait = deque(a)

# print(bridge + wait)

cnt = 0

# 반환: 하중합 <- 다리위하중 + 기다리는 맨앞트럭 무게
def func_weighted_sum():
    if wait:
        return sum(bridge) + wait[0]
    else:
        return sum(bridge)


while bridge:
    
    # 뭐가 됐던지 간에 다리위는 한칸씩 이동
    bridge.popleft()

    # 하중합이 제한하중보다 낮을때 다리위로 트럭이 감
    if func_weighted_sum() <= l:
        if wait:
            bridge.append(wait.popleft())
    else:
        bridge.append(0)
    
    # print(*bridge, '||' ,*wait)
    cnt += 1 

print(cnt)