T = int(input())
num = []
for i in range(T):
    num.append(int(input()))

for i in num:
    dp = [0 for _ in range(i+1)]

    for k in range(0, i+1):
        if k == 0:
            dp[k] = 1
        elif k == 1:
            dp[k] = 2
        elif k == 2:
            dp[k] = 4
        else:
            dp[k] = dp[k-1] + dp[k-2] + dp[k-3]

    print(dp[i-1])