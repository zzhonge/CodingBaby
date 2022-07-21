n = int(input())

dp = [0] * (n+1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[n])
# N = int(input())
# count = 0
#
# numbers = [3**i for i in range(1,13)]
# numbers_1 = [3**i+1 for i in range(1,13)]
# numbers_2 = [3**i+2 for i in range(1,13)]
#
# while N > 1:
#     if N % 3 == 0:
#         N /= 3
#         count += 1
#         continue
#
#     elif N in numbers_1 or numbers_2:
#         N -= 1
#         count += 1
#         continue
#
#     elif N % 3 != 0 and N % 2 == 0 and N not in numbers_1:
#         N /= 2
#         count += 1
#         continue
#
#     elif N % 3 != 0 and N % 2 == 1 and N not in numbers_2:
#         N -= 1
#         count += 1
#         continue
#
# print(count)