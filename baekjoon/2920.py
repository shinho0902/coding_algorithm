import sys
sys.stdin = open("input.txt", "r")



arr = list(map(int,input().split()))

asc = True
desc = True

for i in range(1,len(arr)):
    # 오름차순
    if arr[i-1] < arr[i]:
        desc = False
    # 내림차순
    elif arr[i-1] > arr[i]:
        asc = False
    

if asc:
    print('ascending')
elif desc:
    print('descending')
else:
    print('mixed')
