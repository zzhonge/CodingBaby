N = int(input())
member = []

for i in range(N):
    A ,B = input().split()
    member.append((int(A),B))

member.sort(key= lambda x : x[0])

for age, name in member:
    print(age, name)