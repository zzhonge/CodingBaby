N = int(input())
number = []
for i in range(N):
    number.append(int(input()))

number.sort()

for i in number:
    print(i)