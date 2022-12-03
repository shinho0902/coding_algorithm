data = input()
# 123402
# 7755

N = len(data)
sum_1 = 0
sum_2 = 0

for i in range(N):
    if i<N/2:
        sum_1 += int(data[i])
    else:
        sum_2 += int(data[i])


if sum_1 == sum_2:
    print('LUCKY')
else:
    print('READY')




