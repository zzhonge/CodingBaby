import sys

N, M = input().split()
Poketmon = []
Poketmon_n = {}
for i in range(int(N)):
    Poket = sys.stdin.readline().strip()
    Poketmon.append(Poket)
    Poketmon_n[Poket] = i + 1

for i in range(int(M)):
    checking = sys.stdin.readline().strip()

    if checking.isdigit():
        print(Poketmon[int(checking)-1])
    else:
        print(Poketmon_n[checking])


