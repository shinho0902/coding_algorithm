data = input() 
# K1KA5CB7
# AJKDLSI412K4JSJ9D

result = []
num = 0
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        num += int(x)

# # 1
# result.sort()
# if num != 0:
#     result.append(str(num))
# print(''.join(result))

# 2
result = ''.join(sorted(result))
if num != 0:
    result = result + str(num)
print(result)

