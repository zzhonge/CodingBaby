N, M, V = map(int, input().split())
graph = [[0]*(N+1) for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited_dfs = [0] * (N+1)
def dfs(V):
    visited_dfs[V] = 1
    print(V, end= ' ')
    for i in range(N+1):
        if visited_dfs[i] == 0 and graph[i][V]:
            dfs(i)

visited_bfs = [0] * (N+1)
def bfs(V):
    visited_bfs[V] = 1
    queue = []
    queue.append(V)
    while queue:
        node = queue.pop(0)
        print(node, end = ' ')
        for i in range(N+1):
            if visited_bfs[i] == 0 and graph[i][node]:
                queue.append(i)
                visited_bfs[i] = 1

dfs(V)
print()
bfs(V)

