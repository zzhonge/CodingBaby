import sys

N = int(input())
stack = []

for i in range(N):
    value = list(sys.stdin.readline().split())
    if value[0] == "push":
        stack.append(value[1])

    elif value[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    elif value[0] == "size":
        print(len(stack))

    elif value[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif value[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()