N = int(input())
A = list(map(int, input().split()))
A.sort()
print(A[0], A[N-1])

#list(map(int, input().split()))이랑
#input().split()했을때 sort값이 왜 다를까 씨발?