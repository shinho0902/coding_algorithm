import sys
sys.stdin = open("input1.txt", "r")

import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    num = int(input())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        abs_num = abs(num)
        heapq.heappush(heap, (abs_num, num))

