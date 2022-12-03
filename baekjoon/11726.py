import sys
sys.stdin = open("input1.txt", "r")

n = int(input())


arr = [0] * 10001
arr[1] = 1
arr[2] = 2

for i in range(3, 1001):
    arr[i] = arr[i-1] + arr[i-2]
    
print(arr[n]%10007)