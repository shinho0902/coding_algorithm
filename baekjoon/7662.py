import sys
sys.stdin = open("input1.txt", "r")

import sys
input = sys.stdin.readline

import heapq

def pop(heap): # heap과 deleted는 global 변수
    while heap: # 삭제할 원소 찾기
        data, id = heapq.heappop(heap) # 꺼내기
        if not deleted[id]: # 처음 삭제하는 원소일때
            deleted[id] = True
            return data
    return None # 삭제할 원소가 없으면 None 반환

T = int(input())
for t in range(T):
    # print(f'\n***CASE {t}***')
    k = int(input())
    
    min_heap = []
    max_heap = []
    
    current = 0   # 삽입할 원소의 인덱스 (ID값)
    deleted = [False] * (k + 1) # 각 원소의 삭제여부

    for i in range(k):
        # op) 'I': n을 Q에 삽입
        # 'D': Q에서 최댓값을 삭제 | 단 n=-1 경우 최솟값을 삭제
        # Q가 비어있는 경우는 연산무시
        op, data = input().split()
        data = int(data)
        if op == 'D':
            if data == -1:
                pop(min_heap)
            elif data == 1:
                pop(max_heap)
        elif op == 'I':
            heapq.heappush(min_heap, (data, current))
            heapq.heappush(max_heap, (-data, current))
            current += 1

    max_value = pop(max_heap)
    if max_value == None:
        print('EMPTY')
    else:
        # max_value는 min_heap에서도 꺼내지므로 다시 넣어줌
        heapq.heappush(min_heap, (-max_value, current))

        # 결과 출력
        print(-max_value, pop(min_heap))



