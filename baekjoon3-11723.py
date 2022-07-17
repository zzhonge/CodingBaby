import sys

N = int(sys.stdin.readline())
S = set()
ALL = [i for i in range(1,21)]

for i in range(N):
    value = sys.stdin.readline().strip().split()
    if len(value) == 1:
        if value[0] == "all":
            S = set(ALL)
        elif value[0] == "empty":
            S.clear()

    else:
        real = value[0]
        x = value[1]
        x = int(x)
        if real == "add":
            S.add(x)
        elif real == "remove":
            S.discard(x)
        elif real == "check":
            if x in S:
                print(1)
            else:
                print(0)
        elif real == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
