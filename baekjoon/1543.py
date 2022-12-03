import sys
sys.stdin = open("input4.txt", "r")

# 1543: 문서 검색

text = input()
target = input()

# print(text)

cnt = 0
while text.find(target) != -1:
    n = text.find(target)
    # print(n)
    text = text[n + len(target):]
    # print(text)
    cnt += 1
print(cnt)

