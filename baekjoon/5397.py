import sys
sys.stdin = open("input1.txt", "r")


T = int(input())

for t in range(T):
    data = input()
    left_stack = []
    right_stack = []

    # 스택을 좌우로 나누어 커서가 벽이라고 생각하고 숫자가 좌우로 이동
    for com in data:
        if com == '>':
            if right_stack:
                ch = right_stack.pop()
                left_stack.append(ch)
        elif com == '<':
            if left_stack:
                ch = left_stack.pop()
                right_stack.append(ch)
        elif com == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(com)

     # 커서가 중간에 있을수도 있으므로 right도 돌려서 붙여야함
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))


# delete 연산이 추가 된다면 right에서 pop해나가면 될듯