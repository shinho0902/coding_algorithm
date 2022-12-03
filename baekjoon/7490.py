import sys
sys.stdin = open("input1.txt", "r")

# 7490: 0 만들기 - 패캠 나동빈

# 재귀적으로 연산자 리스트를 생성함 (몇개가 필요할까?)
def make_operators(arr, n):
    if len(arr) == n:
        operators_list.append(arr.copy())
        return

    arr.append(' ')
    make_operators(arr, n)
    arr.pop()

    arr.append('+')
    make_operators(arr, n)
    arr.pop()

    arr.append('-')
    make_operators(arr, n)
    arr.pop()

T = int(input())
for t in range(T):
    n = int(input())
    nums = [i for i in range(1, n+1)]
    operators_list = []
    # (숫자갯수)-1 개 만큼 연산자가 필요함
    make_operators([], n - 1)

    for operators in operators_list:
        string = ''
        for i in range(n-1):
            # "문자열" += 숫자 + 연산자
            string = string + str(nums[i]) + operators[i]
        # 마지막거: + 숫자
        string = string + str(nums[-1])
        # 공백일때 숫자 붙여서 계산한게 = 0
        if eval(string.replace(' ','')) == 0:
            print(string)

    print()