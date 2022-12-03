import sys
sys.stdin = open("input1.txt", "r")


# 2110: 공유기설치 나동빈 이코테 p369
import sys
input = sys.stdin.readline

n, c = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
# 1 2 8 4 9

arr.sort()
# 1 2 4 8 9

start = arr[1] - arr[0]
end = arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start + end) // 2 # mid는 gap 을 의미
    
    value = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if arr[i] >= value + mid:
            value = arr[i] # value: 공유기 설치된 곳의 값
            count += 1
    
    if count >= c: # c개 이상의 공유기를 설치할수 있는경우
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)

