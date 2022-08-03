import sys
strings = list(sys.stdin.readline().strip())
strings2 = []

N = int(sys.stdin.readline().strip())

for i in range(N):
    k = list(sys.stdin.readline().strip().split())
    oh = k[0]
    if oh == "P":
        strings.append(k[1])
    elif oh == "D":
        if len(strings2) == 0:
            pass
        else:
            strings.append(strings2.pop())
    elif oh == "L":
        if len(strings) == 0:
            pass
        else:
            strings2.append(strings.pop())
    elif oh == "B":
        if len(strings) == 0:
            pass
        else:
            strings.pop()
strings.extend(reversed(strings2))
for i in strings:
    print(i, end = "")

# for i in range(N):
#     k = list(sys.stdin.readline().strip().split())
#     if k[0] == "P":
#         strings.insert(strings.index('V'), k[1])
#     elif k[0] == "L":
#         if strings.index('V') == 0:
#             pass
#         else:
#             strings.insert(strings.index('V')-1, 'V')
#             strings.pop(strings.index('V')+2)
#     elif k[0] == "D":
#         if strings.index('V') == -1:
#             pass
#         else:
#             strings.insert(strings.index('V') + 1, 'V')
#             strings.pop(strings.index('V'))
#     elif k[0] == "B":
#         if strings.index('V') == 0:
#             pass
#         else:
#             strings.pop(strings.index('V')-1)
#
# strings.remove('V')
#
# for i in strings:
#     print(i, end= "")


