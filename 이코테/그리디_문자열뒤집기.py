s = input()

nums = []
for i in s:
    nums.append(int(i))

cnt_0 = 0
cnt_1 = 1

for i in range(len(nums)-1):

    if nums[i]!=nums[i+1]:
        
        if nums[i]==1:
            cnt_1 += 1
        elif nums[i]==0:
            cnt_0 += 1

result = min(cnt_0,cnt_1)

print(result)