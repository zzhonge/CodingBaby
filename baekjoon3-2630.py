import sys
N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

white =0
blue = 0

def paper(graph, x, y, n):
    global white, blue
    point = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if point != graph[i][j]:
                paper(graph,x,y,n//2)
                paper(graph,x,y+n//2,n//2)
                paper(graph,x+n//2,y,n//2)
                paper(graph,x+n//2,y+n//2,n//2)
                return

    if point == 1:
        blue += 1
    else:
        white += 1

paper(graph,0,0,N)
print(white)
print(blue)