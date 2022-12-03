# 6730 장애물 경주 난이도
T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    cha_arr = []
    for i in range(len(arr)):
        if i < len(arr)-1:
            cha = arr[i+1]-arr[i]
            cha_arr.append(cha)
    up_result = max(cha_arr)
    down_result = -min(cha_arr)

    if up_result<0:
        up_result = 0
    if down_result<0:
        down_result = 0

    print(f'#{t+1} {up_result} {down_result}')

