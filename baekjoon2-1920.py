N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

A.sort()

for i in B:
    start = 0
    end = N-1
    while 1:
        middle = (start + end) // 2
        if A[middle] == i:
            print(1)
            break

        if A[middle] > i:
            end = middle - 1
        elif A[middle] < i:
            start = middle + 1

        if start > end:
            print(0)
            break