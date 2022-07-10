N = int(input())
A = list(map(int,input().split()))

count = 0
for i in A:
    if i == 1 :
        pass
    elif i != 1:
        for j in range(2,i+1):
            if i % j == 0 and i // j != 1:
                break
            elif i % j == 0 and i // j == 1:
                count += 1
print(count)
