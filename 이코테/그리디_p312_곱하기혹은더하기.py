import sys
sys.stdin = open("input2.txt", "r")


"""
02984

576
"""

"""
567

210
"""

# 0일 땐 버리고
# 나머지는 다 곱하면 제일 큰거 같은데
s = list(input())

# 숫자로 바꾸어줌
for i in range(len(s)):
    s[i] = int(s[i])

    if s[i] == 0: # 0일 경우에는 1로 바꾸어버림 (곱할거니까)
        s[i] = 1

result = 1
for num in s:
    result *= num
print(result)