import sys
sys.stdin = open("input1.txt", "r")

n = int(input())

# n = 100
dp = [0] * (n+10)

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] = dp[i] % 15746

# print(dp[:10])
print(dp[n])

