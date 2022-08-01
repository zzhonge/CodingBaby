import sys

N = int(input())

for i in range(N):
    sentence = list(map(str, sys.stdin.readline().strip().split()))
    for j in sentence:
        print(j[::-1], end=" ")