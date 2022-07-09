scale1 = list(map(int, input().split()))
scale2 = []
scale3 = []
scale2.extend(scale1)
scale3.extend(scale1)
scale2.sort()
scale3.reverse()

if scale2 == scale1:
    print("ascending")
elif scale2 == scale3:
    print("descending")
else:
    print("mixed")