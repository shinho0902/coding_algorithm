import sys
sys.stdin = open("input3.txt", "r")

n = int(input())
k = int(input())

arr = list(map(int,input().split()))
arr.sort()


if k >= n:
    print(0)

else:
    # print(arr)

    dist_arr = []
    for i in range(len(arr)-1):
        dist_arr.append(arr[i+1]-arr[i])
    dist_arr.sort(reverse=True)

    for i in range(k-1):
        dist_arr[i] = 0

    print(sum(dist_arr))

    # print(n, k)
    # print(dist_arr)