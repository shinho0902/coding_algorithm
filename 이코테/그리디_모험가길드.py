n = int(input())
arr = list(map(int,input().split()))

arr.sort()

# print(arr)
cnt = 0
result = 0
for i in arr:
    cnt += 1
    if cnt >= i :
        result += 1
        cnt = 0

print(result)

