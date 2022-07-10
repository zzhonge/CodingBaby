N, K = map(int,input().split())
N1 = 1
K1 = 1
for i in range(N,N-K,-1):
    N1 *= i
for i in range(K,0,-1):
    K1 *= i

print(N1//K1)
