T = int(input())
array = []

for i in range(T):
    array.append(int(input()))


def fibonacci(n):
    zero , one = 1, 1
    for i in range(n):
        zero, one = one, zero+one
    return one


array_zero = [1,0,1]
array_one = [0,1]

for i in range(max(array)):
    array_zero.append(fibonacci(i))
    array_one.append(fibonacci(i))
for i in array:
    print(array_zero[i],array_one[i])
