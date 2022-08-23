# import sys
# N = int(sys.stdin.readline().strip())
# nigga = list(map(int, sys.stdin.readline().strip().split()))
#
# for i in range(N):
#     if i == N-1:
#         print(-1)
#         break
#     else:
#         for j in nigga[i+1:]:
#             if nigga[i] < j:
#                 print(j, end= " ")
#                 break
#         else:
#             print(-1, end = " ")

N = int(input())
nigga = list(map(int, input().split()))
black = [-1] * N
index = [0]

for i in range(1,N):
    while index and nigga[index[-1]] < nigga[i]:
        black[index[-1]] = nigga[i]
        index.pop()
    index.append(i)
for i in black:
    print(i, end=' ')