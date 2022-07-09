T = int(input())
for i in range(T):
    R, S = input().split()
    output = ''
    for j in S:
        output = output + j  * int(R)
    print(output)



# T = int(input())
#
# for i in range(T):
#     R, S = input().split()
#     for j in range(len(S)):
#         print(str(S[j])*int(R), end='')