import sys
sys.stdin = open("input1.txt", "r")

import hashlib

S = input()

# 바이트 객체 구하기
encoded_data = S.encode()

# 해쉬 객체 생성
obj = hashlib.sha256(encoded_data)

# 해쉬 결과 반환
result = obj.hexdigest()


print(result)