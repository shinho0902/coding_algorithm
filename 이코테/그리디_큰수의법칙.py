n, m, k = map(int, input().split())
data = list(map(int,input().split()))

"""
5 8 3
2 4 5 4 6

46
"""

data.sort(reverse=True)
frist = data[0]
second = data[1]

result = 0
cnt = 0

for i in range(m):
    if cnt==k:
        result += second
        cnt = 0
    else :    
        result += frist
        cnt += 1

print(result)
