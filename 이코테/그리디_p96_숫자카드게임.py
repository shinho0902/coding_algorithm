import sys
sys.stdin = open("input1.txt", "r")

"""
3 3
3 1 2
4 1 4
2 2 2

2
"""

"""
2 4 
7 3 1 8
3 3 3 4

3
"""

n, m = map(int,input().split()) # n:행 , m: 열 갯수
arr = [list(map(int,input().split())) for _ in range(n)]    # n 행을 가진 2차원 배열 입력 받기


mins = []
for i in range(n):
    min_row = min(arr[i]) # 행별 최소값
    mins.append(min_row)

col_idx = mins.index(max(mins)) # 행별 최소값들 중에서 최대가 있는 행

print(min(arr[col_idx]))

