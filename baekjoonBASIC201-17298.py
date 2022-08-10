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

from collections import deque

N = int(input())
nigga = deque(map(int, input().split()))
black = [-1] * N

for i in range(N-1):
    if nigga[i] < nigga[i+1]:
        black[i] = nigga[i+1]
    else:
        pass
