while 1:
    A = list(map(int, input().split()))
    A.sort()
    if A[0] and A[1] and A[2] != 0:
        if A[0]**2 + A[1]**2 == A[2]**2:
            print("right")
        else:
            print("wrong")
    else:
        break

