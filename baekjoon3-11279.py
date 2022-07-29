import heapq
import sys
N = int(sys.stdin.readline())

q = []

for i in range(N):
    k = int(sys.stdin.readline())
    if k == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (-k, k))
