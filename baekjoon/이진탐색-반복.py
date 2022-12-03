# array: 원소가 들어있는 리스트
array = [1,3,5,7,9,11,13,15,17,19]
# n: 원소의 개수, target: 찾고자 하는 값
n, target = 10, 6

# 정렬
array.sort()


start = 0
end = n
result = None

while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
        result = mid
        break
    elif array[mid] > target:
        end = mid - 1
    elif array[mid] < target:
        start = mid + 1
    else:
        result = None


if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print('결과 인덱스:', result)
