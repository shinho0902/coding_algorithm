import sys
sys.stdin = open("input4.txt", "r")



n = int(input())
limit = list(map(int,input().split()))
limit.sort(reverse=True)
m = int(input())
box = list(map(int,input().split()))
box.sort(reverse=True)



# print(limit)
# print(list(box))
# print('*'*10)

time = 0
while box:
    if max(limit) < max(box):
        time = -1
        break
    for i in range(len(limit)):
        if not box:
            break
        for j in range(len(box)):
            if limit[i] >= box[j]:
                box.remove(box[j])
                break

    time += 1
print(time)