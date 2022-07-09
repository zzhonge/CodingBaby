T = int(input())
for k in range(T):
    A = list(map(int, input().split()))
    H = [i for i in range(1,A[0]+1)]
    W = []
    for i in range(1,A[1]+1):
        if i <= 9:
            W.append("{}{}".format(0,i))
        else:
          W.append(i)

    room_number = []
    for n in W:
        for m in H:
            room_number.append("{}{}".format(m,n))
    print(room_number[A[2]-1])