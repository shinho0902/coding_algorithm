import sys
sys.stdin = open("input1.txt", "r")

import sys
input = sys.stdin.readline

import heapq

k, n = map(int,input().split())
data = list(map(int,input().split()))

heap = []
visited = set() # 이미 처리된수
max_value = max(data)

for x in data: # 초기 원소를 최소 힙에 삽입
    heapq.heappush(heap, x)

# N-1 개의 원소 꺼내기
for i in range(n-1): # 힙에서 원소를 N번 꺼내기
    element = heapq.heappop(heap)
    for x in data:
        now = element * x # 곱한 결과 계산
        # 힙의 크기가 N 이상이고 힙의 최댓값보다 곱한 결과가 크다면
        if len(heap) >= n and max_value < now:
            continue
        if now not in visited: # 처음 방문하는 수라면
            heapq.heappush(heap, now)
            max_value = max(max_value, now)
            visited.add(now) # 방문처리

# N번째 원소 꺼내기
print(heapq.heappop(heap))