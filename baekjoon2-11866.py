N, K = map(int, input().split())
number = [i for i in range(1,N+1)]
P = []

while(number):
    for i in range(K-1):
        number.append(number.pop(0))
    P.append(str(number.pop(0)))

print("<", ", ".join(P), ">", sep="")