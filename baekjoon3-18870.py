import sys
N = int(sys.stdin.readline())

q = list(map(int,sys.stdin.readline().strip().split()))

real = set(q)
newq = list(real)
newq.sort()

qq = {}
for i in range(len(newq)):
    qq[newq[i]] = i

for i in q:
    print(qq[i], end = " ")


# real = q[0]
# new = sorted(q[0])
# print(real)
# print(new)
#
# k = []
# for i in range(N):
#     if new.index(real[i]) - new.index(real[i])
#         k.append([real[i],new.index(real[i])])
#
#
#
#
# for i in range(N):
#     print(k[i][1], end=" ")