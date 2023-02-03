import sys
sys.stdin = open("input2.txt", "r")

"""
5
2 3 1 2 2

2
"""
"""
6
4 3 3 3 3 2


"""

n = int(input()) # n: 모험가 수
arr = list(map(int,input().split())) # 각 공포도

arr.sort(reverse=True) # asc O(nlogn)

i, cnt= 0, 0 # i: 반복문 인덱스, cnt: 그룹 몇 개 인지 결과값 카운트

while i < n:
    i += arr[i] # 가장 큰 수 만큼 인덱스(i)를 건너뛰어줌
    cnt += 1
    if i > n:   # 인덱스 넘어 갈 경우에는 
        cnt -= 1    # 카운트 하나 빼야함

print(cnt)