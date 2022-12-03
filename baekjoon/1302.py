import sys
sys.stdin = open("input1.txt", "r")

# 1302: 베스트셀러

n = int(input())
books = []
for i in range(n):
    data = input()
    books.append(data)

books_set= list(set(books))
books_set.sort()
cnt = [0] * len(books_set)

for k in range(len(books_set)):
    for i in range(len(books)):
        if books_set[k] == books[i]:
            cnt[k] += 1
max = 0
for i in range(len(cnt)):
    if max < cnt[i]:
        max = cnt[i]
        max_book = books_set[i]

# print(books_set)
# print(cnt)

print(max_book)