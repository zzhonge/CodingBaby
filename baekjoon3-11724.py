import sys
sys.setrecursionlimit(10**4)
N ,M = map(int, sys.stdin.readline().strip().split())

graph = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = graph[b][a] = 1
count = 0

check = [0] * (N+1)
def searching(x):
    check[x] = 1
    for i in range(1, N+1):
        if graph[x][i] and check[i] == 0:
            searching(i)

for i in range(1, N+1):
    if check[i] == 0:
        searching(i)
        count += 1

print(count)

# global count
# for i in range(N):
#     for j in range(N):
#
#         if graph[i][j] == 1:
#             count += 1
#             for k in range(N):
#                 if graph[k][y] or graph[x][k] == 1:
#                     graph[k][y] = graph[x][k] = 0
#                     searching(k,y)
#                     searching(x,k)
#                     return