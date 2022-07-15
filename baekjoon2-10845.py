import sys

N = int(input())
queue = []

for i in range(N):
    value = list(sys.stdin.readline().split())
    real = value[0]

    if real == "push":
        queue.append(value[1])

    elif real == "pop":
        if len(queue) != 0:
            print(queue[0])
            queue.pop(0)
        else:
            print(-1)

    elif real == "size":
        print(len(queue))

    elif real == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif real == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif real == "back":
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)


