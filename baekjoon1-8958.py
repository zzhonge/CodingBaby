T = int(input())

for i in range(T):
    sum = 0
    A = input().split("X")
    for n in A:
        j = len(n)
        while j > 0:
            sum += j
            j -= 1

    print(sum)