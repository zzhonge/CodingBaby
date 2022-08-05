import sys
PS = list(sys.stdin.readline().strip())
cnt = 0
poppin = []


for i in range(len(PS)):
    if PS[i] == '(' and PS[i+1] == ')':
        cnt += len(poppin) -1

    if PS[i] == '(':
        poppin.append(PS[i])
    elif PS[i] == ')':
        cnt += 1
        poppin.pop()
print(cnt)