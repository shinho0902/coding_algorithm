import sys
sys.stdin = open("input2.txt", "r")

# 1236: 성 지키기

n, m = map(int,input().split())
arr = []

for i in range(n):
    col = list(input())
    arr.append(col)

# print(arr)

# 행 탐색
cnt1 = 0
for i in range(len(arr)):
    flag = False
    for j in range(len(arr[0])):
        # print(arr[i][j], end ='')
        if arr[i][j] == 'X':
            flag = True
    
    if flag == False:
        # print(arr[i], end ='')
        cnt1 += 1
# print(cnt1)

# 열 탐색
cnt2 = 0
for i in range(len(arr[0])):
    flag = False
    for j in range(len(arr)):
        # print(arr[j][i], end ='')
        if arr[j][i] == 'X':
            flag = True
    
    if flag == False:
        # print(arr[j], end ='')
        cnt2 += 1
# print(cnt2)

print(max(cnt1, cnt2))