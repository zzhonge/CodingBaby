N, M = map(int,input().split())

A = max(N,M)
B = min(N,M)

while A % B != 0:
    newA = A
    newB = B

    A = newB
    B = newA % newB
print(B)
print(N*M//B)