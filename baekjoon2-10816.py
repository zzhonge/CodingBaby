N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()
p = {}

for i in N_list:
    if i in p:
        p[i] += 1
    else:
        p[i] = 1

for i in M_list:
    if i in p:
        print(p[i], end = " ")
    else:
        print(0, end = " ")

# for i in M_list:
#     K.append(str(N_list.count(i)))
# print(" ".join(K), sep="")