cpu = int(input())
N = int(input())

graph = [[0]*(cpu+1) for i in range(cpu+1)]
for i in range(N):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

count = []
visited_dfs = [0] * (cpu+1)

def dfs(x):
    visited_dfs[x] = 1
    count.append(x)
    for i in range(cpu+1):
        if visited_dfs[i] == 0 and graph[i][x]:
            dfs(i)

dfs(1)

print(len(count)-1)