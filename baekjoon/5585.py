import sys
sys.stdin = open("input1.txt", "r")

money = 1000 - int(input())

arr = [500,100,50,10,5,1]

cnt = 0

for coin in arr:
    cnt += money // coin  # 몫
    money %= coin # 나머지

print(cnt)