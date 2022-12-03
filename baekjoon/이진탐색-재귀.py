# 이진탐색 - 재귀
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    # 중간의 값과 타겟값이 같은 경우 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간의 값보다 타겟값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간의 값보다 타겟값이 큰 경우 오른쪽 확인
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)



# array: 원소가 들어있는 리스트
array = [1,3,5,7,9,11,13,15,17,19]
# n: 원소의 개수, target: 찾고자 하는 값
n, target = 10, 7

# 정렬
array.sort()

# 이진 탐색 수행 결과 출력 --> index 값
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result)

    