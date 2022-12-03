# 11399 그리디 (26분)

n = int(input())
p = list(map(int,input().split()))

p.sort()
# print(p)
sum = 0
result = 0
for i in range(n):
    sum += p[i]
    result += sum
    

print(result)