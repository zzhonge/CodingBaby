import sys
from collections import deque
N, K = map(int, sys.stdin.readline().strip().split())
number = deque(i for i in range(1,N+1))
P = []

while(number):
    for i in range(K-1):
        number.append(number.popleft())
    P.append(str(number.popleft()))

print("<", ", ".join(P), ">", sep="")