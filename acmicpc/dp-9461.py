# https://www.acmicpc.net/problem/9461

t = int(input())
arr = [int(input()) for _ in range(t)]

n = max(arr)

dp = [0] * 101
dp[1:5+1] = [1,1,1,2,2]

if n > 5:
    for i in range(5, n+1):
        dp[i] = dp[i-1] + dp[i-5]

for n in arr:
    print(dp[n])
