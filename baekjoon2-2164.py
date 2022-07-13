# N = int(input())
# N_list = [i for i in range(1,N+1)]
#
# for j in range(N):
#     N_list.pop(-N+j)
#     if len(N_list) == 1:
#         break
#     N_list.append(N_list[-N+j+1])
#     N_list.pop(-N+j)
#
# print(N_list[0])

from collections import deque

N = int(input())
N_list = deque([i for i in range(1,N+1)])

while(len(N_list) > 1) :
    N_list.popleft()
    A = N_list.popleft()
    N_list.append(A)

print(N_list[0])