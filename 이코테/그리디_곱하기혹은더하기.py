s = input()

nums=[]
for i in s:
    nums.append(int(i))

result = 0
for num in nums:
    if (num == 0) | (result == 0):
        result += num
    else:
        result *= num
    
    

print(result)