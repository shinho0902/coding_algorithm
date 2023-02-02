import sys
sys.stdin = open("input1.txt", "r")

"""
5 8 3
2 4 5 4 6

46
"""

n, m, k = map(int,input().split()) # n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 몇번 더할수 있는지
arr = list(map(int,input().split())) # 배열
arr.sort(reverse=True) # desc : O(nlogn)
# 6 5 4 4 2
# 6+6+6+5+6+6+6+5 = 46

ans = 0
cnt = 0
# O(n)
for i in range(m):
    cnt += 1    # 카운트 증가
    if cnt % k == 0:    # 몇번더할수 있는지의 나머지 값이 0으로 떨어지면 횟수 다썼다는 뜻
        cnt = 0 # 카운트 초기화 (횟수)
        ans += arr[1]   # 2번째로 큰값을 더해줌
    else:
        ans += arr[0]

print(ans)

# 아이디어 : 가장 큰수랑 두번째 큰수만 알면 됨