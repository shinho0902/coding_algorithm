import sys
sys.stdin = open("input1.txt", "r")

N = list(input())
for i in range(len(N)):
    N[i] = int(N[i])
N.sort(reverse=True)
for n in N:
    print(n,end='')
