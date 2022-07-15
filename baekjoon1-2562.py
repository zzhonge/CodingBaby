value = []

for i in range(9):
    value.append(int(input()))

print(sorted(value)[-1])
print(value.index(sorted(value)[-1])+1)



