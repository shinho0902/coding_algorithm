n = int(input()) # n X n 크기 
x, y = 1, 1
plans = input().split()

# L,R,U,D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i] # 새로운 좌표
            ny = y + dy[i]
    
    # 공간을 벗어나는 경우 무시 (좌표를 업데이트 하지 x)
    if (nx<1) or (ny<1) or (nx>n) or (ny>n):
        continue
    # 이동 수행
    x, y = nx , ny

print(x,y)