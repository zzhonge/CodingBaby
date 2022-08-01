import sys
N = int(input())

for i in range(N):
    sum = 0
    PS = list(sys.stdin.readline().strip())
    for i in PS:

        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1

        if sum < 0:
            print("NO")
            break

    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")
