n = input() 
# K1KA5CB7
# AJKDLSI412K4JSJ9D


num = 0
alp = ''
for i in n:
    if i>='A' and i<='Z':
        alp = alp + i
    elif i>='0' and i<='9':
        num += int(i)

alp = ''.join(sorted(alp))

result = alp + str(num)
print(result)

