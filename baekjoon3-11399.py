N = int(input())
P = sorted(list(map(int, input().split())))

ATM = []
# 12334
# 1 3 6 9 13
for i in range(N):
    ATM.append(sum(P))
    P.pop()

print(sum(ATM))
