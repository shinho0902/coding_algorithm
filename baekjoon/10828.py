import sys
sys.stdin = open("input1.txt", "r")
###

import sys
input = sys.stdin.readline # 빠른 입력 함수 사용
# from collections import deque

n = int(input())
stack = list()
for i in range(n):
    com = input().split()
    # com = sys.stdin.readline().split()
    if com[0] == 'push':
        stack.append(com[1])
    elif com[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    
