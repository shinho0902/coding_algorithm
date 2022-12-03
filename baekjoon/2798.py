import sys
sys.stdin = open("input.txt", "r")

n, m = map(int,input().split())
arr = list(map(int,input().split()))

total = 0
result = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            total = arr[i] + arr[j] + arr[k]
            if total <= m:
                result = max(total, result)

print(result)


# total = []
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         for k in range(j+1, len(arr)):
#             total.append(arr[i] + arr[j] + arr[k])

# total = sorted(list(set(total)),reverse=True)

# for num in total:
#     if num <= m:
#         print(num)
#         break
