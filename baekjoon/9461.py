import sys
sys.stdin = open("input1.txt", "r")



dp = [0] * 105
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4,105):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
    
        
# print(dp[:15])