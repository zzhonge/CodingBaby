while 1:
    A = input()
    i = 0
    if int(A) != 0:
        if len(A) % 2 == 0:
            while i <= len(A)//2:
                if int(A[i])==int(A[-i-1]):
                    i = i+1
                else:
                    print("no")
                    break

                if i == len(A)//2:
                    print("yes")

        elif len(A) % 2 == 1:
            while i <= len(A) // 2:
                if int(A[i]) == int(A[-i - 1]):
                    i = i + 1
                else:
                    print("no")
                    break

                if i == len(A) // 2 + 1:
                    print("yes")
    else:
        break