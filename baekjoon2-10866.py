import sys

N = int(input())
deque = []

for i in range(N):
    value = list(sys.stdin.readline().split())
    real = value[0]

    if real == "push_front":
        deque.insert(0,value[1])
    elif real == "push_back":
        deque.append(value[1])
    elif real == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque.pop(0)
    elif real == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            deque.pop(-1)
    elif real == "size":
        print(len(deque))
    elif real == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif real == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif real == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
