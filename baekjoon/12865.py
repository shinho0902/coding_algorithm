import sys
sys.stdin = open("input1.txt", "r")

# 12865 - dp (못품)


items = []

n, k = map(int,input().split())
for _ in range(n):
    w, v = map(int,input().split())
    per_wv = v / w
    items.append([w, v, per_wv])

# print(items)    
items = sorted(items, key=lambda x:x[2], reverse=True)
print(items)

tot = 0
for item in items:
    tot += item[0]
    if tot > k:
        tot -= item[0]
        break
print(tot)
     