N = int(input())
point = []

for i in range(N):
    x,y = map(int, input().split())
    point.append((x,y))

point.sort(key= lambda k : (k[0],k[1]))

for x,y in point:
    print(x,y)