import sys
N, M = map(int, input().split())

Hear = set()
Watch = set()

for i in range(N):
    Hear.add(sys.stdin.readline().strip())
for i in range(M):
    Watch.add(sys.stdin.readline().strip())

MIX = sorted(list(Hear & Watch))
print(len(MIX))
for i in MIX:
    print(i)