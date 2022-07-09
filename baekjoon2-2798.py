N, M = map(int, input().split())
number = list(map(int,input().split()))
sumlist = []
sum = 0
for a in number:
    for b in number:
        if a==b:
            continue
        for c in number:
            if a==b or b==c or c==a:
                continue
            sum = sum + a + b + c
            sumlist.append(sum)
            sum = 0
sumlist.sort()
for i in sumlist:
    if i > M:
        del sumlist[sumlist.index(i):]
print(sumlist[-1])