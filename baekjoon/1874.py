import sys
sys.stdin = open("input1.txt", "r")


n = int(input())

ans = []
stack = []
cnt = 1

for i in range(1, n+1):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(ans))


"""
+ 1 push
+ 2 push
+ 3 push
+ 4 push
- 4 pop
- 3 pop
+ 5 push
+ 6 push
- 6 pop
+ 7 push
+ 8 push
- 8 pop
- 7 pop
- 5 pop
- 2 pop
- 1 pop
"""
"""
+ 1 push
- 1 pop
+ 2 push
- 2 pop
+ 3 push
+ 4 push
+ 5 push
- 5 pop
- 4 pop
- 3 pop
"""