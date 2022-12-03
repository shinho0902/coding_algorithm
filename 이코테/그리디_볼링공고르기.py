from sympy import And


n, m = map(int,input().split())
weights = list(map(int,input().split()))

# from itertools import combinations
# result_set = set(list(combinations(weight,2)))
# print(result_set)
# print(len(result_set))

i,result = 0,0


for i in weights:
    for j in weights:
        if i!=j and i<j:
            print(i,j)
            result += 1 


print(result)