import sys

T = int(input())
sys.setrecursionlimit(10**4)

def dfs(graph, row, col, m,n):
    if row == m or col == n or row == -1 or col==-1:
        return False
    if graph[col][row] == 1:
        graph[col][row] = 0
        dfs(graph, row + 1, col, m, n)
        dfs(graph, row, col + 1, m, n)
        dfs(graph, row-1, col, m, n)
        dfs(graph, row, col - 1, m, n)
        return  True


for t in range(T):
    count = 0
    m, n, k = map(int, input().split())
    graph = [[0]* m for j in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    for j in range(n):
        for i in range(m):
            if graph[j][i] == 1:
                if dfs(graph, i, j, m, n) == True:
                    count += 1
    print(count)
