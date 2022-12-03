n, m = map(int,input().split())

# array = [[0]*m for _ in range(n)]

array = [list(map(int,input().split())) for _ in range(n)] # n행을 가진 2차원 배열 입력받기

# print(array)

"""
3 3
3 1 2
4 1 4
2 2 2

2
"""

"""
2 4 
7 3 1 8
3 3 3 4

3
"""

result = min(array[0])
for i in range(n):
    result = max(result,min(array[i]))
#    if result < min(array[i]):
#        result = min(array[i])
    
print(result)
