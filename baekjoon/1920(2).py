import sys
sys.stdin = open("input1.txt", "r")

# 1920: 수찾기 - 이진탐색

def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

m = int(input())
targets = list(map(int,input().split()))


for target in targets:
    result = binary_search(arr, target, 0, n-1)
    if result == None:
        print(0)
    else:
        print(1)