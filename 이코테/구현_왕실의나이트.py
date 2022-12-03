# 현재 나이트의 위치 입력
input_data = input() # a1

row = int(input_data[1]) # 행
col = int(ord(input_data[0])) - int(ord('a')) + 1 # 열

# print(row,',',col) # a1 -> 1,1

# 나이트가 이동할수 있는 8가지 방향 정의 (step[0],step[1])
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]


# 8가지 방향에 대해 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if (next_row>=1) and (next_row<=8) and (next_col>=1) and (next_col<=8):
        result +=1 

print(result)